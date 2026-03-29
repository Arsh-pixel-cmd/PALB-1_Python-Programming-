def min_swaps_to_make_identical(s1, s2):
    if len(s1) != len(s2): return -1
    
    # Count positions where they differ
    diff_s1_0 = 0 # s1 has 0, s2 has 1
    diff_s1_1 = 0 # s1 has 1, s2 has 0
    
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if c1 == '0':
                diff_s1_0 += 1
            else:
                diff_s1_1 += 1
                
    # Each swap can fix:
    # 2 differences of the same type (0-1, 0-1) -> 1 swap
    # 2 differences of different types (0-1, 1-0) -> 2 swaps
    
    res = (diff_s1_0 // 2) + (diff_s1_1 // 2)
    
    # If there's one of each type left
    if diff_s1_0 % 2 != diff_s1_1 % 2:
        return -1
        
    if diff_s1_0 % 2 == 1:
        res += 2
        
    return res

if __name__ == "__main__":
    s1 = input("Enter first binary string: ")
    s2 = input("Enter second binary string: ")
    print(f"Minimum swaps: {min_swaps_to_make_identical(s1, s2)}")
