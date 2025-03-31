import math


def square_root(x):
    if x < 0:
        raise ValueError("Square root of a negative number is not allowed")
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Factorial of a negative number is not allowed")
    return math.factorial(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Natural logarithm of non-positive numbers is not allowed")
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

if __name__ == "__main__":
    while True:
        print("\nScientific Calculator Menu:: ")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power Function (x^b)")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                num = float(input("Enter number: "))
                print("Result:", square_root(num))
            elif choice == '2':
                num = int(input("Enter integer: "))
                print("Result:", factorial(num))
            elif choice == '3':
                num = float(input("Enter number: "))
                print("Result:", natural_log(num))
            elif choice == '4':
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print("Result:", power(base, exponent))
            elif choice == '5':
                print("Goodbye!!  Exiting...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")
        except ValueError as e:
            print(f"Error: {e}")
