def count_vowel_strings(n):
    # Rule: Each vowel follows a specific vowel
    # a -> e
    # e -> a, i
    # i -> a, e, o, u
    # o -> i, u
    # u -> a
    
    # dp[i][j] = number of strings of length i ending with vowel j
    # a=0, e=1, i=2, o=3, u=4
    MOD = 10**9 + 7
    a, e, i, o, u = 1, 1, 1, 1, 1
    
    for _ in range(n - 1):
        a_next = (e + i + u) % MOD
        e_next = (a + i) % MOD
        i_next = (e + o) % MOD
        o_next = (i) % MOD
        u_next = (i + o) % MOD
        a, e, i, o, u = a_next, e_next, i_next, o_next, u_next
        
    return (a + e + i + o + u) % MOD

if __name__ == "__main__":
    n = int(input("Enter length n: "))
    print(f"Number of unique vowel strings: {count_vowel_strings(n)}")
