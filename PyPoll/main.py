import csv
import os

def count_votes(file):
    with open(file, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader, None)

        votes = 0
        for row in reader:
            votes += 1
        return votes

def compile_candidate(file):
    with open(file, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader, None)
    
        candidates = {}
        for row in reader:
            name = row[2]
            if name in candidates:
                candidates[name] += 1
            else:
                candidates[name] = 1

    return candidates

if __name__ == "__main__":
    basefolder = os.path.dirname(os.getcwd())
    csvfile = os.path.join(basefolder, "pypoll", "Resources", "election_data.csv")
    votes = count_votes(csvfile)
    candidates = compile_candidate(csvfile)
    max_votes = 0
    winner = ""

    print("\nElection Results\n")
    print("---------------------------\n")
    print(f"Total Votes: {votes}\n")
    print("---------------------------\n")
    for candidate, candidate_votes in candidates.items():
        vote_percentage = (candidate_votes / votes) * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({candidate_votes})\n")
        if candidate_votes > max_votes:
            max_votes = candidate_votes
            winner = candidate
    print("---------------------------\n")
    print(f"Winner: {winner}\n")
    print("---------------------------")

output_file = os.path.join(basefolder, "pypoll", "analysis", "results.txt")

with open(output_file, "w") as f:
    f.write("\nElection Results\n")
    f.write("---------------------------\n")
    f.write(f"Total Votes: {votes}\n")
    f.write("---------------------------\n")
    for candidate, candidate_votes in candidates.items():
        vote_percentage = (candidate_votes / votes) * 100
        f.write(f"{candidate}: {vote_percentage:.3f}% ({candidate_votes})\n")
        if candidate_votes > max_votes:
            max_votes = candidate_votes
            winner = candidate
    f.write("---------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("---------------------------")