import json
import requests
import io
import base64
import time
from PIL import Image

url = "http://127.0.0.1:7860"
output = "D:\\hcde496\\sd_api\\output\\test\\"
timestr = time.strftime("%Y%m%d-%H%M%S")

payload = {
    "prompt": "puppy dog playing with random object",
    "steps": 5
}

response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

r = response.json()

image = Image.open(io.BytesIO(base64.b64decode(r['images'][0])))
image.save(output + 'output-' + timestr + '.png')