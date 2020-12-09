min = 278384
max = 824795

# part 1
def nbOfPwds_1(min, max):
    counter = 0
    for pwd in range(min, max, 1):
        adjacent = False
        increase = True
        pwd = list(str(pwd))

        for i, p in enumerate(pwd):
            if (i > 0):
                if (pwd[i-1] <= p):
                    if (p == pwd[i-1]):
                        adjacent = True
                else:
                    increase = False
                    break

        if (adjacent == True and increase == True):
            counter += 1

    return counter

# part 2
def nbOfPwds_2(min, max):
    counter = 0
    for pwd in range(min, max, 1):
        adjacent = False
        increase = True
        pwd = list(str(pwd))
        arr = []

        # print(pwd)
        for i, p in enumerate(pwd):
            if (i > 0):
                if (pwd[i-1] <= p):
                    if (p == pwd[i-1]): 
                        if (i < 5 and p != pwd[i+1]):
                            if (i > 1 and p != pwd[i-2]):
                                adjacent = True
                            elif (i == 1):
                                adjacent = True

                        elif (i == 5): # OK
                            if (p != pwd[i-2]):
                                adjacent = True

                        
                else:
                    increase = False
                    break

        if (adjacent == True and increase == True):
            counter += 1

    return counter


# part 1
print('1:',nbOfPwds_1(min, max))
# part 2
print('2:',nbOfPwds_2(min, max))