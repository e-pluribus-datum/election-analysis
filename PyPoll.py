import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
    print(election_data)

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    print(headers)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file.
# txt_file = open(file_to_save, "w")

# # Write some data to the file.
# txt_file.write("Counties in the Election\n" + "".ljust(25, "-") + "\nArapahoe\nDenver\nJefferson")

# # Close the file
# txt_file.close()

# # 1. Total number of votes cast
# # 2. Complete list of candidates who received votes
# # 3. Percentage of votes each candidate won
# # 4. Total number of votes each candidate won
# # 5. Winner of election based on popular vote