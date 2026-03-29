def common_elements(arr1, arr2, arr3):
    i = j = k = 0
    res = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            if not res or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    return res if res else -1

if __name__ == "__main__":
    arr1 = [int(x) for x in input("Enter sorted arr1: ").split()]
    arr2 = [int(x) for x in input("Enter sorted arr2: ").split()]
    arr3 = [int(x) for x in input("Enter sorted arr3: ").split()]
    print(f"Common: {common_elements(arr1, arr2, arr3)}")
