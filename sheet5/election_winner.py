from collections import Counter

def election_winner(votes):
    count = Counter(votes)
    # Get max votes
    max_votes = max(count.values())
    # Candidates with max votes
    winners = [name for name, v in count.items() if v == max_votes]
    # Smallest name lexicographically
    winners.sort()
    return [winners[0], str(max_votes)]

if __name__ == "__main__":
    votes = input("Enter votes (names): ").split()
    print(f"Winner: {election_winner(votes)}")
