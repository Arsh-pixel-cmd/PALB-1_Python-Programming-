from collections import Counter

def sort_by_frequency(s):
    count = Counter(s)
    # Sort by frequency (ascending) and then lexicographically
    items = sorted(count.items(), key=lambda x: (x[1], x[0]))
    res = ""
    for char, freq in items:
        res += char * freq
    return res

if __name__ == "__main__":
    s = input("Enter string: ")
    print(f"Sorted by frequency: {sort_by_frequency(s)}")
