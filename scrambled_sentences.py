import os
import openai
from env_variable import OPENAI_API_KEY
from word_lists import *

# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

# move this to word_list.py & add one for each unit/lesson
word_str = ', '.join(l2_u1_l1_list)
print(word_str)

response = openai.Completion.create(
    model="text-davinci-003", 
    prompt=f'''
        Generate one sentence for each of the following words: "{word_str}". 
        The sentences should be appropriate for CEFR A2 level students.
        Write the sentences in a numbered bullet format.
        Write instructions telling students to rewrite the sentences in the correct order.
        ''', 
    temperature=.3, 
    max_tokens=2000
    )

response_text = response.choices[0]['text']

# add spaces blanks to text manually so that ChatGPT is relied on for this part
# add a word bank

print(response_text)