
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

## Define csv file name either budget_data_1.csv or budget_data_2.csv
## Also change the filename of the output file 

csvpath=os.path.join('PyBank','budget_data_2.csv')

### Definning variables, dictionaries and lists
total_revenue = 0
total_months = 0
past_revenue =0
revenue_change_list = []
tracking_month=[]
Rev_change_month={}
month_revenue = {}

## Open csvpath
with open(csvpath,newline='') as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=',')

# Skip 1st row header
    next(csvreader)

 # Assigning month_revenue 
    month_revenue = {row[0]:row[1] for row in csvreader}
   
   
# for calculation of revenue change
for month, rev_value in month_revenue.items():
    revenue = int(rev_value)
    total_revenue += revenue
    total_months += 1
    revenue_change_list.append(revenue - past_revenue)
    tracking_month.append(month)
    past_revenue = revenue

# Calculating Average Revenue Change for month over month
Average_revenue_change = round(float(sum(revenue_change_list))/(len(revenue_change_list)))

# printing out end result for test
#print(total_revenue)
#print(total_months)
#print(Average_revenue_change)
#print(revenue_change_list)
#print(tracking_month)
#print(len(revenue_change_list))
#print(len(tracking_month))

Rev_change_month=dict(zip(tracking_month,revenue_change_list))

#print(Rev_change_month)


     
### Specifying the file to output to
#output_path = os.path.join('output','budget_1_analysis.csv')

## Open the file using the write mode.

with open('budget_data_2_analysis.csv','w',newline='') as csvfile:

    # Initialize csv writer
    csvwriter = csv.writer(csvfile,delimiter=',')

    #Write the 1st row
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(['Total Months:' + str(total_months)])
    csvwriter.writerow(['Total Revenue:'+ str(total_revenue)])
    csvwriter.writerow(['Average Revenue Change:'+ str(Average_revenue_change)])
    csvwriter.writerow(['Greatest Increase in Revenue is in '+ str(max(Rev_change_month))+':(' +str(max(Rev_change_month.values()))+')'])
    csvwriter.writerow(['Greatest Decrease in Revenue is in '+ str(min(Rev_change_month))+ ':('+str(min(Rev_change_month.values()))+')'])



