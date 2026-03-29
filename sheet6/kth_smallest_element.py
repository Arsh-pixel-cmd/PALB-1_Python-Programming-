import random

def kth_smallest(arr, k):
    # Quick select algorithm for O(n) average time
    if not arr: return None
    
    pivot = random.choice(arr)
    lefts = [x for x in arr if x < pivot]
    middles = [x for x in arr if x == pivot]
    rights = [x for x in arr if x > pivot]
    
    if k <= len(lefts):
        return kth_smallest(lefts, k)
    elif k <= len(lefts) + len(middles):
        return pivot
    else:
        return kth_smallest(rights, k - len(lefts) - len(middles))

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array: ").split()]
    k = int(input("Enter k: "))
    print(f"{k}th smallest element: {kth_smallest(arr, k)}")
