# Chat-Bot-With-Fine-Tuning

## About
This project provides a walkthrough of how to fine-tune a GPT model, specifically the text-babbage model, using a custom dataset. The objective is to create a chatbot capable of answering questions based on a given prompt. By leveraging the power of the OpenAI API, this project enables users to train their own conversational models and interact with them programmatically.

## Features
- Fine-tuning of GPT models: This project provides the necessary steps to fine-tune a GPT model using a custom dataset.
- Dataset formatting: The project guides you on how to format your dataset into a suitable structure for fine-tuning.
- Cost estimation: Estimate the number of tokens in your dataset to understand the associated cost of using the OpenAI API.
- Command-line interface: Utilize the OpenAI CLI tool to initiate the fine-tuning process and manage your training jobs.
- OpenAI API integration: Interact with the fine-tuned model using the OpenAI API to generate responses from the chatbot.

## Installation
1. Clone the repository.
2. Install the required dependencies.

## Data
The project uses a dataset sourced from Kaggle, which contains a collection of questions and their corresponding answers from StackOverflow.

## Fine-Tuning Formatting
To prepare the dataset for fine-tuning, it needs to be formatted in a specific structure. Each data instance consists of a prompt (question) and an expected completion (answer). This format is crucial for dialogue-based training. The dataset is converted into a list of dictionaries, where each dictionary contains a prompt-completion pair.

## Price Estimation
Before proceeding with fine-tuning, it's important to estimate the number of tokens in the dataset. Tokens are the units of text that the model processes. The "tiktoken" library is used to estimate the token count. The number of tokens is essential for understanding the associated cost of using the OpenAI API.

## Command Line for Fine-Tuning
The fine-tuning process is initiated using the OpenAI CLI tool via the terminal or command line. The tool needs to be installed beforehand. Once installed, a command is executed to start the fine-tuning process by specifying the training data file and the target model.

## OpenAI API
To interact with the fine-tuned model, you need to set up your OpenAI API Key as an environment variable. This ensures the API Key is not directly present in the code for security reasons. Once the API Key is set, you can make API calls to generate responses from the fine-tuned model. The API call includes parameters such as the model, prompt, maximum token limit, and temperature.

## Usage
1. Prepare your dataset: Ensure you have a dataset consisting of question-answer pairs, preferably in a CSV format.
2. Format the dataset: Convert your dataset into a suitable format for fine-tuning using the provided instructions.
3. Estimate token count: Utilize the "tiktoken" library to estimate the token count in your dataset and understand the associated cost.
4. Fine-tuning via Command Line: Install the OpenAI CLI tool and follow the instructions in the README to initiate the fine-tuning process using your training data.
5. Set up OpenAI API: Set your OpenAI API Key as an environment variable to interact with the fine-tuned model via the OpenAI API.
6. Interact with the model: Use the provided code snippet in the README to generate responses from the fine-tuned model based on a given prompt.

That's the high-level overview of the project. By following the instructions provided in the README, you can fine-tune your own GPT model using a custom dataset and utilize the OpenAI API to generate responses from the chatbot model. Enjoy building your AI

-powered conversational system!
