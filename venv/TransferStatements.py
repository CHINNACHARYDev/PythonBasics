# Transfer Statements

# Python supports 2 types of Transfer Statements 1. Break 2. Continue

A = 'CHINNA CHARY'
B = 0

# Break: We can use break statement inside loops to break loop execution based on some condition.

while B <= 10:
    print("Break While Loop B Value", B)
    if B < 6:
        print("Break While Loop If B Value", B)
    elif B == 6:
        print("Break While Loop ElIf B Value", B)
        break
    else:
        print("Break While Loop Else B Value", B)
    B = B + 1


for X in A:
    print("Break For Loop X Value", X)
    if X == ' ':
        print("Break For Loop X IF1 Value", X)
        break
    else:
        print("Break For Loop X ELSE1 Value", X)
        if X == 'Y':
            print("Break For Loop X IF2 Value", X)
        else:
            print("Break For Loop X ELSE2 Value", X)



A = 'CHINNA CHARY'
B = 0

# Continue: We can use continue statement inside loops to skip current iteration and continue to next iteration.

while B <= 10:
    print("Continue While Loop B Value", B)
    if B < 6:
        print("Continue While Loop If B Value", B)
    elif B == 6:
        B = B + 1
        continue
        print("Continue While Loop ElIf B Value", B)
    else:
        print("Continue While Loop Else B Value", B)
    B = B + 1


for X in A:
    print("Continue For Loop X Value", X)
    if X == ' ':
        continue
        print("Continue For Loop X IF1 Value", X)
    else:
        print("Continue For Loop X ELSE1 Value", X)
        if X == 'Y':
            print("Continue For Loop X IF2 Value", X)
        else:
            print("Continue For Loop X ELSE2 Value", X)