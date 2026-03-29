def score_of_parentheses(s):
    stack = [0]
    for char in s:
        if char == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2 * v, 1)
    return stack.pop()

if __name__ == "__main__":
    s = input("Enter balanced parentheses string: ")
    print(f"Score: {score_of_parentheses(s)}")
