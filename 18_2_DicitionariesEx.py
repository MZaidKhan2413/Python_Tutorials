# PROGRAM TO INPUT ELEMENTS IN A DICTIONARY AND PRINT ITS KEYS ALONG WITH VALUES(SQ OF KEYS) :
def sqr(x):
    return x*x

dicr = {}
size = int(input("Enter the size of dict : "))
key_list = []
for i in range(size):
    key_elem = int(input(F"Enter the {i+1} value : "))
    key_list.append(key_elem)

value_list = list(map(sqr,key_list))

for key,value in zip(key_list,value_list):
    dicr[key] = value

for j in dicr:
    print(j," = ",dicr[j])