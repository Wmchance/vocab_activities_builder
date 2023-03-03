import os
import openai
from env_variable import OPENAI_API_KEY
from word_lists import *

# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

# move this to word_list.py & add one for each unit/lesson
l2_u1_str = ', '.join(level_2_unit1_word_list)
print(l2_u1_str)

response = openai.Completion.create(
    model="text-davinci-003", 
    prompt=f'''
        Write an individual sentence for each of the following words: "admire, adopt, focus, stepmother". 
        The topic of each sentences should be about celebrating or holidays.
        Create a blank space where the above given words should go so that students can fill them in.
        Present the  sentences in a numbered bullet format.
        Make the sentences appropriate for CEFR A2 level students.
        ''', 
    temperature=.5, 
    max_tokens=2000
    )

response_text = response.choices[0]['text']

# add spaces blanks to text manually so that ChatGPT is relied on for this part
# add a word bank

print(response_text)