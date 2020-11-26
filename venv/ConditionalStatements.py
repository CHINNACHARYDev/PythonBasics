# Conditional statements (Selection Statements/Decesion Making Statements)

# It will decide the execution of a block of code based on the condition of the expression

# 'if' Statement
# 'if else' Statement
# 'if elif else' Statement
# Nested 'if' Statement

A = 'CHINNA'
B = 'CHARY'
C = 'CHINNACHARY'
D = 'CHINNA CHARY'


# If Statement: It executes the set of instructions based on the condition
if A + B == C:
    print('If Statement IF', C)


# If Else Statement: It executes the set of instructions based on the condition
if A + B == C:
    print('If Else Statement IF', C)
else:
    print('If Else Statement ELSE', A + B)


# If ElIf Else Statement:
if A + B == D:
    print('If ElIf Else Statement IF', D)
elif A + B == C:
    print('If ElIf Else Statement ELIF', C)
else:
    print('If ElIf Else Statement ELSE', A + B)

# Nested If Statement:
if A + B == D:
    print('Nested If Statement IF1', D)
    if A + B == C:
        print('Nested If Statement IF2', C)
    else:
        print('Nested If Statement ELSE1', C)
else:
    print('Nested If Statement ELSE2', A + B)