import csv

my_variable = input('Enter a string to test this script: ')

with open('TestCSV.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(my_variable)
f.close()
print(my_variable)
