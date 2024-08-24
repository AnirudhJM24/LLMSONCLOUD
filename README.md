# Running LLMs Supported on Ollama via Cloud and Local Machine

This guide walks you through the process of running large language models (LLMs) supported on Ollama using a cloud-based environment and accessing it through your local machine. By the end of this tutorial, you'll be able to deploy an LLM on the cloud and interact with it seamlessly from your local setup.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Create a New Notebook with T4 Runtime](#step-1-create-a-new-notebook-with-t4-runtime)
  - [Step 2: Upload `server.py` to Colab](#step-2-upload-serverpy-to-colab)
  - [Step 3: Copy and Run the `ollamaoncolab.ipynb` Notebook](#step-3-copy-and-run-the-ollamaoncolabipynb-notebook)
  - [Step 4: Execute `client.py` on Your Local Machine](#step-4-execute-clientpy-on-your-local-machine)
- [Future Plans](#future-plans)


## Prerequisites

Before starting, ensure you have the following:
- A Google Colab account.
- A local machine with Python installed.
- Basic knowledge of Python and cloud environments.

## Setup Instructions

### Step 1: Create a New Notebook with T4 Runtime
1. Log in to your Google Colab account.
2. Create a new notebook.
3. In the notebook, navigate to `Runtime` > `Change runtime type`.
4. Select `GPU` and choose the `T4` option for the hardware accelerator.

### Step 2: Upload `server.py` to Colab
1. On your local machine, create a file named `server.py`. This file will serve as the backend for running the LLMs on Colab. I have uploaded an example of what it looks like
2. In your Colab notebook, click on the file icon on the left panel.
3. Upload the `server.py` file to your Colab workspace.

### Step 3: Copy and Run the `ollamaoncolab.ipynb` Notebook
1. Copy the contents of the `ollamaoncolab.ipynb` notebook into the Colab notebook you created in Step 1.
2. Run all the cells in the notebook. This will set up the environment, install necessary dependencies, and start the server.

### Step 4: Execute `client.py` on Your Local Machine
1. On your local machine, create and open a file named `client.py`.
2. Paste the code necessary to connect to the server running on Colab.
3. Modify and Run `client.py` to interact with the LLM hosted on the cloud.

### Creating GGUF models using OLLAMA

1. Download huggingface-cli ```pip install -U "huggingface_hub[cli]"```
2. find the model of your choice and download using the command - ``` huggingface-cli download repo-id filename --local-dir /foldername ```
3. create a new file `makefile` and in it type ``` FROM /foldername/modelfilename
4. Either in the `server.py` or the `ollamaoncolab.py` run the following command - `ollama create modelname -f makefile'
5. list the models - `ollama list` and use the modelname in your client


