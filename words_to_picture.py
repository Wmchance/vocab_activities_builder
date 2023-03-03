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
        Make a word bank for the following words: "{word_str}". 
        Write instructions asking students to draw a picture for each of the words in the word bank.
        Write instructions asking the students to write a sentence to accompany each of the pictures they have drawn.
        Create an area for student to complete the above tasks.
        Make the instructions appropriate for CEFR A2 level students.
        ''', 
    temperature=.5, 
    max_tokens=2000
    )

response_text = response.choices[0]['text']

print(response_text)