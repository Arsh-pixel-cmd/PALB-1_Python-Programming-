def min_time_difference(time_points):
    def to_seconds(t):
        h, m, s = map(int, t.split(':'))
        return h * 3600 + m * 60 + s
        
    seconds = sorted([to_seconds(t) for t in time_points])
    min_diff = float('inf')
    
    for i in range(1, len(seconds)):
        min_diff = min(min_diff, seconds[i] - seconds[i-1])
        
    # Check wrap around (24 hours = 86400 seconds)
    min_diff = min(min_diff, 86400 - (seconds[-1] - seconds[0]))
    
    return min_diff

if __name__ == "__main__":
    times = input("Enter time strings (HH:MM:SS) space separated: ").split()
    print(f"Minimum difference in seconds: {min_time_difference(times)}")
