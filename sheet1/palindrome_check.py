def is_palindrome(s):
    # Convert to string to handle both numbers and strings
    s = str(s).lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string or number: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")
