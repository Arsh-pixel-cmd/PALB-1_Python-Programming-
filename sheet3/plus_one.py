def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

if __name__ == "__main__":
    digits = [int(x) for x in input("Enter digits: ").split()]
    print(f"Result: {plus_one(digits)}")
