import csv

file1 = csv.reader(open('master.csv', 'r')) #Master file whioh contains larger set of data
all = list(file1)

file2 = csv.reader(open('slave.csv', 'r'))
omit = list(file2)
matched_count = 0
unmatched_count = 0
with open('result_of_comparison.csv', 'w', newline='') as csvo:
    om = csv.writer(csvo)

    for pr in all:

        if pr not in omit:
            print((pr))
            om.writerow(pr)
            unmatched_count = unmatched_count + 1
        else:
            matched_count = matched_count + 1
    for pr in omit:

        if pr not in all:
            print(str(pr))

            # print(str(pr) + " : Not Matched/Present in/from CDK")
            om.writerow(pr)
            unmatched_count = unmatched_count + 1
        else:
            matched_count = matched_count + 1

    print("Total Matched Records = {}".format(matched_count))
    print("Total Unmatched Records = {}".format(unmatched_count))
