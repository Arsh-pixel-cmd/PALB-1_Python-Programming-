def largest_string_k_deletions(s, k):
    # Lexicographically largest string after K deletions
    # We want to remove K characters such that the result is maximized
    # Mono-decreasing stack
    stack = []
    to_remove = k
    for char in s:
        while to_remove > 0 and stack and stack[-1] < char:
            stack.pop()
            to_remove -= 1
        stack.append(char)
        
    # If still need to remove
    while to_remove > 0:
        stack.pop()
        to_remove -= 1
        
    return "".join(stack)

if __name__ == "__main__":
    s = input("Enter string: ")
    k = int(input("Enter k: "))
    print(f"Largest string: {largest_string_k_deletions(s, k)}")
