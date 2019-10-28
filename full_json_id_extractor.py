import json
import csv

json_file = open("C:/Users/rehman.ashraf/PycharmProjects/JavaInt/venv/file.json")
data = json.load(json_file)
li = []
for li in data:
    length = len(li)

for x in range(0, length):
    rec = data[x]

    firstJson = list(rec.values())

with open('id.csv', 'w', newline='') as csvo:
    om = csv.writer(csvo)
    for distro in data:
        print(distro['id'])
        om.writerow([distro['id']])
