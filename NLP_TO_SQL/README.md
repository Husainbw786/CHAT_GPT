# Natural Language Processing To Structured Query Language (NLP->SQL)

Welcome to the "From Natural Language Processing to Structured Query Language" project! This initiative aims to showcase the seamless transition from natural language prompts to structured query language (SQL) queries using OpenAI's GPT-3 model. By bridging the gap between natural language understanding and data querying, this project empowers you to effortlessly derive insights from your data.

## Libraries Used

This project harnesses the capabilities of several vital libraries:

- **openai**: This library facilitates interaction with the OpenAI API, allowing for GPT-3 model utilization.
- **pandas**: Pandas serves as the foundation for data manipulation and analysis, providing efficient tabular data handling.
- **sqlalchemy**: SQLAlchemy streamlines SQL database interactions, simplifying the process of managing connections and queries.

## Features

- **Data Querying**: This project enables data querying using both Pandas and SQL syntax, offering the flexibility to retrieve specific information from sales data.
- **Natural Language Interaction**: Through the OpenAI API, you can engage with the GPT-3 model using natural language prompts, eliminating the need for complex SQL query composition.
- **Dynamic Prompt Generation**: The project dynamically generates prompts for GPT-3 based on table structures and user-provided natural language requests.

## Usage

1. **Setting Up Environment**: Install the required libraries using the provided pip command.

2. **Data Loading**: Utilize Pandas to read and manipulate sales data from "sales_data_sample.csv".

3. **Querying Data**: Employ both Pandas and SQL syntax to query the data and extract meaningful insights.

4. **Natural Language Interaction**: Use GPT-3 to generate SQL queries from natural language prompts. Securely access the OpenAI API by setting up your API key as an environment variable.

5. **Dynamic Prompt Generation**: Combine table structure prompts and user-input natural language requests to create prompts for GPT-3.

6. **OpenAI API Call**: Communicate with the GPT-3 model via the OpenAI API and retrieve generated SQL queries.

7. **Executing the Query**: Execute the generated query on the database to obtain desired results.

## Examples

Consider the scenario where you want to determine total sales for each quarter of the year:

1. Employ Pandas to group data by quarter and calculate the sum of sales.

2. Alternatively, utilize GPT-3 to generate an SQL query by prompting, "Provide the total sales for each quarter."

## Acknowledgment

This project acknowledges the transformative capabilities of OpenAI's GPT-3 model, which excels in language understanding and generation. We also recognize the significance of the Pandas library for efficient data manipulation and analysis, as well as the versatility of the SQLAlchemy library for simplified database interactions.

Embrace the potential of bridging natural language understanding with structured query language to seamlessly explore, experiment, and gain insights from your data!
