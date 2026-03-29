def sum_n_natural(n):
    return (n * (n + 1)) // 2

if __name__ == "__main__":
    n = int(input("Enter the value of N: "))
    if n < 1:
        print("Please enter a positive integer.")
    else:
        print(f"The sum of first {n} natural numbers is {sum_n_natural(n)}")
