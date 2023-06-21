# Automatic Recipe Generator

![License](https://img.shields.io/badge/license-MIT-blue.svg)

Welcome to the documentation of the Automatic Recipe Generator project! This project aims to simplify the process of generating detailed recipes based on a given list of ingredients. With this tool, you can easily create customized recipes and even obtain an image related to the recipe.

## About

The Automatic Recipe Generator is a Python project that utilizes the OpenAI API to generate detailed recipes. By providing a list of ingredients, the program generates a recipe prompt and assigns a title to the recipe. This tool is especially helpful for cooking enthusiasts, food bloggers, or anyone in need of creative recipe ideas.

## Installation

To use the Automatic Recipe Generator, follow these steps:

1. Install the necessary dependencies:
   - Python (version 3.7 or higher)
   - OpenAI library

2. Clone the project repository:
   ```bash
   $ git clone https://github.com/your_username/your_project.git
   $ cd your_project
   ```

3. Set up the OpenAI API key:
   - Create an account on the OpenAI platform (https://openai.com/).
   - Obtain your API key.
   - Set the OPENAI_API_KEY environment variable with your API key.

4. Install the project dependencies:
   ```bash
   $ pip install -r requirements.txt
   ```

## Usage

To generate a recipe using the Automatic Recipe Generator:

1. Define the list of ingredients you want to use for the recipe.

2. Call the `create_dish_prompt` function, passing the list of ingredients as an argument. This function generates a recipe prompt based on the provided ingredients.

3. Make an API call to the OpenAI API, passing the generated recipe prompt. This generates the recipe.

4. Extract the generated recipe text and the recipe title from the API response.

5. Optionally, you can retrieve an image related to the recipe by making another API call to the OpenAI Image API, using the recipe title as the prompt.

6. Save the retrieved image.

## Features

- **Customization**: Generate recipes based on a list of ingredients you provide.
- **Creativity**: The Automatic Recipe Generator generates detailed recipes with assigned titles, making them unique and appealing.
- **Image Retrieval**: Optionally retrieve an image related to the recipe, enhancing the visual presentation.

## License

This project is licensed under the [MIT License](LICENSE). Please review the license file for more information.

For detailed documentation and examples, please visit the [Project Repository](https://github.com/your_username/your_project).

We appreciate your interest in the Automatic Recipe Generator project. Feel free to provide feedback and suggestions for improvement. Enjoy creating delicious recipes!
