# Add dependencies
import csv
import os

# Add variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Add variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_options = []
candidate_votes = {}
county_list = []
county_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
separator = "".ljust(25, "-")

# Track the county with the largest turnout and the number of votes cast there
activist_county = ""
activist_votes = 0
activist_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name
        candidate_name = row[2]

        # Extract the county name
        county_name = row[1]

        # If the candidate does not match any existing candidate add them to
        # the candidate list and begin tracking their voter count
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county, add it to
        # the county list and begin tracking its voter count
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name] = 0

        # Add a vote to that county's vote count
        county_votes[county_name] += 1

# Save the results to text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"{separator}\n"
        f"Total Votes: {total_votes:,}\n"
        f"{separator}\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    # Write this also to the output text file
    txt_file.write(election_results)

    # Loop through county dictionary
    for county_name in county_votes:

        # Retrieve the county vote count
        cvotes = county_votes.get(county_name)

        # Calculate the percentage of votes for the county
        cvote_percentage = float(cvotes) / float(total_votes) * 100

         # Print the county results to the terminal
        county_results = (
            f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")
        print(county_results, end="")
         # Save the county votes to a text file
        txt_file.write(county_results)
         # Determine the most active county and get its vote count
        if (cvotes > activist_votes):
            activist_votes = cvotes
            activist_county = county_name
            activist_percentage = cvote_percentage 

    # Print the county with the largest turnout to the terminal
    county_summary = (
        f"\n"
        f"{separator}\n"
        f"Largest County Turnout: {activist_county}\n"
        f"{separator}\n"
        )
    print(county_summary)
    
    # Save the county with the largest turnout to the text file
    txt_file.write(county_summary)

    # Save the final candidate vote count to the text file
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to terminal
        print(candidate_results)

        # Save the candidate results to the text file
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate to terminal
    winning_candidate_summary = (
        f"{separator}\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"{separator}\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
