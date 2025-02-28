from .utils import add, subtract, multiply, divide, power
def ask_user_input():
    """
    This function asks the user to input two numbers and an operator

    Parameters:
        - None

    Returns:
        - tuple: A tuple containing two numbers and an operator
    """

    operator = input("Enter an operator (+, -, *, /): ")

    while operator not in ['+', '-', '*', '/']:
        operator = input("Enter an operator (+, -, *, /): ")

    if operator in ["+", "*"]:
        n_number = input("How many numbers do you want to add or multiply: ")
        while not n_number.isdigit():
            n_number = input("How many numbers do you want to add or multiply: ")
        n_number = int(n_number)
        numbers = []

        for i in range(n_number):
            number = input(f"Enter number {i+1}: ")
            while not number.isdigit():
                number = input(f"Enter number {i+1}: ")
            numbers.append(int(number))
    else:
        n_number = 2
        numbers = []

        for i in range(n_number):
            number = input(f"Enter number {i+1}: ")
            while not number.isdigit():
                number = input(f"Enter number {i+1}: ")
            numbers.append(int(number))

    return numbers, operator

def calculator():
    numbers, operator = ask_user_input()
    result = 0
    if operator == "+":
        result = add(numbers)
    elif operator == "-":
        result = subtract(numbers)
    elif operator == "*":
        result = multiply(numbers)
    elif operator == "/":
        result = divide(numbers[0], numbers[1])

    return result

def print_result():
    result = calculator()
    print(f"The result is: {result}")


if __name__ == "__main__":
    print_result()
