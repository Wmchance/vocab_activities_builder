import tkinter

from env_variable import OPENAI_API_KEY
from word_lists import *
from fill_in_the_blank_individual_sentences import *

if __name__ == '__main__':
    
    csv_from_book = 'SYM_2_WordList.csv'
    generate_word_lists(csv_from_book)

    # activity = fill_in_the_blank_individual_sentences(OPENAI_API_KEY, (', '.join(l2_u1_l1_list)))
    print(l2_u1_l4_list)