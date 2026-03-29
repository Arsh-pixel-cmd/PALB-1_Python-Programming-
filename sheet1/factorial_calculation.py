def factorial(n):
    if n < 0:
        return "Not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        res = 1
        for i in range(2, n + 1):
            res *= i
        return res

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Factorial of {n} is {factorial(n)}")
