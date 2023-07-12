# Program to illustrate File I/O in Python :
f = open('NewFile.txt','w')
f.write("Hello World")      # It will over Write the text
f.close()

f = open('NewFile.txt',"a")
f.write("\nNew comment")    # It will add the text
f.close()

f = open('NewFile.txt','r')
text = f.read()
print(text)
f.close()

# readline() function :
g = open("readLine.txt","r")
while True:
    line = g.readline()
    if not line :
        break
    print(line)

# writeline() function :
h = open("writeLine.txt","w")
lines = ["line 1\n","line 2\n","line 3"]
h.writelines(lines)
h.close()
h = open("writeline.txt","r")
while True:
    line = h.readline()
    if not line:
        break
    print(line)