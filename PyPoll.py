import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1

print(total_votes)
    