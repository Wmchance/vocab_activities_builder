import os
import openai
from env_variable import OPENAI_API_KEY

# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
response_text = response.choices[0]['text']

print(response_text)
