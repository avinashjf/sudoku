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
    suMainList = [0, 0, 9, 1, 0, 0, 0, 0, 7,
                  0, 0, 6, 2, 0, 0, 4, 0, 0,
                  0, 2, 0, 0, 7, 0, 0, 0, 0,
                  2, 4, 0, 0, 0, 0, 0, 8, 0,
                  0, 9, 5, 0, 1, 0, 3, 7, 0,
                  0, 3, 0, 0, 0, 0, 0, 5, 9,
                  0, 0, 0, 0, 8, 0, 0, 3, 0,
                  0, 0, 2, 0, 0, 7, 9, 0, 0,
                  5, 0, 0, 0, 0, 4, 8, 0, 0]
    #Evil rating: http://www.websudoku.com/?level=4&set_id=1431729349
    suMainList = [0, 3, 0, 6, 0, 0, 0, 0, 0,
                  0, 8, 0, 9, 0, 0, 0, 7, 0,
                  0, 0, 9, 5, 0, 7, 1, 0, 0,
                  0, 1, 0, 0, 0, 0, 2, 0, 4,
                  0, 0, 5, 0, 0, 0, 9, 0, 0,
                  3, 0, 2, 0, 0, 0, 0, 6, 0,
                  0, 0, 1, 2, 0, 6, 8, 0, 0,
                  0, 6, 0, 0, 0, 8, 0, 1, 0,
                  0, 0, 0, 0, 0, 4, 0, 9, 0]
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
    #print(suCellSquare)
    return suCellSquare

#Setup the possible values for each cell. 1-9 for each cell not identified
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

    #check for number pairs that can reduce the cell options for each row/ column
    #suCellOptions = calcOptionsPairs(suMainList, suCellOptions)

    # Iterate through the cells and reduce possible options
    for i in range(81):
        if suMainList[i]==0: #len(suCellOptions[i]) > 1:
            cell = suMainList[i]
            row = int((i - i % 9) / 9)
            column = i % 9
            square = suCellSquare[i]

            #check if a number between 1-9 exists already in the row or column or square combination. If so remove it as a possible combination
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

#Iterate through all cells and see if there is only one option for a certain cell because no other square can have that number as an opiton
def calcRemSquares(suMainList,suRowList,suColList,suSquareList,suCellSquare,suCellOptions):
    suList = [[],[],[],[],[],[],[],[],[]]
    for i in range(81):
        s=suCellSquare[i]
        suList[s].append(suCellOptions[i])
    for s in range(9):

        for j in numbersRemaining(suSquareList[s]):
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

#calculate remaining combinations/numbers to be identified
def numbersRemaining(suList):
    suRemain = []
    for i in range(1,10):
        if suList.count(i)==0:
            suRemain.append(i)
    return  suRemain

#calculate how many rows and columns have only 2 cells with 2 options for each cell (for eg: if cell[79] and cell[80] has options [1,6]
#then 1 and 6 can only go in those 2 cells with no other cell having this possiblity. Then go to the other cells that belong to the row
# or column and remove those numbers as options

def calcOptionsPairs(suMainList,suCellOptions):
    for i in range(81):
        if suMainList[i] == 0 and len(suCellOptions[i])==2:
            #go to each cell option for the row and find any options where the cell option matches exactly. if so its a pair
            row = int((i - i % 9) / 9)
            for j in range(9*row,9*row+9):
                if i!=j and suCellOptions[i] == suCellOptions[j]:
                    #if a pair is found then go to other cells in that row and remove these numbers as an option if it exists
                    #print("Cell " + str(i) + " matches with cell " + str(j) + " combinations " + str(suCellOptions[i]))
                    for k in range(9 * row, 9 * row + 9):
                        if k != i and k!=j: #since i and j are pairs and both of them are not to be touched
                            for pairNum in suCellOptions[i]: #iterate through all pair numbers and remove in other row cells
                                if suCellOptions[k].count(pairNum)==1:
                                    suCellOptions[k].remove(pairNum)
                                    #if only one cell option remains post removing the pairs then assign it as the number in main list
                                    if len(suCellOptions[k])==1: suMainList[k]=suCellOptions[k][0]

            # go to each cell option for the column and find any options where the cell option matches exactly. if so its a pair
            column = i % 9
            for j in [column,9*1+column,9*2+column,9*3+column,9*4+column,9*5+column,9*6+column,9*7+column,9*8+column]:
                if i != j and suCellOptions[i] == suCellOptions[j]:
                    # if a pair is found then go to other cells in that column and remove these numbers as an option if it exists
                    #print("Cell " + str(i) + " matches with cell " + str(j) + " combinations " + str(suCellOptions[i]))
                    for k in [column,9*1+column,9*2+column,9*3+column,9*4+column,9*5+column,9*6+column,9*7+column,9*8+column]:
                        if k != i and k != j:  # since i and j are pairs and both of them are not to be touched
                            for pairNum in suCellOptions[i]:  # iterate through all pair numbers and remove in other row cells
                                if suCellOptions[k].count(pairNum) == 1:
                                    suCellOptions[k].remove(pairNum)
                                    # if only one cell option remains post removing the pairs then assign it as the number in main list
                                    if len(suCellOptions[k]) == 1: suMainList[k] = suCellOptions[k][0]


    return suMainList

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

    suMainList = calcOptionsPairs(suMainList, suCellOptions)

    print("Iteration: " + str(mainrun) + " ----- Number of fields to solve: " + str(suMainList.count(0)))
    if suMainList.count(0)==0:
        break



for i in range(9):
    if i % 3 == 0:
        print("")
    print(str(suMainList[i*9:i*9+3]) + " " + str(suMainList[i*9+3:i*9+6]) + " " + str(suMainList[i*9+6:i*9+9]))


#print(Output)
for i in range(81):
    if suMainList[i] != 0:
        print("Cell " + str(i) + " = " + str(suMainList[i]))
    else:
        print("Cell " + str(i) + " = " + str(suCellOptions[i]) + "Square: " + str(suCellSquare[i]))


