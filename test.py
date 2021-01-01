#!/usr/bin/env python3

import json

print("hello")
temp_list = []

with open('article.json') as f:
    data = json.load(f)

for d in data[0]:
    print(d)

for d in data[0]:
    temp_list.append(d)

print(temp_list)

for i in temp_list:
    print(data[0][i])

