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

def encode_file_to_base64(path):
    with open(path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

def decode_and_write_base64(base64_str, save_path):
    write_file(decode_base64(base64_str), save_path)
    
def decode_base64(base64_str):
    return base64.b64decode(base64_str)

def write_file(file_data, save_path):
    with open(save_path, "wb") as file:
        file.write(file_data)

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

def openpose_payload(parameters, pose_image_base64):
    parameters.update({ "alwayson_scripts": {"ControlNet": { "args": [{
        "enabled": True,
        "control_mode": "ControlNet is more important",
        "input_image": pose_image_base64,
        "model": "control_v11p_sd15_openpose [cab727d4]",
        "module": "none",
        "weight": 2
    }]} }})
    return parameters

def override_payload(parameters, model_checkpoint = "cyberrealistic_v41BackToBasics.safetensors [925bd947d7]"):
    parameters.update({ "override_settings": {"sd_model_checkpoint": model_checkpoint}})
    return parameters

def image_source_payload(parameters, payload_image_base64):
    parameters.update({ "init_images": [payload_image_base64]})
    return parameters

def img2img_payload(parameters, model_checkpoint, payload_image_base64, pose_image_base64):
    parameters = override_payload(parameters, model_checkpoint)
    parameters = image_source_payload(parameters, payload_image_base64)
    parameters = openpose_payload(parameters, pose_image_base64)
    return parameters

def txt2img_payload(parameters, model_checkpoint, payload_image_base64, pose_image_base64):
    parameters = override_payload(parameters, model_checkpoint)
    parameters = openpose_payload(parameters, pose_image_base64)
    return parameters

def show_img(image_enc):
    Image.open(BytesIO(base64.b64decode(image_enc))).show()
    return 1

def img_out_path(filenum):
    return os.path.join(session_path, f'image-{filenum:03d}.png')

def decode_img(image):
    return Image.open(BytesIO(base64.b64decode(image)))

def image_binary_to_base64(image_binary):
    binary_file_obj = BytesIO()
    image_binary.save(binary_file_obj, format="JPEG")
    file_binary = binary_file_obj.getvalue()  # blend_bytes: image in binary format.
    return base64.b64encode(file_binary).decode('utf-8')

def blend_images_base64(image_one_base64, image_two_base64, blend = 0.5):
    # If alpha is 0.0, a copy of the first image is returned. If alpha is 1.0, a copy of the second image is returned. 
    image_one_binary = decode_img(image_one_base64)
    image_two_binary = decode_img(image_two_base64)
    img_blend_binary = Image.blend(image_one_binary, image_two_binary, blend)
    return image_binary_to_base64(img_blend_binary)

def denoise_incr(incr_num, total):
    return (((incr_num +1) * (0.3/total))+0.45)

if __name__ == '__main__':
    project_name = "meshes"
    model_checkpoint = ["faetastic_Version2.safetensors [3c7a4c79e1]", "cyberrealistic_v41BackToBasics.safetensors [925bd947d7]", "faetastic_Version2.safetensors [3c7a4c79e1]"]
    session_seed = datetime.now().strftime("%H%M%S")
    print(session_seed)

    parameters = {
        "prompt": "dreamlike photo highly detailed cinematic",
        "negative_prompt": "nude anime animation drawing",
        "seed": session_seed,
        "sampler_name": "DPM++ 2M Karras",
        "steps": 20,
        "width": 1024,
        "height": 1024,
        "denoising_strength": 0.5,
        "n_iter": 1,
        "batch_size": 1,
        "cfg_scale": 7,
        "batch_size": 1,
    }
    

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
    blank_image = "D:\\hcde496\\blank1024x1024.png"

    # use image
    # seed_image_base64 = encode_file_to_base64(images_list[0])

    # or use blank
    seed_image_base64 = encode_file_to_base64(blank_image)
    
    # image loop
    for filenum in range(len(images_list)): 
        print(filenum, " of ", len(images_list))
        
        # use pose source?
        pose_source_base64 = encode_file_to_base64(pose_list[filenum])

        # use img source?
        # image_source_base64 = encode_file_to_base64(images_list[filenum])
        # seed_image_base64 = blend_images_base64(image_source_base64, seed_image_base64, 0.75)
        # show_img(seed_image_base64)

        payload = img2img_payload(parameters, model_checkpoint[2], seed_image_base64, pose_source_base64)
        response = call_img2img_api(**payload)
        images_output = response.get('images')

        for index, image_out_base64 in enumerate(images_output):
            if index == 0:
                decode_and_write_base64(image_out_base64, img_out_path(filenum))
                seed_image_base64 = blend_images_base64(image_out_base64, seed_image_base64, 0)

        dstrength = ((0.25/30)*(filenum % 30)) + 0.5
        print
        print(dstrength)
        parameters.update({"denoising_strength": dstrength})


        if filenum % 30 == 0:
            parameters.update({"seed": datetime.now().strftime("%H%M%S")})
