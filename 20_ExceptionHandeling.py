# try....except
# It checks the error in try body and executes except body :
num = input("Enter a number : ")
try:
    for i in range(int(num)):
        print(i,end=" ")
# except ValueError:
#     print("Invalid input !")
# except TypeError:
#     print("Data Type is not Correct")
# # etc...Much more type of errors are present in it !

except Exception as e :
    print(e)                # This method will print the actual error and run the after program
