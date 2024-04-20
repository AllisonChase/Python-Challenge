#Code was created with help from BOOTCAMP TUTOR "Justin"

#import needed modules
import os 
import csv

#Import data from excel sheet
budgetData=os.path.join("PyBank","Resources","budget_data.csv")

#Define variables
month=0
profitorloss=0
earliermonth=0
increase=["", 0]
decrease=["", 9999999999999999999]
results=[]

#Clean up excel data that was imported
with open(budgetData, "r") as budgetFile:
    lessugly=csv.reader(budgetFile)
    
    #Don't include the top row
    next(lessugly)

    #Create loop to go through the "rows" in the data
    for row in lessugly:
        month +=1
        profitorloss += int(row[1])

        #Calculate change in profit or loss from the earlier month
        if month >1:
            change= int(row[1])- earliermonth
            results.append(change)

            #Calculate greatest increase in profits
            if change > increase[1]:
                increase[0]=row[0]
                increase[1]=change

            #Calculate greatest decrease in profits
            if change < decrease[1]:
                decrease[0]= row[0]
                decrease[1]=change

        earliermonth= int(row[1])

# Calculate the average
average= sum(results)/ len(results)


#Print the final results

print("Financial Analysis")
print("----------------------------")
print ("Total months : " +str(month))
print("Total: $"+str(profitorloss))
print("Average Change: $"+ str(average))
print("Greatest Increase in Profits: " + str(increase[0]) + " (" + str(increase[1]) + ")")
print("Greatest Decrease in Profits: " + str(decrease[0]) + " (" + str(decrease[1]) + ")")