# Easy way :
strg = "Hello World"[::-1]
print(strg)

# From Scratch :
def revstr(string):
    s =" "
    for i in string :
        s=i+s
    return s

String=input("Enter a string : ")
print("Reversed string is : ")
reverse = revstr(String)
print(reverse)

''' logic:
string = Hello
i = H ==> s = H;
i = e ==> s = eH;
i = l ==> s = leH;
and so on....
'''