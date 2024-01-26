# llama2-Inference-Server

## Introduction
The llama2-Inference-Server is a lightweight, versatile inference server designed to streamline the deployment of Large Language Models (LLMs), specifically tailored for Llama 2. It facilitates easy integration of LLMs into various applications by accepting HTTP requests for inference tasks and returning prompt results.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.8 or later
- Docker (for Docker-based setup)
- pip and virtualenv

## Installation

### Local Installation

#### Setting up the Environment
1. Clone the repository to your local machine.
2. Navigate to the project's root directory.

#### Launching the Main Server
1. Change directory to `src/`:
    ```sh
    cd src/
    ```
2. Set up a Python virtual environment and activate it:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Start the server using `run.sh`:
    ```sh
    sh run.sh
    ```

#### Launching the Inference Server
1. Open a new terminal and navigate to the `Llama-2-Open-Source-LLM-CPU-Inference` directory.
2. Repeat the steps to set up a Python virtual environment and activate it.
3. Install dependencies and start the server as described above.

### Docker Installation

#### Configuration
- Adjust the `register.json` file to ensure proper network communication between containers:
    ```json
    {
        "llama2-7b": {
            "endpoint": "http://llama2:5000/inference",
            "required": ["message"]
        }
    }
    ```
- Modify all `run.sh` files to launch services on `0.0.0.0`.

#### Building and Running
1. Build the Docker images:
    ```sh
    docker-compose build
    ```
2. Start the containers:
    ```sh
    docker-compose up
    ```

## Usage
To interact with the server, send a JSON-formatted HTTP request as follows:

```sh
curl http://localhost:3000/completion -H 'Content-Type: application/json' -d '{"model": "llama2-7b", "message": "What is the meaning of life?"}'
```

## Use Another Model

Expanding the server to support new models is easy! To add another model to the server, modify the register.json to include the endpoint and required fields for the new inference model. The new model will recieve a json containing all required fields, and must respond with a json with the response.
