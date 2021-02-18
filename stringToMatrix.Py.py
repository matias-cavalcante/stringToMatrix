def splitAndList(chain, dim):
    """Receives a string that represent a numbers sequence being each one of them an integer. They are
    only separated from each other by a blank space. Also is given an integer representing the dimentions
    of an array. The program will put the integers in the chain inside of list of size (dim), resulting in
    the built of a matrix that is returned."""
    mainList = []
    i = 0
    for r in range(dim):
        row = []
        while len(row) < dim:
            go = True
            num = ""
            while go == True:
                if chain[i] != " ":
                    num = num + chain[i]
                    if i == len(chain)-1:
                        break
                    i = i + 1
                elif chain[i] == " ":
                    i = i + 1
                    go = False
            row.append(num)
        mainList.append(row)
    
    return mainList


#Examples below

"""values = 6 6 7 -10 9 -3 8 9 -1 9 7 -10 6 4 1 6 1 1 -1 -2 4 -6 1 -4 -6 3 9 -8 7 6 -1 -6 -6 6 -7 2 -10 -4 9 1 -7 8 -5 3 -5 -8 -3 -4 2 -3 7 -5 1 -5 -2 -7 -4 8 3 -1 8 2 3 -3 4 6 -7 -7 -8 -3 9 -6 -2 0 5 4 4 4 -3 3 0"""

values = """3 3 -2 1 2 5 7 -2 1"""
v = splitAndList(values, 3)

for r in v:
    print(r)