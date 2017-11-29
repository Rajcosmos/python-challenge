## Display total votes
##Count the total votes for each candidate including % of the total votes
##Display the winner


## Assign modules
import os
import csv

######## Declare variables

## count all candidates 
count_candidates=[]
## count unique candidates
candidate=[]
## total votes list
total_votes=[]
## votes count dictionary
votes_count={}

## Read the election data file

with open('election_data_2.csv',newline ='') as csvfile:

    csvreader=csv.reader(csvfile,delimiter=',')

#Skip the 1st row
    next(csvreader)
    
## Create 2 lists, 1 which will capture candidates list (will have repeat lists of candidates) 
# and other list will capture unique # of candidates

    for row in csvreader:
        count_candidates.append(row[2])
        if row[2] not in candidate:
            candidate.append(row[2])

## count total votes
    for x in range(len(candidate)):
          y=count_candidates.count(candidate[x])
          total_votes.append(y)

## We will put 2 lists, candidates_count and candidate in a dictionary votes_count that will give us total votes per candidate
votes_count=dict(zip(candidate,total_votes))

## Debug by printing
print(votes_count)
print(sum(total_votes))
for key,value in votes_count.items():
    print('% votes for'+str(key)+'is'+'%'+str(round((value/sum(total_votes)*100))))

print('winner is '+max(votes_count))

## Save the results in output election_data_*_analysis.csv file

with open('election_data_2_analysis.csv','w',newline='') as csvfile:

    # Initialize csv writer
    csvwriter = csv.writer(csvfile,delimiter=',')

    #Write the rows
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------'])
    csvwriter.writerow(['Total Votes:' + str(sum(total_votes))])
    csvwriter.writerow(['-------------------'])

    ## Iterate to find % votes per candidate
    for key,value in votes_count.items():
        csvwriter.writerow([str(key)+':'+str(round(value/sum(total_votes)*100))+'% ('+str(value)+')'])

    ## Display the winner
    csvwriter.writerow(['-------------------'])
    csvwriter.writerow(['Winner :'+max(votes_count)])
    csvwriter.writerow(['-------------------'])




       
       
        







       
       

