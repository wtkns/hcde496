# https://github.com/Mikubill/sd-webui-controlnet/discussions/673

# https://github.com/Mikubill/sd-webui-controlnet/wiki/API#migrating-from-controlnet2img-to-sdapiv12img
import json
import base64

import requests


def submit_post(url: str, data: dict):
    """
    Submit a POST request to the given URL with the given data.
    """
    return requests.post(url, data=json.dumps(data))


def save_encoded_image(b64_image: str, output_path: str):
    """
    Save the given image to the given output path.
    """
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))

def encode_image(image_path):
  with open(image_path, "rb") as i:
    b64 = base64.b64encode(i.read())
  return b64.decode("utf-8")


if __name__ == '__main__':
#    img2img_url = 'http://127.0.0.1:7861/sdapi/v1/img2img'
    img2img_url = 'http://127.0.0.1:7861/sdapi/v1/txt2img'
    image= encode_image("pose.png")	 
    data =\
	{
	  "prompt":"a sad 70 y.o man sitting at dinning table",
#	  "init_images": [image],	# For img2img
	  "sampler_name": "Euler",
	  "alwayson_scripts": {
	    "controlnet": {
	      "args": [
		{
	  	  "input_image": image,
#		  "module": "depth","model": "control_depth-fp16 [400750f6]"
		  "module": "none","model": "control_openpose-fp16 [9ca67cc5]",
		}
	      ]
	    }
	  }
	}
    response = submit_post(img2img_url, data)
#    print( response.json())
    save_encoded_image(response.json()['images'][0], 'result.png')

