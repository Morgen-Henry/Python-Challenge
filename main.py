#import csv
import csv
import os
#read through csv file
csvpath = os.path.join("PyBank","Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    #set beginning values
    month_count = 0
    profit_loss_sum = 0
    prev_prof_loss = 0
    change = []
    great_in = 0
    great_de = 0
    #for loop for each rox in csv file
    next (reader)
    for row in reader:
        #add another month for each row
        month_count = month_count + 1
        #add the second colum of each row together to get a sum of every profit and loss
        profit_loss = int(row[1])
        profit_loss_sum = profit_loss_sum + profit_loss
        #find differences between the loss/profit values
        prof_loss_change = profit_loss - prev_prof_loss
        prev_prof_loss = profit_loss
        #list of changes to average later
        change.append(prof_loss_change)
        #check if this is the greatest increase or decrease
        if prof_loss_change > great_in:
            great_in = prof_loss_change
            great_in_mon = row[0]
        elif prof_loss_change < great_de:
            great_de = prof_loss_change
            great_de_mon = row[0]
        else:
            continue

#remove first value of change list
change.pop(0)

#format results
print("Financial Analysis")
print("----------------------------")
print("Total Months:", month_count)
print("Total: $", profit_loss_sum)
print("Average Change: $", round(sum(change)/len(change),2))
print("Greatest Increase in Profits:", great_in_mon, "($", great_in, ")")
print("Greatest Decrease in Profits:", great_de_mon, "($", great_de, ")")

#export result to text file in analysis file
with open('PyBank/Analysis/analysis_results.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     
     writer.writerow(["Total Months", month_count])
     writer.writerow(["Total", profit_loss_sum])
     writer.writerow(["Average Change", round(sum(change)/len(change),2)])
     writer.writerow(["Greatest Increase in Profits", great_in_mon, great_in])
     writer.writerow(["Greatest Decrease in Profits", great_de_mon, great_de])

