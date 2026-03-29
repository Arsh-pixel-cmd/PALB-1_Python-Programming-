def count_one_mismatch_pairs(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if len(arr[i]) != len(arr[j]):
                continue
            mismatch = 0
            for c1, c2 in zip(arr[i], arr[j]):
                if c1 != c2:
                    mismatch += 1
            if mismatch == 1:
                count += 1
    return count

if __name__ == "__main__":
    arr = input("Enter strings: ").split()
    print(f"One mismatch pairs: {count_one_mismatch_pairs(arr)}")
