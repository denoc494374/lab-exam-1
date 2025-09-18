import math


def lcm(x, y):
    if x <= 0 or y <= 0:
        raise ValueError("Both numbers must be positive integers.")

    return abs(x * y) // math.gcd(x, y)


def main():
    try:
        x = int(input("Enter a value for x: "))
        y = int(input("Enter a value for y: "))

        if x <= 0 or y <= 0:
            print("Please enter positive non-zero integers.")
            return

        result = lcm(x, y)
        print(f"The LCM of {x} and {y} is = {result}")

    except ValueError:
        print("Please enter valid integers.")


main()
