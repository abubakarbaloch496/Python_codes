# Prints multiplication tables from 2 up to the given number
num=int(input("Enter a number"))
for i in range(2,num+1):
        for p in range(1,11):
            print(p,"x",i,"=", p*i )
        print()