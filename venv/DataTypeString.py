# String Variable

# Immutable
# Positive & Negetive Indexing

# String can be in 'Single Quoted', "Double Quoted" or '''Triple Quoted'''
valueOne = 'CHINNA'
valueTwo = "CHARY"
valueThree = '''CHINNA CHARY'''

# String Objects are Immutable
# value[0] = "K"
# We can add 2 strings & can slice string but we can't update existing characters with new chars

# Indexing: String Index in Python will be in Passive Indexing (0 to End) and Negetive Indexing (-1 to End)
value = 'CHINNA CHARY'
# Passive Indexing      0   1   2   3   4   5   6   7   8   9   10  11
# String Value          C   H   I   N   N   A       C   H   A   R   Y
# Negetive Indexing     -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

# Slicing: We can slice string using ':' operator
print('String Slicing', value[0:6])
# Concatenation: We can Concatenation(ADD) 2 or More strings into 1 String
print('Concatenation String', valueOne + " " + valueTwo)
# Multiplication: We can multifly the string into number of times
print('Multiplication String', value * 3)

# String Functions
exValue = 'Chinna Chary'
exValueTwo = '@ $ Chinna Chary % &'

# Capitalize: Capitalize converts 1st Letter of the 1st Word in the string into Upper Case
# And the rest letters into Lower Case
print('Capitalize String', exValue.capitalize())
# Title: Title converts 1st Letter of every word in the string into Upper Case
# And the rest into Lower case
print('Title Sting', exValue.title())
# IsLower (TRUE or FALSE): Check Letters/Words is in Lower Case or Not
print("isLower String", exValue.islower())
# IsUpper (TRUE or FALSES): Check Letters/Words is in Upper Case or Not
print('isUpper String', exValue.isupper())
# Lower: Converts every letter in the string into Lower Case
print("Lower String", exValue.lower())
# Upper: Converts every letter in the string into Upper Case
print("Upper String", exValue.upper())
# SwapCase: Converts Lower Case to Upper and Upper Case to Lower
print('Swap Case String', exValue.swapcase())
# Replace: Replace an existing chars with new chars
print('Replace String', exValue.replace('Chinna', 'CHINNA'))
# Length: Count the number of chars in the string
print('Length String', len(exValue))
# Count: Count the number of specific char
print('Count String', exValue.count('C'))
# Split: Splits the given string into multiple strings
print('Split String', exValue.split())
# Strip: Removes the Special chars 'strip', 'lstrip', 'rstrip'
print('Strip String', exValueTwo.strip('@&'))
print('Left Strip String', exValueTwo.lstrip('@'))
print('Right Strip String', exValueTwo.rstrip('&'))


