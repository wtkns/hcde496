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


def call_txt2img_api(**payload):
    return call_api('sdapi/v1/txt2img', **payload)

def text2img_payload(pl_prompt, pl_seed):
    return {
        "prompt": pl_prompt,
        "seed": pl_seed,
    }

def img2img_payload(pl_model, pl_image, pl_pose, pl_prompt, pl_neg_prompt, pl_seed = -1, pl_steps = 30, pl_denoise = 0.5, pl_guidance = 7, ):
    return {
            "model": pl_model,
            "prompt": pl_prompt,
            "negative_prompt": pl_neg_prompt,
            "seed": pl_seed,
            "sampler_name": "DPM++ 2M Karras",
            "steps": pl_steps,
            "width": 512,
            "height": 512,
            "denoising_strength": pl_denoise,
            "n_iter": 1,
            "init_images": [pl_image],
            "batch_size": 1,
            "cfg_scale": pl_guidance,
        }

def show_img(image_enc):
    Image.open(BytesIO(base64.b64decode(image_enc))).show()
    return 1

def img_out_path(filenum):
    return os.path.join(session_path, f'image-{filenum:03d}.png')

def decode_img(image):
    return Image.open(BytesIO(base64.b64decode(image)))
    
def blend_images(image_one_enc, image_two_enc, blend = 0.5):
    # If alpha is 0.0, a copy of the first image is returned. If alpha is 1.0, a copy of the second image is returned. 
    image_one_dec = decode_img(image_one_enc)
    image_two_dec = decode_img(image_two_enc)
    img_blend_dec = Image.blend(image_one_dec, image_two_dec, blend)
    blend_file = BytesIO()
    img_blend_dec.save(blend_file, format="JPEG")
    blend_bytes = blend_file.getvalue()  # blend_bytes: image in binary format.
    return base64.b64encode(blend_bytes).decode('utf-8')

def denoise_incr(incr_num, total):
    return (((incr_num +1) * (0.3/total))+0.45)

if __name__ == '__main__':
    # set params
    # model = "cyberrealistic_v41BackToBasics.safetensors [925bd947d7]"
    model = "faetastic_Version2.safetensors [3c7a4c79e1]"
    
    project_name = "meshes"
    prompt = "dancer cinematic exciting dramatic lighting highly detailed and intricate"
    neg_prompt = "monochrome"
    batch_size = 1
    seed = 3873480359
    steps = 25
    denoise = 0.5
    guidance = 7

    # defaults
    webui_server_url = 'http://127.0.0.1:7860'
    root_dir = os.path.join("D:\\", "hcde496")
    project_dir = os.path.join(root_dir, "Projects", project_name)
    images_in = os.path.join(project_dir, "images", "input")
    pose_dir = os.path.join(project_dir, "images", "pose")

    #prepare output
    images_out = os.path.join(project_dir, "images", "output", )
    session_name = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_path = os.path.join(images_out, session_name )
    os.mkdir(session_path)

    # load image list
    images_list = get_image_list(images_in)
    pose_list = get_image_list(pose_dir)
    project_len = len(images_list)

    blend_image = encode_file_to_base64(images_list[0])
    
    # image loop
    for filenum in range(10): 
        print(filenum, " of ", project_len)
        image_source = encode_file_to_base64(images_list[filenum])
        pose_source = encode_file_to_base64(pose_list[filenum])

        # payload = img2img_payload(model, image_source, pose_source, prompt, neg_prompt, seed, steps, denoise, guidance)
        payload = text2img_payload("happy dancing elf", seed)
        payload.update({ "override_settings": {"sd_model_checkpoint": model}})
        payload.update({ "alwayson_scripts": {"ControlNet": { "args": [{"enabled": True, "input_image": pose_source,"model": "control_v11p_sd15_openpose [cab727d4]", "module": "none"}]} }})
        # response = call_img2img_api(**payload)

        response = call_txt2img_api(**payload)
        images = response.get('images')
        image_out_path = img_out_path(filenum)

        # show_img(pose_source)

        for index, image in enumerate(response.get('images')):
            decode_and_save_base64(image, image_out_path)
            show_img(image)

            # seed_img_enc = image



        # denoise = denoise_incr(filenum, len(images_list))
        # print(denoise)

        # blend_enc = blend_images(seed_img_enc, image_in_enc, blend = 0.15)
        # show_img(pose_img_enc)
        # add exponential random for blend? or based on modulo