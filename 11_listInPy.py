L1=[1,2,3,"xyz",True,1.5]
L2 = [1,2,3,4,5,6,7,8,9,0]
print(L1)
for i in range(0,5):
    print(L1[i])

# Negative Indexing in List :
print(L1[-2])   # len(L)-2

# Check weather a element present in List or not :
if "xyz" in L1 :
    print("YES !")
else : 
    print("NO !")

# Slicing in List :
print(L1[0:len(L1)])
print(L1[1:4])
print(L1[1:-1])

# JUMP_INDEX in list :
print(L1[0:len(L1):2])    # Index with the gap of 1 will be printed
print(L2[::3])            # Index with the gap of 2 will be printed

# List Comprehension :
L3=[i for i in range(4)]
print(L3)

L3=[i*i for i in range(1,5)]
print(L3)

L3=[i for i in range(1,10) if i%2==0]
print(L3)
