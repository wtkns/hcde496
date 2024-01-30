from datetime import datetime
import urllib.request
import base64
import json
import time
import os
import subprocess
from PIL import Image
from io import BytesIO

ffmpeg = os.path.join("D:\\", "bin", "ffmpeg.exe")
project_name = "meshes"
webui_server_url = 'http://127.0.0.1:7860'

root_dir = os.path.join("D:\\", "hcde496")
project_dir = os.path.join(root_dir, "Projects", project_name)
image_in_dir = os.path.join(project_dir, "images", "input")
# pose_dir = os.path.join(project_dir, "images", "pose")
image_out_dir = os.path.join(project_dir, "images", "output")
# video_in_dir = os.path.join(project_dir, "videos", "input")
# video_out_dir = os.path.join(project_dir, "videos", "output")
# video_in_file = os.path.join(video_in_dir, f'{project_name}.mkv')

prompt = "bubbling cosmic debris"
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


def call_img2img_api(**payload):
    return call_api('sdapi/v1/img2img', **payload)

def img2img_payload(pl_image, pl_prompt, pl_negative_prompt, pl_seed = -1, pl_steps = 30, pl_denoise = 0.5):
    return {
            "prompt": pl_prompt,
            "negative_prompt": pl_negative_prompt,
            "seed": pl_seed,
            "steps": pl_steps,
            "width": 512,
            "height": 512,
            "denoising_strength": pl_denoise,
            "n_iter": 1,
            "init_images": [pl_image],
            "batch_size": 1,
            # "mask": encode_file_to_base64(r"B:\path\to\mask.png")
        }

def show_img(image_enc):
    Image.open(BytesIO(base64.b64decode(image_enc))).show()
    return 1

def blend_images(image_one_enc, image_two_enc, blend = 0.5):
    image_one_dec = Image.open(BytesIO(base64.b64decode(image_one_enc)))
    image_two_dec = Image.open(BytesIO(base64.b64decode(image_two_enc)))
    img_blend_dec = Image.blend(image_one_dec, image_two_dec, blend)
    blend_file = BytesIO()
    img_blend_dec.save(blend_file, format="JPEG")
    blend_bytes = blend_file.getvalue()  # blend_bytes: image in binary format.
    return base64.b64encode(blend_bytes).decode('utf-8')

if __name__ == '__main__':
    # extract_frames(video_in_file, image_in_dir, project_name, 30, 10, 15)
    denoise = 0.5
    batch_size = 1
    image_input_list = get_image_list(image_in_dir)
    seed_img_enc = encode_file_to_base64(image_input_list[100])
    # show_img(seed_img_enc)
    

    for filenum in range(len(image_input_list)): # (5): # 
        file_in = image_input_list[filenum]
        image_in_enc = encode_file_to_base64(file_in)
        blend_enc = blend_images(seed_img_enc, image_in_enc, blend = 0.25)
        payload = img2img_payload(blend_enc, prompt, negative_prompt, 30619249, 30, 0.5)
        response = call_img2img_api(**payload)
        images = response.get('images')
        image_out_path = os.path.join(image_out_dir, f'image-{filenum:03d}.jpg')
        print(image_out_path)

        for index, image in enumerate(response.get('images')):
            decode_and_save_base64(image, image_out_path)
            seed_img_enc = image

        # seed_img_enc = blend_enc
        # show_img(blend_enc)


    #     # print(payload)

        # 
        # 



    #         blend = blend_images(file_in, file_out, blend = 0.5)
    #         blend.show()
