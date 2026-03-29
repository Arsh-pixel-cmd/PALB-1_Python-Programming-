def combinationSum3(k, n):
    res = []
    
    def backtrack(num, stack, target):
        if len(stack) == k:
            if target == 0:
                res.append(list(stack))
            return
            
        for i in range(num, 10):
            if i > target:
                break
            stack.append(i)
            backtrack(i + 1, stack, target - i)
            stack.pop()
            
    backtrack(1, [], n)
    return res

if __name__ == "__main__":
    k = int(input("Enter k (number of elements): "))
    n = int(input("Enter n (target sum): "))
    print(f"Combinations: {combinationSum3(k, n)}")
