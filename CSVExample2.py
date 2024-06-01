import csv

header = ['Reg Num', 'Name','Section']
data1 = ['2100030312', 'LOKESH', '17']
data2 = [['2100030767', 'SREYA', '17'],
         ['2100030800','HEMANTH','17'],
         ['2100030991','ROOPAK','17']]

with open('studentdata1.csv', 'w') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerow(data1)

    #Writing Multiple Data into the CSV
with open('studentdata1.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(data2)

print("Writing of data successfully done")

    #Reading Multiple Data from CSV
with open('studentdata1.csv', 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    print(header)
    for row in csvreader:
        print(row)

    #Printing Total number of Rows in the file
    print("Total no. of rows: %d" % (csvreader.line_num))

print("Printing of data successfully done")

# with open('studentdata1.csv', 'w') as f:
#     writer = csv.writer(f)
#     for line in f:
#         del line['Section']
#         writer.writerow(line)
# print("Printing of data successfully done123")