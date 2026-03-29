def count_subarrays_with_min_first(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        min_val = arr[i]
        for j in range(i, n):
            if arr[j] < min_val:
                break
            count += 1
    return count

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array: ").split()]
    print(f"Count of subarrays: {count_subarrays_with_min_first(arr)}")
