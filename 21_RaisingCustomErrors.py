# Why we need to raise custom errors ?
'''Some times we dont want our program to execute at a certain parameter so we need to raise
   custom errors so that our program will stop exectuing !
   To raise a custom error we use "raise" keyword
'''
# Program example :
userInput = int(input("Enter the number between 0 to 9 : "))
print("\n")
if userInput<0 or userInput>9 :
    raise ValueError("Invalid input !\nOnly the digit between 0 and 9 !!")
else :
    print(f"You have entered {userInput} successfully !")