#import csv
import csv
#read through csv file
with open ("PyPoll/Resources/election_data.csv") as csvfile:
    reader = csv.reader(csvfile)
    #set beginning values
    vote_count = 0
    list_of_candidates = {}
    #skip headers
    next (reader)
    #for loop for each rox in csv file
    for row in reader:
        #add to vote count
        vote_count = vote_count + 1
        if row[2] in list_of_candidates:
            candidate = row[2]
            list_of_candidates[candidate] = list_of_candidates.get(candidate, 0) + 1
        else:
            candidate = row[2]
            list_of_candidates.update({candidate: 1})

top_vote = 0
#print result in terminal
print("Election Results")
print("-------------------------")
print("Total Votes:", vote_count)
print("-------------------------")
for key,value in list_of_candidates.items():
     print(key, ":", "{:.3%}".format(value/vote_count),
     "(", value, ")")
     if value > top_vote:
        top_vote = value
        winner = key
print("-------------------------")
print("Winner:", winner)
print("-------------------------")

#export to analysis folder
with open('PyPoll/Analysis/analysis_results.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     
     writer.writerow(["Total Votes", vote_count])
     for key,value in list_of_candidates.items():
        writer.writerow([key,"{:.3%}".format(value/vote_count), value])
     writer.writerow(["Winner", winner])
