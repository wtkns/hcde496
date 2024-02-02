from datetime import datetime
import urllib.request
import base64
import json
import time
import os
import subprocess
from PIL import Image
from io import BytesIO

def get_image_list(image_dir):
    return [os.path.join(image_dir, image_name) for image_name in os.listdir(image_dir)] 

def get_img_in(filename):
    with open(filename, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

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

def img2img_payload(pl_image, pose_image, pl_prompt, pl_negative_prompt, pl_seed = -1, pl_steps = 30, pl_denoise = 0.5, guidance_scale = 7, ):
    return {
            "prompt": pl_prompt,
            "negative_prompt": pl_negative_prompt,
            "seed": pl_seed,
            "sampler_name": "DPM++ 2M Karras",
            "steps": pl_steps,
            "width": 512,
            "height": 512,
            "denoising_strength": pl_denoise,
            "n_iter": 1,
            "init_images": [pl_image],
            "batch_size": 1,
            "cfg_scale": guidance_scale,
            "alwayson_scripts": {
                "ControlNet": {
                    "args" : [{
                            "controlnet_module": "none",
                            "enabled": "true",
                            "image": {
                                "image": pose_image,
                            },
                            "module": "openpose",
                            "model": "control_v11p_sd15_openpose [cab727d4]",
                            "controlnet_guidance": 1.0,
                            "control_mode": "Balanced",
                            "weight": 1,
                            "guidance_end": 1,
                            "guidance_start": 0,
                        }]
                }
            }
        }

def show_img(image_enc):
    Image.open(BytesIO(base64.b64decode(image_enc))).show()
    return 1

def img_out_path(filenum):
    return os.path.join(session_path, f'image-{filenum:03d}.png')

def blend_images(image_one_enc, image_two_enc, blend = 0.5):
    # If alpha is 0.0, a copy of the first image is returned. If alpha is 1.0, a copy of the second image is returned. 
    image_one_dec = Image.open(BytesIO(base64.b64decode(image_one_enc)))
    image_two_dec = Image.open(BytesIO(base64.b64decode(image_two_enc)))
    img_blend_dec = Image.blend(image_one_dec, image_two_dec, blend)
    blend_file = BytesIO()
    img_blend_dec.save(blend_file, format="JPEG")
    blend_bytes = blend_file.getvalue()  # blend_bytes: image in binary format.
    return base64.b64encode(blend_bytes).decode('utf-8')

def denoise_incr(incr_num, total):
    return (((incr_num +1) * (0.3/total))+0.45)

if __name__ == '__main__':
    project_name = "meshes"
    webui_server_url = 'http://127.0.0.1:7860'

    root_dir = os.path.join("D:\\", "hcde496")
    project_dir = os.path.join(root_dir, "Projects", project_name)

    # input
    image_in_dir = os.path.join(project_dir, "images", "input")
    pose_dir = os.path.join(project_dir, "images", "pose")

    #output
    image_out_dir = os.path.join(project_dir, "images", "output", )

    session_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_path = os.path.join(image_out_dir, session_name )
    os.mkdir(session_path)

    prompt = "dancer cinematic exciting dramatic lighting highly detailed and intricate"
    negative_prompt = "monochrome"

    batch_size = 1
    pl_seed = 5432143
    image_input_list = get_image_list(image_in_dir)
    pose_list = get_image_list(pose_dir)
    project_len = len(image_input_list)

    seed_img_enc = encode_file_to_base64(image_input_list[0])
    

    for filenum in range(project_len): # (5): # 
        print(filenum, " of ", project_len)

        image_in_enc = encode_file_to_base64(image_input_list[filenum])
        pose_img_enc = encode_file_to_base64(pose_list[filenum])

        denoise = denoise_incr(filenum, len(image_input_list))
        print(denoise)

        # blend_enc = blend_images(seed_img_enc, image_in_enc, blend = 0.15)
        show_img(pose_img_enc)
        # add exponential random for blend? or based on modulo

        payload = img2img_payload(image_in_enc, pose_img_enc, prompt, negative_prompt, -1, 30, 0.5)
        response = call_img2img_api(**payload)
        images = response.get('images')

        image_out_path = img_out_path(filenum)
        print(image_out_path)
        for index, image in enumerate(response.get('images')):
            decode_and_save_base64(image, image_out_path)
            show_img(image)

            # seed_img_enc = image
