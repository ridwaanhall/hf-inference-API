import os
from dotenv import load_dotenv
import requests

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/ridwaanhall/sentimen"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

input_text = input("Masukkan kalimat (default): ") or "aku cinta kamu, tetapi kamu tolak."

output = query({
    "inputs": input_text,
})

for item in output[0]:
    label = item['label']
    score = item['score']
    print(f"{label}: {score}")