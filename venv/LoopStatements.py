# Looping Statements (Iterative Statements)

# Executes set of instructions repeatedly

# Pythons supports 2 types of iterative statements 1. While Loop 2. For Loop

A = "CHINNA CHARY"
B = 0

# While Loop: Executes set of statements repetedly until condition fails

while B <= 6:
    print("While Loop B Value", B)
    B = B + 1

B = 0

while B <= 10:
    print("While Loop B Value", B)
    if B < 6:
        print("While Loop If B Value", B)
    elif B == 6:
        print("While Loop ElIf B Value", B)
    else:
        print("While Loop Else B Value", B)
    B = B + 1


# For Loop: Executes set of statements repeatedly depending on the no.of elements in sequence

for X in A:
    print("For Loop X Value", X)

for X in A:
    print("For Loop X Value", X)
    if X == ' ':
        print("For Loop X IF1 Value", X)
    else:
        print("For Loop X ELSE1 Value", X)
        if X == 'Y':
            print("For Loop X IF2 Value", X)
        else:
            print("For Loop X ELSE2 Value", X)