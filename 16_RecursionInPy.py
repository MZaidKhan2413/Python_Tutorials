# Program to print Fibonaccii series using recursion :
def func(fib):
    if(fib<=1):
        return fib
    else :
        return (func(fib-1) + func(fib-2))

num =int(input("Enter the range of series : "))
print("Fibonaccii series is : ")
for i in range(num):
    series = func(i)
    print(series,end=" ")