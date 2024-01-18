from datetime import datetime
import urllib.request
import base64
import json
import time
import os

prompt = "colorful dancer elaborate costume"
negative_prompt = "monochrome"
imgfileDir = "G:\\Shared drives\\080 - Code\\Python\\hcde496\\ffmpeg\\tophat\\input\\"
webui_server_url = 'http://127.0.0.1:7860'
out_dir = "G:\\Shared drives\\080 - Code\\Python\\hcde496\\ffmpeg\\tophat\\"
out_dir_i2i = os.path.join(out_dir, 'output')

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

def call_img2img_api(filenum, **payload):
    response = call_api('sdapi/v1/img2img', **payload)
    for index, image in enumerate(response.get('images')):
        save_path = os.path.join(out_dir_i2i, f'img2img{filenum:03d}.png')
        decode_and_save_base64(image, save_path)


if __name__ == '__main__':

    img_dir_list = os.listdir(imgfileDir)

    for filenum in range(len(img_dir_list)):
        file = img_dir_list[filenum]
        imageFile = imgfileDir + file
       
        print(imageFile)

        init_images = [
             encode_file_to_base64(imageFile),
        ]
        
        denoise = filenum * (0.75/len(img_dir_list))
        print(denoise)
                
        batch_size = 1
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



# # Importing Image module from PIL package 
# from PIL import Image
 
# # creating a image1 object and convert it to mode 'P'
# im1 = Image.open(r"C:\Users\sadow984\Desktop\i2.PNG").convert('L')
 
# # creating a image2 object and convert it to mode 'P'
# im2 = Image.open(r"C:\Users\sadow984\Desktop\c2.PNG").convert('L')
 
# # alpha is 0.0, a copy of the first image is returned
# im3 = Image.blend(im1, im2, 0.0)
 
# # to show specified image 
# im3.show()