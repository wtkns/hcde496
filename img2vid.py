from datetime import datetime
import urllib.request
import base64
import json
import time
import os
import subprocess
from PIL import Image
from io import BytesIO

def init_environment( api_url, proj_name, root):
    global webui_server_url, project_name, model_checkpoint, session_seed, root_dir, project_dir, images_in_dir, pose_dir
    global session_path
    global images_list
    global pose_list

    webui_server_url = api_url
    project_name = proj_name
    model_checkpoint = get_model_list()
    session_seed = datetime.now().strftime("%H%M%S")
    root_dir = os.path.join("D:\\", root)
    project_dir = os.path.join(root_dir, "Projects", project_name)
    images_in_dir = os.path.join(project_dir, "images", "input")
    pose_dir = os.path.join(root_dir, "Projects", project_name, "images", "pose")

    #prepare output
    session_path = os.path.join(project_dir, "images", "output", session_seed )
    os.mkdir(session_path)

    # load image list
    images_list = get_image_list(images_in_dir)
    pose_list = get_image_list(pose_dir)

    return 

def get_image_list(image_dir):
    return [os.path.join(image_dir, image_name) for image_name in os.listdir(image_dir)] 

def get_model_list():
    response = call_api_get("sdapi/v1/sd-models")
    model_list = []
    for index, model in enumerate(response):
        model_list.append(model.get('title'))
    return model_list

def encode_file_to_base64(path):
    with open(path, 'rb') as file:
        newsize = (1024, 512)
        image = Image.open(file).resize(newsize)
        return image_binary_to_base64(image)
        # return base64.b64encode(file.read()).decode('utf-8')

def decode_and_write_base64(base64_str, save_path):
    write_file(decode_base64(base64_str), save_path)
    
def decode_base64(base64_str):
    return base64.b64decode(base64_str)

def write_file(file_data, save_path):
    with open(save_path, "wb") as file:
        file.write(file_data)

def call_api_get(api_endpoint):
    request = urllib.request.Request(
        f'{webui_server_url}/{api_endpoint}',
        headers={'Content-Type': 'application/json'}
    )
    response = urllib.request.urlopen(request)
    return json.loads(response.read().decode('utf-8'))

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
    # parameters = openpose_payload(parameters, pose_image_base64)
    return parameters

def txt2img_payload(parameters, model_checkpoint, payload_image_base64, pose_image_base64):
    parameters = override_payload(parameters, model_checkpoint)
    parameters = openpose_payload(parameters, pose_image_base64)
    return parameters

def show_image(image_enc):
    Image.open(BytesIO(base64.b64decode(image_enc))).show()
    return 1

def image_out_path(filenum):
    return os.path.join(session_path, f'image-{filenum:03d}.png')

def decode_image(image):
    return Image.open(BytesIO(base64.b64decode(image)))

def image_binary_to_base64(image_binary):
    binary_file_obj = BytesIO()
    image_binary.save(binary_file_obj, format="JPEG")
    file_binary = binary_file_obj.getvalue()  # blend_bytes: image in binary format.
    return base64.b64encode(file_binary).decode('utf-8')

def blend_images_base64(image_one_base64, image_two_base64, blend = 0.5):
    # If alpha is 0.0, a copy of the first image is returned. If alpha is 1.0, a copy of the second image is returned. 
    image_one_binary = decode_image(image_one_base64)
    image_two_binary = decode_image(image_two_base64)
    img_blend_binary = Image.blend(image_one_binary, image_two_binary, blend)
    return image_binary_to_base64(img_blend_binary)




if __name__ == '__main__':
    
    init_environment( 'http://127.0.0.1:7860', "liquid", "HCDE496")    # set system defaults

    parameters = {
        "prompt": "plastic candy crushed sugar glowing shining sparkling sequins mirrorball dancing in an infinite crystal mirror ballroom of glittering diamonds and glass refracting prismatic diachroic lights and mirrors forever dreamlike photo highly detailed cinematic",
        "negative_prompt": "nude human man woman child girl boy anime animation drawing pixel bit",
        "seed": session_seed,
        "sampler_name": "DPM++ 2M Karras",
        "steps": 40,
        "width": 1024,
        "height": 512,
        "denoising_strength": 0.5,
        "n_iter": 1,
        "batch_size": 1,
        "cfg_scale": 7,
        "batch_size": 1,
    }
    
    seedlength = 10


    blank_image_base64 = encode_file_to_base64("D:\\hcde496\\blank1024x512.png")

    # use image
    # seed_image_base64 = encode_file_to_base64(images_list[0])

    # or use blank
    seed_image_base64 = blank_image_base64
    
    # image loop
    for filenum in range(len(images_list)): 
        print(filenum, " of ", len(images_list))
        
        # # use pose source?
        pose_source_base64 = encode_file_to_base64(pose_list[filenum])
        
        # GET WEIRD
        # pose2_source_base64 = encode_file_to_base64(pose_list[filenum + 30])
        # pose_source_base64 = blend_images_base64(pose_source_base64, pose2_source_base64, 0.5)


        # use img source?
        guide_image_base64 = encode_file_to_base64(images_list[filenum])
        seed_image_base64 = blend_images_base64(guide_image_base64, seed_image_base64, 0.95)
       
        payload = img2img_payload(parameters, model_checkpoint[1], guide_image_base64, pose_source_base64)

        response = call_img2img_api(**payload)
        images_output = response.get('images')

        for index, image_out_base64 in enumerate(images_output):
            if index == 0:
                decode_and_write_base64(image_out_base64, image_out_path(filenum))
                seed_image_base64 = blend_images_base64(image_out_base64, seed_image_base64, 0.25)

                # dim_guide_base64 = blend_images_base64(blank_image_base64, guide_image_base64, 0.25)
                # seed_image_base64 = blend_images_base64(image_out_base64, dim_guide_base64, 0.5)
                # seed_image_base64 = blend_images_base64(seed_image_base64, blank_image_base64, 0.25)
                # show_image(seed_image_base64)

        dstrength = 0.5 # (0.5 - (0.15/seedlength)*(filenum % seedlength))
        print(dstrength)
        parameters.update({"denoising_strength": dstrength})


        if filenum % seedlength == 0:
            parameters.update({"seed": datetime.now().strftime("%H%M%S")})
