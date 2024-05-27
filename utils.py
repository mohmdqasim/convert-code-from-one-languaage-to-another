
import os
from dotenv import load_dotenv
from openai import OpenAI
import openai
load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY') # Setting OpenAI API Key 
chat_client = OpenAI()
api_key = os.getenv("OPENAI_API_KEY")

def get_results(input_language, output_language, input_code):
    prompt = f"""
                Convert the following code from {input_language} to {output_language}:

                Input ({input_language}):
                {input_code}

                Output ({output_language}):
                """
    chat_completion = chat_client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-4-turbo",
    )
    return chat_completion.choices[0].message.content