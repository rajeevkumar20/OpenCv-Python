import csv, os

file = "Data"+os.sep+"data.csv"
row_data = []
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        row_data.append(row)
    csvfile.close()
    print(row_data)
