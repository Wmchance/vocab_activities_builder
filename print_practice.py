import csv
with open('SYM_2_WordList.csv') as level_2_word_list_csv:
    all_word_list = csv.reader(level_2_word_list_csv)
    next(all_word_list) #skips header row
    for row in all_word_list:
        print(row[1])