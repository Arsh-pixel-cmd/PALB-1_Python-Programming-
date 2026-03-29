def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == "__main__":
    a = int(input("Enter first number (a): "))
    b = int(input("Enter second number (b): "))
    
    # Swapping using temporary variable
    temp = a
    a_new = b
    b_new = temp
    
    print(f"After swapping (using temp): a = {a_new}, b = {b_new}")
    
    # Swapping without temporary variable
    a_new2, b_new2 = swap_without_temp(a, b)
    print(f"After swapping (without temp): a = {a_new2}, b = {b_new2}")
