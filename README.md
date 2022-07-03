# Election Analysis

## Overview
This project used Python to parse a CSV file containing information for votes cast in a local congressional election. Requested by the Board of Elections were:

1. The total number of votes cast.
2. A complete list of candidates who received votes.
3. The total number of votes each candidate received.
4. The percentage of votes each candidate received.
5. The winner of the election, based on popular vote.
6. The voter turnout for each county
7. Percentage of votes from each county
8. County with the highest proportion of the total votes


[The script](./PyPoll_Challenge.py) was written to print this information to terminal and to an [output text file](./analysis/election_analysis.txt).

## Resources
- Data Source: [election_results.csv](./Resources/election_results.csv)
- Software:
  - Python 3.9.12
  - Visual Studio Code 1.68.1

## Results
1. A total of 369,711 votes were cast in the election.

2. \- 4. are tabulated below:

    | Candidate Name | Votes Received | Votes Percentage |
    | -------------- | -------------: | ---------------: |
    | Diana DeGette | 272,892 | 73.8% |
    | Raymon Anthony Doane | 11,606 | 3.1% | 
    | Charles Casper Stockham | 85,213 | 23.0% |

<!-- start new numbered list -->

5. **Diana DeGette** won the election with 272,892 (73.8%) of the votes.

6. \- 7. are tabulated below:

    | County Name | Votes Cast | Percentage of All Votes|
    | ----------- | ---------: | ---------------------: |
    | Arapahoe | 24,801 | 6.7% |
    | Denver | 306,055 | 82.8% |
    | Jefferson | 38,855 | 10.5% |

<!-- -->

8. Most votes were cast from **Denver** county.

## Summary

This script is written such that the winner of the election is any candidate with the plurality of votes. For use in an election where there must be a majority vote, a warning message can be displayed:

```
if winning_percentage < 50:
    no_winner_warning = "The winner did not receive a majority!"
    print(no_winner_warning)
    txt_file.write(no_winner_warning)
```
Similarly, a warning message could be displayed if the minimum number of ballots was not cast:

```
quorum = 1000

if total_votes < quorum:
    no_quorum_warning = "There weren't enough votes to obtain a quorum!"
    print(no_quorum_warning)
    txt_file.write(no_quorum_warning)
```