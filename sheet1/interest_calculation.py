def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_compound_interest(principal, rate, time):
    return principal * (pow((1 + rate / 100), time)) - principal

if __name__ == "__main__":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period (in years): "))
    
    si = calculate_simple_interest(principal, rate, time)
    ci = calculate_compound_interest(principal, rate, time)
    
    print(f"Simple Interest: {si:.2f}")
    print(f"Compound Interest: {ci:.2f}")
