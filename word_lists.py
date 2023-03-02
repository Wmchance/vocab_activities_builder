import csv

level_2_unit1_word_list = []
level_2_unit2_word_list = []
level_2_unit3_word_list = []
level_2_unit4_word_list = []
level_2_unit5_word_list = []
level_2_unit6_word_list = []
level_2_unit7_word_list = []
level_2_unit8_word_list = []
level_2_unit9_word_list = []
level_2_unit10_word_list = []
level_2_unit11_word_list = []
level_2_unit12_word_list = []

csv_from_book = 'SYM_2_WordList.csv'

def generate_word_lists(csv_from_book):
    with open(csv_from_book) as level_2_word_list_csv:
        all_word_list = csv.reader(level_2_word_list_csv)
        next(all_word_list) #skips header row
        for row in all_word_list:
            if row[0] == '1':
                level_2_unit1_word_list.append(row[1])
            elif row[0] == '2':
                level_2_unit2_word_list.append(row[1])
            elif row[0] == '3':
                level_2_unit3_word_list.append(row[1])
            elif row[0] == '4':
                level_2_unit4_word_list.append(row[1])
            elif row[0] == '5':
                level_2_unit5_word_list.append(row[1])
            elif row[0] == '6':
                level_2_unit6_word_list.append(row[1])
            elif row[0] == '7':
                level_2_unit7_word_list.append(row[1])
            elif row[0] == '8':
                level_2_unit8_word_list.append(row[1])
            elif row[0] == '9':
                level_2_unit9_word_list.append(row[1])
            elif row[0] == '10':
                level_2_unit10_word_list.append(row[1])
            elif row[0] == '11':
                level_2_unit11_word_list.append(row[1])
            elif row[0] == '12':
                level_2_unit12_word_list.append(row[1])
        


generate_word_lists(csv_from_book)
print(level_2_unit4_word_list)