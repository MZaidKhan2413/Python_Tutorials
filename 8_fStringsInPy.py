# Program to show f-Strings :
text = "Hi my name is {} and I am from {}."
name="Zaid"
place="Bikaner"
text=text.format(name,place)      #String Formatting
print(text)

#Easy way of string formatting is F-String :
newtxt=f"Hi my name is {name} and I am from {place}."
print(newtxt)