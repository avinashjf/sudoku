#Make sudoku great again

#row and column relationship cell=9*row +column, column = cell%9

#initialize the sudoku list

suMainList = [0, 0, 0, 0, 0, 0, 5, 2, 0,
              0, 9, 6, 4, 5, 3, 8, 0, 0,
              0, 3, 1, 0, 0, 7, 0, 0, 0,
              0, 0, 5, 0, 4, 6, 9, 0, 0,
              4, 0, 0, 0, 9, 0, 0, 0, 7,
              0, 0, 7, 3, 2, 0, 1, 0, 0,
              0, 0, 0, 8, 0, 0, 4, 6, 0,
              0, 0, 2, 6, 7, 4, 3, 1, 0,
              0, 1, 4, 0, 0, 0, 0, 0, 0]

# initialize the colList and squareList structure
suColList = [[],[],[],[],[],[],[],[],[]]
suSquareList = [[],[],[],[],[],[],[],[],[]]
suCellSquare = list(suMainList)

#initialize possible list for each cell
suCellOptions = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                 [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for i in range(81):
    #if puzzle already has cell provided then use it as the only option else populate 1 to 9
    if suMainList[i]!=0:
        suCellOptions[i].append(suMainList[i])
    else:
        for j in range(1,10):
            suCellOptions[i].append(j)

print(suCellOptions)

#Calculate row index
suRowList = [suMainList[0:9], suMainList[9:18], suMainList[18:27], suMainList[27:36], suMainList[36:45], suMainList[45:54], suMainList[54:63], suMainList[63:72], suMainList[72:81]]

# Create the list of column lists for the main list
for i in range(81):
    j = i%9
    #colList.append(i)
    suColList[j].append(suMainList[i])

# Create the list of square lists for the main list
for s in range(0,3):
    for r in range(3*s+0,3*s+3):
        for c in range(0,3):
            suSquareList[3*s+0].append(suMainList[9*r+c])
            suCellSquare[9*r+c]=3*s+0
        for c in range(3,6):
            suSquareList[3*s+1].append(suMainList[9*r+c])
            suCellSquare[9 * r + c] = 3 * s + 0
        for c in range(6,9):
            suSquareList[3*s+2].append(suMainList[9 * r + c])
            suCellSquare[9 * r + c] = 3 * s + 0


#Iterate through the cells and reduce possible options
for i in range(81):
    if len(suCellOptions[i])>1:
        cell = suMainList[i]
        row = int((i-i%9)/9)
        column = i%9
        square = suCellSquare[i]

        for j in range(1,10):
            if suRowList[row].count(j)>0:
                suCellOptions[i].remove(j)
            if suColList[column].count(j)> 0 and suCellOptions[i].count(j)>0:
                suCellOptions[i].remove(j)
            if suSquareList[square].count(j)> 0 and suCellOptions[i].count(j)>0:
                suCellOptions[i].remove(j)
        if suMainList[i] ==0 and len(suCellOptions[i])==1:
            suMainList[i] = suCellOptions[i][0]

print("Number of fields to solve: " + str(suMainList.count(0)))
#print(suSquareList)
for i in range(81):
    if suMainList[i] != 0:
        print("Cell " + str(i) + " = " + str(suMainList[i]))
    else:
        print("Cell " + str(i) + " = " + str(suCellOptions[i]) + "Square: " + str(suCellSquare[i]))
#print(suCellOptions)


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
    return suMainList

