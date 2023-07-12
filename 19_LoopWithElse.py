# We can use "else" with loops also as well as conditional statements :
# else statement will only run if loop is ENDED successfully ! IF we break a loop then else statement will not run !

# Example program :
for i in range(10):
    print(i,end=" ")
else :
    print("\nLoop ended at i =",i)

# Example 2 :
num =0
while num < 10:
    print(num,end=" ")
    num = num+1
else :
    print("\nLoop ended at",num)

# Example 3 :
for j in range(11):
    if j==6:
        break
    else :
        print(j,end=" ")
else :
    print("Will not run if loop is broke")