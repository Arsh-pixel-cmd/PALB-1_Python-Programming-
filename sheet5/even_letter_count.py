from collections import Counter

def count_even_letters(s):
    count = Counter(s)
    res = 0
    for char, freq in count.items():
        if freq % 2 == 0:
            res += 1
    return res

if __name__ == "__main__":
    s = input("Enter string: ")
    print(f"Number of letters with even frequency: {count_even_letters(s)}")
