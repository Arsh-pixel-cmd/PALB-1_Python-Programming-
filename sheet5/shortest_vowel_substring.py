def shortest_vowel_substring(s):
    vowels = "aeiou"
    n = len(s)
    min_len = float('inf')
    
    for i in range(n):
        for j in range(i + 5, n + 1):
            sub = s[i:j]
            if all(v in sub for v in vowels):
                min_len = min(min_len, len(sub))
                
    return min_len if min_len != float('inf') else -1

if __name__ == "__main__":
    s = input("Enter string: ")
    print(f"Shortest vowel substring length: {shortest_vowel_substring(s)}")
