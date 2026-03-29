def sum_array_elements(arr):
    return sum(arr)

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array: ").split()]
    print(f"Total sum: {sum_array_elements(arr)}")
