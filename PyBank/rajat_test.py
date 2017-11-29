
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The total amount of revenue gained over the entire period
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period
#As an example, your analysis should look similar to the one below:
#Financial Analysis
#----------------------------
#Total Months: 25
#Total Revenue: $1241412
#Average Revenue Change: $216825
#Greatest Increase in Revenue: Sep-16 ($815531)
#Greatest Decrease in Revenue: Aug-12 ($-652794)

## Import Modules - 

import os
import csv


### Definning variables, dictionaries and lists
total_revenue = 0
total_months = 0
my_dict = {}
revenue_change_list = []
#for iteration
i=1 

## Open a budget_data_1.csv file
with open('budget_data_1.csv',newline='') as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=',')

# Skip 1st row header
    next(csvreader)
# Assign Dictionary 
    my_dict = [ row[1] for row in csvreader]

# for calculation
for i in range(len(my_dict)):
    total_revenue += int(my_dict[i])
    total_months += 1
    revenue_change = int(my_dict[i]) - int(my_dict[i-1])
    print(i)
    print(revenue_change)     
    revenue_change_list.append(revenue_change)

# printing end result
print(total_revenue)
print(total_months)
print(revenue_change_list)
x = float(sum(revenue_change_list))/(total_months)
print (x)

print(str(max(my_dict)))
print(str(min(my_dict)))
     
### Specifying the file to output to
#output_path = os.path.join('output','budget_1_analysis.csv')

## Open the file using the write mode.
with open('budget_data_1_analysis.csv','w',newline='') as csvfile:

    # Initialize csv writer
    csvwriter = csv.writer(csvfile,delimiter=',')

    #Write the 1st row
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(['Total Months:' ,total_months])
    csvwriter.writerow(['Total Revenue:',total_revenue])
    csvwriter.writerow(['Average Revenue Change:',x])
    csvwriter.writerow(['Greatest Increase in Revenue:',max(my_dict)])
    csvwriter.writerow(['Greatest Decrease in Revenue:',min(my_dict)])


