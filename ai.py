#!/data/data/com.termux/files/usr/bin/python3
import openai
import os
import sys

# Use the openai API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Prompt the user for input
prompt = sys.stdin.read()

# Send the prompt to the "text-davinci-03" model
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the model's response
print(response["choices"][0]["text"])
