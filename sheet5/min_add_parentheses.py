def min_add_to_make_valid(s):
    res = 0
    balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            if balance > 0:
                balance -= 1
            else:
                res += 1
    return res + balance

if __name__ == "__main__":
    s = input("Enter parentheses string: ")
    print(f"Minimum additions needed: {min_add_to_make_valid(s)}")
