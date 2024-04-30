"""
Simple Calculator
"""
# Provide your solution here

def calculate(a: int, b: int, operator):
    if operator == "+":
        print(a+b)
    elif operator == "-":
        print(a-b)
    elif operator == "*":
        print(a*b)
    elif operator == "/":
        if a == 0:
            print("Division by 0 is not allowed.")
        elif b == 0:
            print("Division by 0 is not allowed.")
        else:
            print(a/b)
    else:
        print("Invalid operator.")

calculate(0, 2, "/")


"""
Reverse Word
"""
# Provide your solution here
def reverse_word(word):
    length = len(word)
    reverse = word[-1] + word[-2] + word[-3] + word [-4] + word[-5] +
    print(str.capitalize(reverse))

reverse_word("hELLo")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

