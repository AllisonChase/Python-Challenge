import os
import csv

electionData=os.path.join("PyPoll","Resources","election_data.csv" )

with open(electionData, "r") as electionFile:
    cleanexcel=csv.reader(electionFile)
    next(cleanexcel)
    # test=list(cleanexcel)
    # print(test)

    for row in cleanexcel:
        print(row)


