def merge_sorted_arrays(arr1, arr2):
    n, m = len(arr1), len(arr2)
    i = n - 1
    j = 0
    
    while i >= 0 and j < m:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i -= 1
            j += 1
        else:
            break
            
    arr1.sort()
    arr2.sort()

if __name__ == "__main__":
    arr1 = [int(x) for x in input("Enter arr1: ").split()]
    arr2 = [int(x) for x in input("Enter arr2: ").split()]
    merge_sorted_arrays(arr1, arr2)
    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")
