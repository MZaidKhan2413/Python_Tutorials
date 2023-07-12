# Python program to chech greatest of 3 number:
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))
if(a>b and b>c):
    print(a," is greatest")
elif(b>c):
    print(b," is greatest")
else:
    print(c," is greatest")