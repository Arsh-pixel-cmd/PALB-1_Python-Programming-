from collections import defaultdict

def group_anagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())

if __name__ == "__main__":
    strs = input("Enter strings: ").split()
    print(f"Grouped anagrams: {group_anagrams(strs)}")
