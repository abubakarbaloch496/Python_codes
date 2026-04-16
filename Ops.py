# Function to perform addition
def add(num1, num2):
    print(num1, "+", num2, "=", num1 + num2)

# Function to perform subtraction
def sub(num1, num2):
    print(num1, "-", num2, "=", num1 - num2)

# Function to perform multiplication
def mul(num1, num2):
    print(num1, "*", num2, "=", num1 * num2)

# Function to perform division
def divi(num1, num2):
    print(num1, "/", num2, "=", num1 / num2)


# Taking user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Menu-driven loop for repeated operations
while True:
    print("\n1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")

    choice = int(input("Enter your choice: "))

    # Performing selected operation
    if choice == 1:
        add(num1, num2)

    elif choice == 2:
        sub(num1, num2)

    elif choice == 3:
        mul(num1, num2)

    elif choice == 4:
        divi(num1, num2)

    elif choice == 5:
        break  # Exit the program loop

    else:
        print("Invalid choice selected. Please try again.")