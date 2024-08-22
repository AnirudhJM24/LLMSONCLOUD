import ollama
from flask import Flask, request, jsonify
import subprocess


# modify as per your needs

model_name = "llama3.1"
# subprocess.run(["ollama", "pull", model_name]) - i suggest doing this in the notebook itself
# result = subprocess.run(["ollama", "list"], capture_output=True, text=True) - do this in the notebook it's better


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Here, you'd interact with Ollama to get predictions
    # Replace this with the appropriate code to generate predictions using Ollama
    result = ollama.chat(
    model=data['model'],
    messages=[{'role': 'user', 'content': data['input']}]
)
    return jsonify(result)

print('running your server---------------------------------')
app.run(host='0.0.0.0', port=5000)