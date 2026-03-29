def previous_smaller_element(arr):
    stack = []
    pse = []
    for x in arr:
        while stack and stack[-1] >= x:
            stack.pop()
        pse.append(stack[-1] if stack else -1)
        stack.append(x)
    return pse

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array: ").split()]
    print(f"PSE: {previous_smaller_element(arr)}")
