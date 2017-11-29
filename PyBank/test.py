import os
import csv

my_dict= {}
temp_list= []


with open('budget_data_1.csv',newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    next(csvreader) 

    my_dict = [ row[1] for row in csvreader]
    
    print(my_dict)
    print(len(my_dict))
    

i=1
for i in range(len(my_dict)):
   temp = int(my_dict[i]) - int(my_dict[i-1])
   print(i)
   print(temp)     
   temp_list.append(temp)

print (temp_list)



