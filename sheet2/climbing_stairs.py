def climb_stairs(n):
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second

if __name__ == "__main__":
    n = int(input("Enter number of stairs: "))
    print(f"Ways to climb: {climb_stairs(n)}")
