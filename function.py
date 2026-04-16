# Function to demonstrate simple message output
def my_function():
    print("you have created a function")

# Calling the function
my_function()


# Function to demonstrate loop and conditional logic
def mira():
    # Looping through odd numbers from 1 to 15
    for i in range(1, 17, 2):
        # This condition will never be true because i is always odd
        if i % 2 == 0:
            print(i, "even")

# Calling the function
mira()


# Function to print numbers from 1 to 10
def loop():
    for i in range(1, 11):
        print(i)

# Calling the function
loop()


# Function to calculate sum of two numbers
def late(num1, num2):
    print("sum is:", num1 + num2)

# Function call with arguments
late(13, 34)


# Function to calculate multiplication of two numbers
def lat(num1, num2):
    print("sum is:", num1 * num2)  # Note: output label says "sum" but it's multiplication

# Function call with arguments
lat(6, 34)