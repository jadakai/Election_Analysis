# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who recieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of voyes each candidate won.
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate Votes.
candidate_options = []
candidate_votes = {}

#Challenge: County Options, County Votes.
county_names = []
county_votes = {}

#track the winning candidate vote and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Challenge: create variables for winning county and percentage
winning_county = ""
winning_county_count = 0

 
# Open the election results and read the file.
with open(file_to_load)as election_data:
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Print the header row.
    headers = next(file_reader)
    
    # Loop each row in the CSV file
    for row in file_reader:
        # Add to the toal vote count.
        total_votes += 1
        # get the candidate name from each row.
        candidate_name = row[2]
        # Get the county name from each row.
        county_name = row[1]
        
        #if the candidate does not match any existing candidate add to the list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # and begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1
        
        # Challenge
        if county_name not in county_names:
            # Add it to the list of county.
            county_names.append(county_name)
            # Begin tracking the county votes
            county_votes[county_name] = 0
        county_votes[county_name] += 1
        
# Write results to the text file
with open(file_to_save, 'w') as election_analysis:
    
    election_results = (
    
        f"Election Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n\n"
        f"County Votes:\n")
    
    print(election_results, end="")
    # Write final vote count to the text file
    election_analysis.write(election_results)
    
    # Determine the percentage of votes for each county.
    # Iterate through the county list.
    for county_name in county_votes:
        # Retrieve vote count of the candidate.
        votes_1 = county_votes[county_name]
        # Calculate the percentage of votes
        vote_percentage_1 = float(votes_1) / float(total_votes) * 100
        # Write the county name and percentage of votes.
        county_results = (f"{county_name}: {vote_percentage_1:.1f}% ({votes_1:,}\n")
        print(county_results)
        election_analysis.write(county_results)
        
        # Determine winning county
        # Determine if the votes are greater than winning count
        if (votes_1 > winning_county_count):
            #If true, set winning count equal to votes and winning county, and equal to county name
            winning_county_count = votes_1
            winning_county = county_name
            
    # Write results to the text file
    winning_county_results = (
        f"\n"
        f"--------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"--------------------\n")
    print(winning_county_results)
    election_analysis.write(winning_county_results)
    
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes_2 = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage_2 = float(votes_2) / float(total_votes) * 100
    
        #Write the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage_2:.1f}% ({votes_2:,})\n")
        print(candidate_results)
        election_analysis.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes_2 > winning_count) and (vote_percentage_2 > winning_percentage):
            # If true then set winning_count equal to votes and winning_percent to vote_percentage.
            winning_count = votes_2
            winning_percentage = vote_percentage_2
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # Write winning candidate results
    winning_candidate_results = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_results)
    election_analysis.write(winning_candidate_results)
    
        

        
    