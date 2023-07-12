def add(a=10,b=20): 
    return a+b

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
ans = add(num1,num2) # Postional arguments are called !
print(ans)

ans= add() # Default arguments will be called !
print(ans)

ans = add(b=5,a=3) #Keyword arguments
print(ans)

def func(*x): # value-type arguments 
    for i in x:
        print(i)

func(1,2,3,4)
func(10,20)
func("ZAID","zaid")
func() # Nothing will print 