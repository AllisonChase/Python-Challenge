import os 
import csv

budgetData=os.path.join("Resources","budget_data.csv")
# print(budgetData)

month=0

with open(budgetData, "r") as budgetFile:
    lessugly=csv.reader(budgetFile)
    next(lessugly)
    # test=list(lessugly)
    # print (test)

    for row in lessugly:
        print(row)
        month +=1

print("Financial Analysis")
print("----------------------------")
print ("Total months : " +str(month))