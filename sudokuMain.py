#Make sudoku great again
#row and column relationship cell=9*row +column, column = cell%9

# initialize variables and lists
suMainList = [0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0]
suRowList = [[],[],[],[],[],[],[],[],[]]
suColList = [[],[],[],[],[],[],[],[],[]]
suSquareList = [[],[],[],[],[],[],[],[],[]]
suCellSquare = list(suMainList)
suCellOptions = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]



#Setup initial puzzle with the puzzle cell values and return list
def initializePuzzle():
    suMainList = [0, 0, 0, 0, 0, 0, 5, 2, 0,
                  0, 9, 6, 4, 5, 3, 8, 0, 0,
                  0, 3, 1, 0, 0, 7, 0, 0, 0,
                  0, 0, 5, 0, 4, 6, 9, 0, 0,
                  4, 0, 0, 0, 9, 0, 0, 0, 7,
                  0, 0, 7, 3, 2, 0, 1, 0, 0,
                  0, 0, 0, 8, 0, 0, 4, 6, 0,
                  0, 0, 2, 6, 7, 4, 3, 1, 0,
                  0, 1, 4, 0, 0, 0, 0, 0, 0]
    suMainList = [0, 0, 9, 1, 0, 0, 0, 0, 7,
                  0, 0, 6, 2, 0, 0, 4, 0, 0,
                  0, 2, 0, 0, 7, 0, 0, 0, 0,
                  2, 4, 0, 0, 0, 0, 0, 8, 0,
                  0, 9, 5, 0, 1, 0, 3, 7, 0,
                  0, 3, 0, 0, 0, 0, 0, 5, 9,
                  0, 0, 0, 0, 8, 0, 0, 3, 0,
                  0, 0, 2, 0, 0, 7, 9, 0, 0,
                  5, 0, 0, 0, 0, 4, 8, 0, 0]
    return suMainList

#Setup initialize row variable
def initSuRows(suMainList):
    suRowList = [[], [], [], [], [], [], [], [], []]
    # Calculate row index
    suRowList = [suMainList[0:9], suMainList[9:18], suMainList[18:27], suMainList[27:36], suMainList[36:45],
    suMainList[45:54], suMainList[54:63], suMainList[63:72], suMainList[72:81]]
    return suRowList

#Setup initialize column variable
def initSuColumns(suMainList):
    suColList = [[], [], [], [], [], [], [], [], []]
    # Create the list of column lists for the main list
    for i in range(81):
        j = i % 9
        # colList.append(i)
        suColList[j].append(suMainList[i])
    return suColList

#Setup initialize square variable
def initSuSquares(suMainList):
    suSquareList = [[], [], [], [], [], [], [], [], []]
    # Create the list of square lists for the main list
    for s in range(0, 3):
        for r in range(3 * s + 0, 3 * s + 3):
            for c in range(0, 3):
                suSquareList[3 * s + 0].append(suMainList[9 * r + c])
        for r in range(3 * s + 0, 3 * s + 3):
            for c in range(3, 6):
                suSquareList[3 * s + 1].append(suMainList[9 * r + c])
        for r in range(3 * s + 0, 3 * s + 3):
            for c in range(6, 9):
                suSquareList[3 * s + 2].append(suMainList[9 * r + c])
    #print(suSquareList)
    return suSquareList

#Setup initialize Cellsquare variable which calculates the square each cell belongs to
def initSuCellSquare(suMainList):
    suCellSquare = list(suMainList)
    # Create the list of square lists for the main list
    for s in range(0, 3):
            for c in range(0, 3):
                for r in range(3 * s + 0, 3 * s + 3):
                    suCellSquare[9 * r + c] = 3*s+0
            for c in range(3, 6):
                for r in range(3 * s + 0, 3 * s + 3):
                    suCellSquare[9 * r + c] = 3*s+1
            for c in range(6, 9):
                for r in range(3 * s + 0, 3 * s + 3):
                    suCellSquare[9 * r + c] = 3*s+2
    print(suCellSquare)
    return suCellSquare

