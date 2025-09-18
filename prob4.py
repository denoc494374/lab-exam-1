def is_palindrome(valStr):
    return valStr == valStr[::-1]


def to_binary_if_number(value):
    if value.isdigit():
        return bin(int(value))[2:]
    return None


def main():
    value = input("Enter a value: ").strip()

    palindrome_check = is_palindrome(value)
    print(f"Input is a palindrome: {palindrome_check}")

    binary = to_binary_if_number(value)
    if binary:
        binary_palindrome_check = is_palindrome(binary)
        print(f"Binary equivalent: {binary}")
        print(f"Binary is a palindrome: {binary_palindrome_check}")
    else:
        print("No binary conversion since input is text.")


main()
