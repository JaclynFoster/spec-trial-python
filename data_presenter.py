import csv

filename = 'Cupcakeinvoices.csv'

# with open(filename, 'r') as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row)

# with open(filename, 'r') as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row[2])

sum_ = 0
with open(filename) as file:
    for line in file:
        columns = line.split(',')
        new = float(columns[4])
        sum_ += new
        print(sum_)