def combination_sum(candidates, target):
    res = []
    
    def backtrack(remain, combo, start):
        if remain == 0:
            res.append(list(combo))
            return
        elif remain < 0:
            return
            
        for i in range(start, len(candidates)):
            combo.append(candidates[i])
            backtrack(remain - candidates[i], combo, i)
            combo.pop()
            
    backtrack(target, [], 0)
    return res

if __name__ == "__main__":
    candidates = [int(x) for x in input("Enter candidates: ").split()]
    target = int(input("Enter target: "))
    print(f"Combinations: {combination_sum(candidates, target)}")
