import json
import csv

json_file = open("data.json")
data = json.load(json_file)
li = []
for li in data:
    length = len(li)

for x in range(0, length):
    rec = data[x]

    firstJson = list(rec.values())

with open('extracted_id.csv', 'w', newline='') as csvo:
    om = csv.writer(csvo)
    for distro in data:
        print(distro['id'])
        om.writerow([distro['id']])
