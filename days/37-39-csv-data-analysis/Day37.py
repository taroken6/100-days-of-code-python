import os
import csv

FILENAME = 'suicide_rates.csv'

csvfile = open(FILENAME, encoding='utf-8-sig')
reader = csv.DictReader(csvfile)

# Select category
category_list = sorted(reader.fieldnames)
for i, category in enumerate(category_list):
    print(f'{i}: {category}')
category_input = -1
while category_input < 0 or category_input >= len(category_list):
    try:
        category_input = int(input('Please select a valid category number: '))
    except ValueError:
        print('Must be an integer')
category = category_list[category_input]
os.system('cls')

# Category options
subcategory_list = sorted(list(set(row[category] for row in reader)))
for i, subcategory in enumerate(subcategory_list):
    print(f'{i}: {subcategory}')
subcategory_input = -1
while subcategory_input < 0 or subcategory_input >= len(subcategory_list):
    try:
        subcategory_input = int(input('Please select a valid subcategory '))
    except ValueError:
        print('Must be an integer')
subcategory = subcategory_list[subcategory_input]

# Get rows that fit selection
csvfile.seek(0)
selections = [row for row in reader if row[category] == subcategory]
selections.sort(key=lambda x: int(x['suicides_no']), reverse=True)
for selection in selections[:5]:
    print(f'{selection["country-year"]}: {selection["suicides_no"]} suicides from a population of {selection["population"]}')
