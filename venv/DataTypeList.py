# List Variable

# Collection of Elements
# Mutable
# Positive & Negetive Indexing

stringValueOne = 'CHINNA CHARY'
stringValueTwo = 'Chinna Chary'
a = 'C'
b = 'H'
c = 'I'
d = 'N'
e = 'N'
f = 'A'
g = ' '
h = 'C'
i = 'H'
j = 'A'
k = 'R'
l = 'Y'
listValue = [a, b, c, d, e, f, g, h, i, j, k, l]
listOne = [a, b, c, d, e, f]
listTwo = [h, i, j, k, l]
listSpecial = [1, 'CHINNA', True, 3.3]
listIntegers = [1, 2, 3, 4, 5, 6]
print('List', listValue)

# Indexing: List Index in Python will be in Passive Indexing (0 to End) and Negetive Indexing (-1 to End)
# Passive Indexing      0   1   2   3   4   5   6   7   8   9   10  11
# String Value          C   H   I   N   N   A       C   H   A   R   Y
# Negetive Indexing     -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
print('Indexing', listValue[2])

# Slicing: We can slice list using ':' operator
print("Slicing List", listValue[0:6])
# Concatenation: We can Concatenation(ADD) 2 or More list into 1 List
print('Concatenation List', listOne + listTwo)
# Multiplication: We can multifly the List into number of times
print('Multiplication List', listOne * 3)
# Packing: listValue = [a, b, c, d, e, f, g, h, i, j, k, l]
# UnPacking: a, b, c, d, e, f, g, h, i, j, k, l = listValue

# List Inside List
listInsideList = [listOne, listTwo]
print('List Inside List', listInsideList)
# String to List
print('String to List', stringValueOne.split())
# List to String
print('List to String', ' '.join(listValue))

# List Funtions

# Lenght: Counts number of elements
print("Length List", len(listValue))
# Count: Specific element count
print("Count List", listValue.count('C'))
# Extend: Can add multiple elements at the end of the List
listOne.extend([listTwo])
print("Extend List", listOne)
# Insert: Can insert multiple elements at required position
listOne.insert(6, listTwo)
print("Insert List", listOne)
# Remove: Remove the specific element in the list
listValue.remove(' ')
print("Remove Element", listValue)
# Insert: Can insert multiple elements at required position
listValue.insert(6, ' ')
print("Insert List", listValue)
# Pop: Remove the specific element in the list based on 'Index'
listValue.pop(6)
print("Pop List", listValue)
# Insert: Can insert multiple elements at required position
listValue.insert(6, ' ')
print("Insert List", listValue)
# Reverse: Reverse the complete existing list
listValue.reverse()
print("Reverse List", listValue)
listValue.reverse()
# Copy: This function copies the existing list into new variable
listValue2 = listValue.copy()
print("Copy List", listValue2)
# Clear: Clears the elements in the list
listValue2.clear()
print("Clear List", listValue2)
# Minimum: Finds the minimum value of the list of int
print("Minimum Value List", min(listIntegers))
# Maximum: Finds the maximum value of the list of int
print("Maximum Value List", max(listIntegers))
# Sort: Sorts elements in the list
listValue2 = listValue.copy()
listValue2.sort(reverse=False)
print("Sort List", listValue2)

