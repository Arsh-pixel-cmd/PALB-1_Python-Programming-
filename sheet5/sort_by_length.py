def sort_by_length(arr):
    # Sort by length (ascending) and then maintain relative order
    return sorted(arr, key=len)

if __name__ == "__main__":
    arr = input("Enter strings: ").split()
    print(f"Sorted by length: {sort_by_length(arr)}")
