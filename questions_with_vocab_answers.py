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
        Make a word bank for the following words: "admire, adopt, focus, stepmother". 
        Write instructions asking the students to write an answer for each of the questions. 
        Tell the students that they should use the words from the word bank in their answers.
        Write an open-ended question for each word in the word bank. 
        The questions should not contain the words from the word bank. 
        The questions should be designed so that answers can use the words from the word bank.
        The questions should be at the CEFR A2 level.
        Do not provide answers to the questions.
        ''', 
    temperature=.5, 
    max_tokens=2000
    )

response_text = response.choices[0]['text']

print(response_text)