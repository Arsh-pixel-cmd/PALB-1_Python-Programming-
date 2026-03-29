def combination_sum2(candidates, target):
    candidates.sort()
    res = []
    
    def backtrack(remain, combo, start):
        if remain == 0:
            res.append(list(combo))
            return
        elif remain < 0:
            return
            
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            combo.append(candidates[i])
            backtrack(remain - candidates[i], combo, i + 1)
            combo.pop()
            
    backtrack(target, [], 0)
    return res

if __name__ == "__main__":
    candidates = [int(x) for x in input("Enter candidates: ").split()]
    target = int(input("Enter target: "))
    print(f"Combinations: {combination_sum2(candidates, target)}")
