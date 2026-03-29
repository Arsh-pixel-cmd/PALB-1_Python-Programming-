def reverse_num(n):
    rev = 0
    temp = abs(n)
    while temp > 0:
        rev = rev * 10 + (temp % 10)
        temp //= 10
    return rev if n >= 0 else -rev

if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    print(f"Reversed integer: {reverse_num(n)}")
