def roman_to_int(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_val = 0
    for char in reversed(s):
        curr_val = roman_map[char]
        if curr_val >= prev_val:
            total += curr_val
        else:
            total -= curr_val
        prev_val = curr_val
    return total

if __name__ == "__main__":
    s = input("Enter Roman numeral: ").upper()
    print(f"Integer value: {roman_to_int(s)}")
