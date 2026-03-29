def check_odd_even(n):
    return "Even" if n % 2 == 0 else "Odd"

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"{n} is {check_odd_even(n)}")
