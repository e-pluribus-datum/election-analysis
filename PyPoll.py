# Add dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize variables:
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
separator = "".ljust(25, "-")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row (ballot) in the CSV file.
    for row in file_reader:
        # Increment total vote counter       
        total_votes += 1
        # Local variable for candidate voted for in this ballot
        candidate_name = row[2]

        # If candidate not already in candidate list,
        if candidate_name not in candidate_options:
            # Add their name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking their vote count
            candidate_votes[candidate_name] = 0

        # Increment vote counter for current candidate
        candidate_votes[candidate_name] += 1

with open(file_to_save, 'w') as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"{separator}\n"
        f"Total Votes: {total_votes:,}\n"
        f"{separator}\n")
    print(election_results, end="") # end allows ending with a character other than '\n'
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine percentage of votes for each candidate
    for candidate_name in candidate_votes:
        # Initialize local variables for:
        # Vote count
        votes = candidate_votes[candidate_name]
        # Percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # String for candidate name, vote %, and # of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
        # Print above variable, then write it to output text file.
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine winning vote count, percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # Print winner's results to terminal
    winning_candidate_summary = (
        f"{separator}\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"{separator}\n")
    print(winning_candidate_summary)

    # Save those results to the output text file.
    txt_file.write(winning_candidate_summary)