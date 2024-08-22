import requests

# Replace with the ngrok URL generated in Colab
url = "your-ngrok-link/predict"

data = {
    'input': 'hi',
    'model':'llama3:8b'
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print("Failed to get a response:", response.status_code)