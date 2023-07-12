list1 = [0,10,20,30,40,50]
list2 = [100,200,300]
print(len(list1))                   # Print the length of list
print(list1.index(20))              # Print the index of given element
print(list1.count(10))              # Print the total numbers , given element is present in list
list1.append(60)                    # Add a given element in the list
print(list1)
list1.reverse()                     # Reverse the list
print(list1)
list1.sort()                        # Sort the given list in ascending order
print(list1)
list1.sort(reverse=True)            # Sort the given list in decending order
print(list1)
list1.insert(2,15)                  # Insert a given element at a given index
print(list1)
print(list1.pop(2))                 # Delete the given index from the list
list1.extend(list2)
print(list1)
list1.remove(300)                   # Same as POP
print(list1)

# many more........