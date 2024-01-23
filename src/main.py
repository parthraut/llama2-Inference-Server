from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/completion', methods=['POST'])
def completion():
    data = request.json
    model = data.get('model')
    message = data.get('message')

    response = generate_response(model, message)

    return response

if __name__ == "__main__":
    app.run(debug=True, port=3000)


def generate_response(model, message):
    if model == "llama2-7b":
        # run model with message and return response
        return "Hello, World!"