'''When we want to access a specific part of the file then we use seek() and tell() function
seek() : It takes an integer argument which represent the byte in text file. Helps to get to the postion of given argument
tell() : It tells the current postion in the file, in bytes.
'''
# Program to illustrate seek() function :
with open("NewFile.txt","r") as f :
    f.seek(5)          # Moves to the 5Th byte in the file
    print(f.tell())    # It will print 5
    data = f.read(3)   # Reads the next 3 bytes
    print(f.tell())    # It will print 8
    print(data)        # It will print the values at the given position