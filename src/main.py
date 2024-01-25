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
    """Check if the error message is from abort(400) and is a string. Forms
    a json response with the error message and returns it with status code 400."""

    if isinstance(e.description, str):
        return jsonify(error=e.description), 400
    return jsonify(error="Bad request"), 400

def check_welformed(data):
    """Checks if the request is well formed as described in register.json. 
    If not, aborts with status code 400."""

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
    """Sends a POST request to the llama2 service with the data. Returns the response."""

    # check if request is well formed
    check_welformed(data)

    try:
        # send request to llama2 service
        response = requests.post(registery[data['model']]["endpoint"], json=data)
        if response.status_code == 200:
                return response.json(), 200
        else:
            return {"error": "Failed to get response from llama2 service"}, response.status_code
    except requests.exceptions.ConnectionError:
        return {"error": "Unable to connect to llama2 service"}, 503  # 503 Service Unavailable
    

@app.route('/completion', methods=['POST'])
def completion():
    """Handles POST requests to /completion. Returns the response."""

    data = request.json

    # run inference on request
    response, status_code = inference(data)

    # return response, status code to client
    return response, status_code

if __name__ == "__main__":
    app.run(debug=True, port=3000)