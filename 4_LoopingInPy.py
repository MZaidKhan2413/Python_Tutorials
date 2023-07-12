# ***Program to print even numbers in a range :***
Start = int(input("Enter the starting number : "))
Final = int(input("Enter the Nth term number : "))
for i in range(Start,Final+1):
    if(i%2==0):
        print(i)

# ***Porgram to print numbers with given differences :***
Start = int(input("Enter the starting number : "))
Final = int(input("Enter the Nth term number : "))
diff = int(input("Enter the difference b/w 2 nums : "))
for i in range(Start,Final,diff):
    print(i)

# ***Program to print String :***
Str = input("Enter a String : ")
for i in Str :
    print(i)