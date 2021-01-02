#!/usr/bin/env python3

import json
import re
import time

with open('article.json') as f:
    data = json.load(f)

title = data[0]['title']
authors = []

for i in data[0]['author']:
    full_name = "[" + i['given'] + ' ' + i['family'] + "]"
    authors.append(full_name)

source = data[0]['source']
url = data[0]['URL']

date = data[0]['issued']['date-parts'][0]

formated_date = str(date[1]) + " " + str(date[2]) + " " + str(date[0])

def get_filename():
    temp_filename = title.replace(",", "")
    return re.sub("’","",temp_filename)

filename = get_filename()
print(title)
print(filename)

for i in authors:
    print(i)

print()
print(url)
print(formated_date)


while True:
    try:
        with open('%s.md' % filename, 'w') as file:
            file.write(title + "\n")
            file.write(str(authors) + "\n")
            file.write(url + "\n")
            file.write(formated_date + "\n")
            file.write("[" + source + "]" + "\n")
            file.write("new test")
        break

    except (FileNotFoundError, OSError):
        print("OS Error or File Not Found Error")
        filename = time.strftime("%Y%m%d", time.gmtime()) + "_" + str(authors[1][1:-1])
        with open('%s.md' % filename, 'w') as file:
            file.write("new name test")
        break


# def write_to_file():
#     with open('%s.md' % filename, 'w') as file:
#             file.write(title)
#             file.write(authors)
#             file.write(url)
#             file.write(formated_date)
#             file.write("[" + source + "]")
#             file.write("new test")
