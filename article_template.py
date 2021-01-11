#!/usr/bin/env python3

import json
import re
import time
import sys

## Takes one argument (json file) and converts JSON data into usable data object
## Needs Help menue for sys argv and exectpion if no argument is made
json_file = sys.argv[1]

print(json_file)
with open(json_file) as f:
    new_data = json.load(f)
    print(new_data)
with open('article.json') as f:
    data = json.load(f)

## Parse Values from JSON file into Variables
title = data[0]['title']
authors = []

for i in data[0]['author']:
    full_name = "[" + i['given'] + ' ' + i['family'] + "]"
    authors.append(full_name)

source = data[0]['source']
url = data[0]['URL']

date = data[0]['issued']['date-parts'][0]

formated_date = str(date[1]) + " " + str(date[2]) + " " + str(date[0])

## Funtion thats returns file name
## Need to removea all values that are not ASCII or valid values for a filename
def get_filename():
    temp_filename = title.replace(",", "")
    return re.sub("’","",temp_filename)

filename = get_filename()

## Wries to File
while True:
    try:
        with open('%s.md' % filename, 'w') as file:
            file.write(title + "\n")
            for i in authors:
                file.write(str(i) + "\n")
            file.write(url + "\n")
            file.write(formated_date + "\n")
            file.write("[" + source + "]" + "\n")
            file.write("new test")
    except (FileNotFoundError, OSError):
        print("OS Error or File Not Found Error")
        filename = time.strftime("%Y%m%d", time.gmtime()) + "_" + str(authors[1][1:-1])
        continue

# def write_to_file():
#     with open('%s.md' % filename, 'w') as file:
#             file.write(title)
#             file.write(authors)
#             file.write(url)
#             file.write(formated_date)
#             file.write("[" + source + "]")
#             file.write("new test")
