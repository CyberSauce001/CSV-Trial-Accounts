import csv
import os
import openpyxl

prefix = input("Enter a prefix string: ")
number = int(input("Enter a number: "))

pre = []
def trial():
    for i in range(1,number+1):
        pre.append(prefix + str(i))

pas = []
def pwd():
    for i in range(number):
        pas.append("123456")

lic = []
def license():
    for i in range(number):
        lic.append("assigned")
trial()
pwd()
license()
print(pre)
print(pas)

rows = ['Username', 'Password', 'License']

from itertools import zip_longest
d = [pre, pas, lic]
export = zip_longest(*d, fillvalue= '')
with open('trialaccount.csv', mode='w', encoding="ISO-8859-1", newline='') as myFile:
    myFile = csv.writer(myFile)
    #write into row
    myFile.writerow(rows)
    #write into column
    myFile.writerows(export)

wb = openpyxl.Workbook()
ws = wb.active

with open('trialaccount.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        ws.append(row)

wb.save('trialaccount.xlsx')
os.remove('trialaccount.csv')
