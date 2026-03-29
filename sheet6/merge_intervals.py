def merge_intervals(intervals):
    if not intervals: return []
    intervals.sort()
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    return merged

if __name__ == "__main__":
    n = int(input("Enter number of intervals: "))
    arr = []
    for _ in range(n):
        arr.append([int(x) for x in input("Enter start end: ").split()])
    print(f"Merged: {merge_intervals(arr)}")
