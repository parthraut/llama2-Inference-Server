# llama2-Inference-Server

## Overview
This lightweight inference server accepts HTTP requests whose payload includes inference input data, runs inference on that data using a Large Language Model (LLM), and responds with the inference results. This server currently supports Llama 2, but can be easily expanded to support other models. 

### Using the Server, An Example

Send a request to the server. In this example, we are requesting the llama2-7b model and send the message "What is the meaning of life?":

```sh
  curl http://localhost:3000/completion -H 'Content-Type: application/json' -d '{"model": "llama2-7b", "message": "What is the meaning of life?"}'
```

It will respond with: "The meaning of life is to find purpose and fulfillment through our experiences, relationships, and contributions to society."

```json
{
  "query": "what is the meaning of life?",
  "result": "The meaning of life is to find purpose and fulfillment through our experiences, relationships, and contributions to society.",
  "time": 53.06127202400239
}
```





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
