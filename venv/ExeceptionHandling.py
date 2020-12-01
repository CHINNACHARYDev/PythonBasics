# Exeption Handling

# Runtime Error : End user and Programmer responsible for this error
# Syntax Error  : Programmer responsible for this error

A = 'CHINNA'
B = 'CHARY'
C = 3
D = 6

if C > D:
    print("kjhkjh")
# else:  Will give you sytax error (SyntaxError: unexpected EOF while parsing)


# Zero Division Error:
try:
    if C / 0 == D:
        print("ZeroDivisionError C / 0 == D")
except ZeroDivisionError:
    print("ZeroDivisionError ", ZeroDivisionError)
finally:
    print("C value can't divides by 0")

# Type Error:
try:
    if A + C:
        print('TypeError A == C')
    elif A / C:
        print("TypeError A / C")
except TypeError:
    print('TypeError ', TypeError)
finally:
    print("String value can't be match with Integer value")

# Name Error:
try:
    if E == A:
        print("NameError E == A")
except NameError:
    print("NameError ", NameError)
finally:
    print("E value not defined")

# Value Error:
try:
    E = int(input("Enter Your Age "))
except ValueError:
    print("ValueError", ValueError)
    print("Given value is not an Integer")
    E = int(input("Enter Your Age "))
finally:
    print("Your Age is ", E)
    print("If user input Datatype is diffent than actual input datatype")