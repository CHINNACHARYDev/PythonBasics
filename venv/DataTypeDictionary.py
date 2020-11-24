# Dictionary / Map

# It is an unordered set of key : value pairs
# Dictionary is mutable
# Indexing & Slicing are not allowed

mapValue = {'firstName' : 'CHINNA', 'lastName' : 'CHARY', 'age' : 26, 'profession' : 'Android Developer'}
print('Dictionary/Map Value', mapValue)

# Functions of Dictionary/Map

# Keys: Extracts all keys from dictionary and creates new List
print('Dictionary/Map Keys', mapValue.keys())
print('Dictionary/Map Keys List', list(mapValue.keys()))
# Values: Extracts all values from dictionary and creates new List
listValues = mapValue.values()
print('Dictionary/Map Values', mapValue.values())
print('Dictionary/Map Values List', list(mapValue.values()))
# Copy: Copies complete dictionary/map to new one
print('Dictionary/Map Copy', mapValue.copy())
# Pop: Pop specific element in the Dictionary/Map by key
print('Dictionary/Map Pop', mapValue.pop('age'))
print('Dictionary/Map New Dictionary', mapValue)
# Clear: Clears complete Dictionary/Map
mapValue.clear()
print('Dictionary/Map Clear', mapValue)