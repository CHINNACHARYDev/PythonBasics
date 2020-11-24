# Set Datatype

# Mutable
# Indexing, Slicing, Concatenation and Multiplications are Not Supported
# Not Supports 'Duplicates' and Not follows sequence

C = True
H = False
A = 4
R = 'CHINNA'
Y = 'CHARY'
I = 6
N = 3.9

setValue = {9, 7, 2, 1, 3, 4, 5, 5, 6, 8}
setValue2 = {C, H, A, R, Y}
print("Set Value", setValue) # will give u random set
print("Set Value 2", setValue2) # will give u random set

# Set Functions

# Add:  Adds new value to set
setValue.add(R)
print("Set Add", setValue)
# Discard: If element exist in the set will be removed, if not never returns anything
setValue.discard(Y)
print("Set Discard", setValue)
# IsSubset: Check if 'setValue2' is Subset of 'setValue' or Not (Returns True or False)
print("Set IsSubset", setValue2.issubset(setValue))
# Union: Removes duplicate elements and adds all sets to One set
setValueNew1 = setValue.union(setValue2)
print("Set Union", setValueNew1)
# Intersection: Removes all other elements except duplicate elements in both sets and creates new set
setValueNew2 = setValue.intersection(setValue2)
print("Set Intersection", setValueNew2)
# Difference: Only present in set and adds to new set
setValueNew3 = setValue.difference(setValue2)
print("Set Difference", setValueNew3)


# Frozen Set

# Immutable

fSet = (C, H, I, N, N, A, C, H, A, R, Y)
fSet2 = {C, H, I, N, N, A, C, H, A, R, Y}
fSet3 = [C, H, I, N, N, A, C, H, A, R, Y]

fSetValue = frozenset(fSet)
print("Set FrozenSet", fSetValue)
fSetValue2 = frozenset(fSet2)
print("Set FrozenSet2", fSetValue2)
fSetValue3 = frozenset(fSet3)
print("Set FrozenSet3", fSetValue3)