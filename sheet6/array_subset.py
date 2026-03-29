def is_subset(a, b):
    # Check if b is a subset of a
    from collections import Counter
    count_a = Counter(a)
    count_b = Counter(b)
    for k, v in count_b.items():
        if count_a[k] < v:
            return False
    return True

if __name__ == "__main__":
    a = [int(x) for x in input("Enter a: ").split()]
    b = [int(x) for x in input("Enter b: ").split()]
    print(f"Is subset: {is_subset(a, b)}")
