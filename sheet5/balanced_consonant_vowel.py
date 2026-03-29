def is_balanced_ratio(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    
    if v_count == 0 or c_count == 0:
        return False
        
    # Check if ratio is 1:1 or specific ratio given in sheet
    # Assuming 1:1 balance for this implementation
    return v_count == c_count

if __name__ == "__main__":
    s = input("Enter string: ")
    print(f"Is balanced (Vowels == Consonants): {is_balanced_ratio(s)}")