#Setup the possible values for each cell
def initSuCellOptions(suMainList):
    suCellOptions = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                     [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                     [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    #initialize possible list for each cell
    for i in range(81):
        # if puzzle already has cell provided then use it as the only option else populate 1 to 9
        if suMainList[i] != 0:
            suCellOptions[i].append(suMainList[i])
        else:
            for j in range(1, 10):
                suCellOptions[i].append(j)

    #print(suCellOptions)
    return  suCellOptions

#Iterate though the variables and run logic
def calcRemOptions(suMainList,suRowList,suColList,suSquareList,suCellSquare,suCellOptions):
    # Iterate through the cells and reduce possible options
    for i in range(81):
        if suMainList[i]==0: #len(suCellOptions[i]) > 1:
            cell = suMainList[i]
            row = int((i - i % 9) / 9)
            column = i % 9
            square = suCellSquare[i]

            for j in range(1, 10):
                if suRowList[row].count(j) > 0 or suColList[column].count(j) > 0 or suSquareList[square].count(j) and suCellOptions[i].count(j) > 0:
                    suCellOptions[i].remove(j)

            #     if suRowList[row].count(j) > 0:
            #         suCellOptions[i].remove(j)
            #     if suColList[column].count(j) > 0 and suCellOptions[i].count(j) > 0:
            #         suCellOptions[i].remove(j)
            #     if suSquareList[square].count(j) > 0 and suCellOptions[i].count(j) > 0:
            #         suCellOptions[i].remove(j)
            if suMainList[i] == 0 and len(suCellOptions[i]) == 1:
                suMainList[i] = suCellOptions[i][0]
    return suMainList

#Iterate through all cells and see if there is only one option for a certain cell
def calcRemSquares(suMainList,suRowList,suColList,suSquareList,suCellSquare,suCellOptions):
    suList = [[],[],[],[],[],[],[],[],[]]
    for i in range(81):
        s=suCellSquare[i]
        suList[s].append(suCellOptions[i])
    for s in range(9):

        for j in cellsRemaining(suSquareList[s]):
            count = 0
            for possibles in suList[s]:
                if possibles.count(j)==1:
                    count+=1
            if count==1:
                #print (str(j) + " is a possiblity in square" + str(s))
                for p in range(81):
                    if suCellSquare[p] == s:
                        if suCellOptions[p].count(j)==1:
                            suMainList[p]=j

    print(suList)
    return suMainList


#calculate cells to be identified
def cellsRemaining(suList):
    suRemain = []
    for i in range(9):
        if suList.count(i)==0:
            suRemain.append(i)
    return  suRemain


#intialize puzzle
suMainList = initializePuzzle()
suCellSquare = initSuCellSquare(suMainList)

print("Iteration: " + str(1) + " ----- Number of fields to solve: " + str(suMainList.count(0)))

for mainrun in range(2,50):
    #Initialize after every run
    suRowList = initSuRows(suMainList)
    suColList = initSuColumns(suMainList)
    suSquareList = initSuSquares(suMainList)
    suCellOptions = initSuCellOptions(suMainList)

    #Solve puzzle
    suMainList = calcRemOptions(suMainList, suRowList, suColList, suSquareList, suCellSquare, suCellOptions)

    suMainList = calcRemSquares(suMainList, suRowList, suColList, suSquareList, suCellSquare, suCellOptions)

    print("Iteration: " + str(mainrun) + " ----- Number of fields to solve: " + str(suMainList.count(0)))
    if suMainList.count(0)==0:
        break

for i in range(9):
    print(suMainList[i*9:i*9+9])

#print(Output)
for i in range(81):
    if suMainList[i] != 0:
        print("Cell " + str(i) + " = " + str(suMainList[i]))
    else:
        print("Cell " + str(i) + " = " + str(suCellOptions[i]) + "Square: " + str(suCellSquare[i]))


