from collections import Counter

def check_permutation_substring(txt, pat):
    n, m = len(txt), len(pat)
    if m > n: return False
    
    pat_count = Counter(pat)
    window_count = Counter(txt[:m])
    
    if pat_count == window_count: return True
    
    for i in range(m, n):
        window_count[txt[i]] += 1
        window_count[txt[i-m]] -= 1
        if window_count[txt[i-m]] == 0:
            del window_count[txt[i-m]]
        if window_count == pat_count:
            return True
            
    return False

if __name__ == "__main__":
    txt = input("Enter txt: ")
    pat = input("Enter pat: ")
    print(f"Permutation is substring: {check_permutation_substring(txt, pat)}")
