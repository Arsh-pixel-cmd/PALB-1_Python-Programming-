def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print(f"Fibonacci sequence up to {n} terms: {fibonacci(n)}")
