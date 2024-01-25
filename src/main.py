from flask import Flask, request, jsonify, abort
import time
import requests
import json

# load json file
with open("register.json", "r") as f:
    registery = json.load(f)

app = Flask(__name__)

@app.errorhandler(400)
def handle_bad_request(e):
    # Check if the error message is from abort(400) and is a string
    if isinstance(e.description, str):
        return jsonify(error=e.description), 400
    return jsonify(error="Bad request"), 400

def check_welformed(data):
    if 'message' not in data:
        abort(400, "Message not specified")
    if 'model' not in data:
        abort(400, "Model not specified")

    if data['model'] not in registery:
        supported_models = ', '.join(registery.keys())
        abort(400, f"Model {data['model']} not supported yet! Supported models are: {supported_models}.")

    for required in registery[data['model']]['required']:
        if required not in data:
            abort(400, f"Required field {required} not specified")
    

def inference(data):
    check_welformed(data)

    try:
        if data['model'] == "llama2-7b":
            # run model with message and return response
            # response = requests.post("http://llama2:5000/inference", json=data)
            print("sending request to llama2")
            response = requests.post("http://127.0.0.1:5000/inference", json=data)

            if response.status_code == 200:
                return response.json(), 200
            else:
                return {"error": "Failed to get response from llama2 service"}, response.status_code
    except requests.exceptions.ConnectionError:
        return {"error": "Unable to connect to llama2 service"}, 503  # 503 Service Unavailable
    

@app.route('/completion', methods=['POST'])
def completion():
    data = request.json

    response, status_code = inference(data)

    print(f"recieved request to llama2{response}")
    return response, status_code

if __name__ == "__main__":
    app.run(debug=True, port=3000)
