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


## Use Another Model

Expanding the server to support new models is easy! To add another model to the server, modify the register.json to include the endpoint and required fields for the new inference model. The new model will recieve a json containing all required fields, and must respond with a json with the response.









## Internship Quest

Your goal is to implement **a CPU inference server for Llama 2**.

- Llama 2 is a Large Language Model (LLM) developed by Meta AI.
- A DNN inference server accepts HTTP requests whose payload includes inference input data, runs inference on that data, and responds with inference results.
- Although it is common for DNN inference servers to utilize GPUs to run DNN inference, it is also reasonable to run computation on CPUs when the model isn't that large.

## Expectations

- Descriptions are intentionally ambiguous, and you will have to make design choices with appropriate justifications.
- The amount of things you need to know is probably a lot, and nobody would know all of it when given the quest. Therefore, it is important to first figure out what things are at a high-level, figure out the minimal set of things you need to learn in order to build this, and then learn quickly.
- There is no single correct solution; basically you build what you think is reasonable considering the amount of time you have, how much you already know (and how much you need to learn), and how fast you think you can build, because that's how research is typically done.
- I do not expect a perfect solution. It should just run correctly on obvious and common use cases (that you define) and that's enough. Basically a working PoC.
- Feel free to look at projects that are already open-source and take them as a reference, but you'll have to write your own version that you understand and can explain top to bottom.

## Minimum Requirements

- Write "good" code. There is no universal definition of good code, so write code that you think is good.
- Write a "good" README, assuming this is an open source project that you will publicly post on GitHub.
- Write something that you'll be proud of if you open-source it on GitHub. And feel free to actually open-source!
- The server should be able to return a response on the following invocation of `curl` (or a similar command, depending on how you designed the endpoint):
  ```sh
  curl http://localhost:3000/completion -H 'Content-Type: application/json' -d '{"model": "llama2-7b", "message": "Once upon a time"}'
  ```

## Design Questions

The following questions may help you get started on design:

- In the world of "open-source DNN inference servers", what already exists?
- What is the specific use case you would like for project to target?
- What is the feature set? (E.g., Will you support other LLM models? What about text generation options like temperature? Do you want to support streaming?)
- How much performance do you want?
- How much code will you implement yourself vs. take/import from other open-source projects?
