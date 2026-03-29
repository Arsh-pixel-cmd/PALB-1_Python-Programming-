def min_jumps(arr):
    n = len(arr)
    if n <= 1: return 0
    if arr[0] == 0: return -1
    
    max_reach = arr[0]
    steps = arr[0]
    jumps = 1
    
    for i in range(1, n - 1):
        max_reach = max(max_reach, i + arr[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            steps = max_reach - i
            
    return jumps

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array (max jump from each position): ").split()]
    print(f"Minimum jumps: {min_jumps(arr)}")
