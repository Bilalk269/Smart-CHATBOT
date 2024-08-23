import os
from openai import OpenAI

# Make sure to set the environment variable OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "write an essay on penguin",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)
