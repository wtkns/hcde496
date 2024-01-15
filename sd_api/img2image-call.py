from datetime import datetime
import urllib.request
import base64
import json
import time
import os

prompt = "tightrope walker in the mountains"
negative_prompt = ""
imgfileDir = "G:\\Shared drives\\080 - Code\\Python\\hcde496\\ffmpeg\\images\\"
webui_server_url = 'http://127.0.0.1:7860'
out_dir = "G:\\Shared drives\\080 - Code\\Python\\hcde496\\ffmpeg\\images\\"
out_dir_i2i = os.path.join(out_dir, 'img2img')



def timestamp():
    return datetime.fromtimestamp(time.time()).strftime("%Y%m%d-%H%M%S")


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
    response = call_api('sdapi/v1/img2img', **payload)
    for index, image in enumerate(response.get('images')):
        save_path = os.path.join(out_dir_i2i, f'img2img-{timestamp()}-{index}.png')
        decode_and_save_base64(image, save_path)


if __name__ == '__main__':



    img_dir_list = os.listdir(imgfileDir)

    for image in img_dir_list:
        imageFile = imgfileDir + image

        init_images = [
            encode_file_to_base64(imageFile),
        ]

        batch_size = 2
        payload = {
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "seed": -1,
            "steps": 20,
            "width": 512,
            "height": 512,
            "denoising_strength": 0.7,
            "n_iter": 1,
            "init_images": init_images,
            "batch_size": batch_size if len(init_images) == 1 else len(init_images),
            # "mask": encode_file_to_base64(r"B:\path\to\mask.png")
        }
        
        call_img2img_api(**payload)
