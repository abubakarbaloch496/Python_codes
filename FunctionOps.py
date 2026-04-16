# Performs addition of two numbers
def add(num1, num2):
    print(num1, "+", num2, "=", num1 + num2)

# Performs subtraction of two numbers
def sub(num1, num2):
    print(num1, "-", num2, "=", num1 - num2)

# Performs multiplication of two numbers
def mul(num1, num2):
    print(num1, "*", num2, "=", num1 * num2)

# Performs division of two numbers
def divi(num1, num2):
    print(num1, "/", num2, "=", num1 / num2)


# Accept user input for first number
num1 = int(input("Enter a first number :"))
print(num1)  # Display entered first number

# Accept user input for second number
num2 = int(input("Enter a second number :"))

# Execute all arithmetic operations
add(num1, num2)
sub(num1, num2)
mul(num1, num2)
divi(num1, num2)