# Check divisibility using if-elif (only one condition will run)
num = 18

if num % 2 == 0:
    print(num, "is divisible by 2")
elif num % 3 == 0:
    print(num, "is divisible by 3")
elif num % 5 == 0:
    print(num, "is divisible by 5")
else:
    print(num, "is not divisible by 2, 3, or 5")


# Check divisibility using multiple if statements (all conditions can run)
num = 18

if num % 2 == 0:
    print(num, "is divisible by 2")

if num % 3 == 0:
    print(num, "is divisible by 3")

if num % 5 == 0:
    print(num, "is divisible by 5")