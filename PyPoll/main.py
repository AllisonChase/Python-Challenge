#import needed modules
import os
import csv

#Import data from excel sheet
electionData=os.path.join("PyPoll","Resources","election_data.csv" )

#Define variables
totalvotes = 0
candidates = {}
topvotes = 0
winnerwinnerchickendinner = ""

#Clean up excel data that was imported
with open(electionData, "r") as electionFile:
    cleanexcel=csv.reader(electionFile)
    
    #Don't include the top row
    next(cleanexcel)
    
    #Create loop to go through the "rows" in the data
    for row in cleanexcel:
        totalvotes += 1

        #Find the Candidate's name
        name = row[2]

        # If the candidate is already in the dictionary, add one more vote to their count
        if name in candidates:
            candidates[name] += 1
        else:
            # If the candidate isn't already in the dictionary, give them one vote to start
            candidates[name] = 1

# Print the vote totals
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalvotes))
print("-------------------------")

# Create loop to print out candidates result info
for candidate, votes in candidates.items():
    # Calculate %n
    percentage = (votes / totalvotes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    # Find the winner
    if votes > topvotes:
        topvotes = votes
        winnerwinnerchickendinner = candidate

#Print the winning Candidate
print("-------------------------")
print("Winner: " + str(winnerwinnerchickendinner))
print("-------------------------")