from datetime import datetime
import urllib.request
import base64
import json
import time
import os
import subprocess
from PIL import Image

ffmpeg = os.path.join("D:\\", "bin", "ffmpeg.exe")
project_name = "tophat"
webui_server_url = 'http://127.0.0.1:7860'

root_dir = os.path.join("G:\\", "Shared drives", "080 - Code", "Python", "hcde496")
project_dir = os.path.join(root_dir, "Projects", project_name)
image_in_dir = os.path.join(project_dir, "images", "input")
image_out_dir = os.path.join(project_dir, "images", "output")
video_in_dir = os.path.join(project_dir, "videos", "input")
video_out_dir = os.path.join(project_dir, "videos", "output")
video_in_file = os.path.join(video_in_dir, f'{project_name}.mkv')

prompt = "colorful dancer elaborate costume"
negative_prompt = "monochrome"

def extract_frames(video_file_path, image_path, image_name, start_time = 0, duration = 10, fps = 30):
    output_path = os.path.join(image_path, f'{image_name}%04d.jpg')
    command = [ffmpeg, '-ss', f'{start_time}', '-t', f'{duration}', '-i', f'"{video_file_path}"', '-vf', f'fps={fps}', '-y', f'"{output_path}"']
    cmdstr = ' '.join(command)
    print(cmdstr)

    if subprocess.run(cmdstr).returncode == 0:
        print ("FFmpeg Script Ran Successfully")
    else:
        print ("There was an error running your FFmpeg script")

def get_img_in(filename):
    with open(filename, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')
    
def blend_images(image_one, image_two, blend = 0.5):
    im1 = Image.open(image_one)
    im2 = Image.open(image_two)
    return Image.blend(im1, im2, blend)

def get_image_list(image_dir):
    return [os.path.join(image_dir, image_name) for image_name in os.listdir(image_dir)] 

def encode_file_to_base64(path):
    with open(path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

def decode_and_save_base64(base64_str, save_path):
    with open(save_path, "wb") as file:
        file.write(base64.b64decode(base64_str))

def call_api(api_endpoint, **payload):
    data = json.dumps(payload).encode('utf-8')
    request = urllib.request.Request(
        f'{webui_server_url}/{api_endpoint}',
        headers={'Content-Type': 'application/json'},
        data=data,
    )
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode('utf-8'))


def call_img2img_api(filenum, **payload):
    response = call_api('sdapi/v1/img2img', **payload)
    for index, image in enumerate(response.get('images')):
        print(index)
        print(response)

#         save_path = os.path.join(out_dir_i2i, f'img2img{filenum:03d}.png')
#         decode_and_save_base64(image, save_path)

if __name__ == '__main__':
    # extract_frames(video_in_file, image_in_dir, project_name, 30, 10, 15)
    denoise = 0.5
    batch_size = 1
    image_input_list = get_image_list(image_in_dir)

    # im3 = blend_images(image_input_list[0], image_output_list[150], 0.5)
    # im3.show()

    for filenum in range(len(image_input_list)):
        file = image_input_list[filenum]
        init_images = [
            encode_file_to_base64(file),
        ]

        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "seed": -1,
            "steps": 30,
            "width": 512,
            "height": 512,
            "denoising_strength": denoise,
            "n_iter": 1,
            "init_images": init_images,
            "batch_size": batch_size if len(init_images) == 1 else len(init_images),
            # "mask": encode_file_to_base64(r"B:\path\to\mask.png")
        }

        call_img2img_api(filenum, **payload)









