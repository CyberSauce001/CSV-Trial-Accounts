import csv

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

trial()
pwd()
print(pre)
print(pas)

rows = ['Username', 'Password']

from itertools import zip_longest
d = [pre, pas]
export = zip_longest(*d, fillvalue= '')
with open('Trial_Account.csv', mode='w', encoding="ISO-8859-1", newline='') as myFile:
    myFile = csv.writer(myFile)
    #write into row
    myFile.writerow(rows)
    #write into column
    myFile.writerows(export)
#myFile.close() pyCharm does not like this line
