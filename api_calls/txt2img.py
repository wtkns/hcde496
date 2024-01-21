from datetime import datetime
import urllib.request
import base64
import json
import time
import os

webui_server_url = 'http://127.0.0.1:7860'

prompt = "adorable puppies forever"
negative_prompt = "not anime"
out_dir = "D:\\hcde496\\"


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

def call_txt2img_api(**payload):
    response = call_api('sdapi/v1/txt2img', **payload)
    for index, image in enumerate(response.get('images')):
        save_path = os.path.join(out_dir, f'txt2img-{timestamp()}-{index}.png')
        decode_and_save_base64(image, save_path)

if __name__ == '__main__':
    payload = {
        "prompt": prompt,  # extra networks also in prompts
        "negative_prompt": negative_prompt,
        "seed": -1,
        "steps": 20,
        "width": 512,
        "height": 512,
        "cfg_scale": 7,
        "sampler_name": "DPM++ 2M Karras",
        "n_iter": 1,
        "batch_size": 1
    }

    call_txt2img_api(**payload)

