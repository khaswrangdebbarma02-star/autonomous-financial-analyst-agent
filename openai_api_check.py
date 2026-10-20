
import os
from dotenv import load_dotenv
from openai import OpenAI

print("Starting OpenAI API test...")

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Check your .env file.")

print("API key found. Sending request...")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5.5",
    input="Explain what a stock market is in two simple sentences."
)

print("\nOpenAI API Response:\n")
print(response.output_text)
