import helper as hp
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("k1.jpg")

if isinstance(output, list):
    hp.prettier(output)
else:
    print("Raw Output:", output)
