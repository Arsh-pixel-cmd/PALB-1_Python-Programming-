def min_people_to_cover(arr):
    n = len(arr)
    intervals = []
    for i in range(n):
        if arr[i] != -1:
            intervals.append((max(0, i - arr[i]), min(n - 1, i + arr[i])))
            
    intervals.sort()
    count = 0
    current_end = -1
    max_reach = 0
    i = 0
    
    while max_reach < n - 1:
        best_reach = -1
        while i < len(intervals) and intervals[i][0] <= max_reach + 1 if max_reach != -1 else intervals[i][0] == 0:
            best_reach = max(best_reach, intervals[i][1])
            i += 1
            
        if best_reach == -1 or best_reach <= max_reach and max_reach != -1:
            return -1
        
        max_reach = best_reach
        count += 1
        if max_reach >= n - 1:
            return count
    return count

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter intervals (use -1 for unavailable): ").split()]
    print(f"Minimum people: {min_people_to_cover(arr)}")
