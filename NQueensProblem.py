import sys
import time

def printMap(map: list):
    """ Custom function for printing the board """
    for row in map:
        print(row)
    print()

def createMap(dimension: int) -> list:
    """
    Returning a 2D list full of dots
    """
    map = list()
    for _ in range(dimension):
        innerList = ['.' for f in range(dimension)]
        map.append(innerList)
    return map

def suitable(row : int, col: int, map: list):

    """
    This function checks if a position is suitable to put a queen
    in it or not
    """

    # check row for queens
    ithRow = map[row]
    if 'q' in ithRow:
        return False
    
    # check column for queens
    ithCol = [map[i][col] for i in range(len(map))]
    if 'q' in ithCol:
        return False

    # check diagonal for queens
    tempRow = row - min(row, col)
    tempCol = col - min(row, col)
    diagonal1 = list()
    while tempRow < len(map) and tempCol < len(map):
        diagonal1.append(map[tempRow][tempCol])
        tempRow += 1
        tempCol += 1
    if 'q' in diagonal1:
        return False
    
    diagonal2 = list()
    tempRow = row
    tempCol = col
    while tempRow != 0 and tempCol != len(map) - 1:
        tempCol += 1
        tempRow -= 1
    while tempRow < len(map) and tempCol > -1:
        diagonal2.append(map[tempRow][tempCol])
        tempRow += 1
        tempCol -= 1
    if 'q' in diagonal2:
        return False
    
    # if no queen detected, then it's a suitable place
    return True

def backtrack(map: list, rowNumber: int, colNumber: int, mapSize: int):
    """
    This function takes the board, row, column and the size of the board
    and it returns the nearest possible position to start again from
    """
    rowNumber -= 1
    colNumber = map[rowNumber].index('q')
    map[rowNumber][colNumber] = '.'
    if colNumber == mapSize - 1:
        rowNumber -= 1
        if rowNumber == -1:
            return -1, -1
        colNumber = map[rowNumber].index('q')
        map[rowNumber][colNumber] = '.'
    colNumber += 1
    return rowNumber, colNumber


def main(args):
    try:
        mapSize = int(args[1])
    except ValueError:
        print("Passed argument must be an integer")
        quit(1)
    except IndexError:
        mapSize = 4
        print("No arguments passed, using the default size which is 4....")

    numpyExist = False
    try:
        import numpy as np
        numpyExist = True
    except ImportError:
        pass
    foundSolutions = 0
    queens = mapSize
    map = createMap(mapSize)
    
    rowNumber = 0
    colNumber = 0
    startTime = time.time()
    while True:
        if suitable(row=rowNumber, col=colNumber, map=map):
            map[rowNumber][colNumber] = 'q'
            rowNumber += 1
            colNumber = 0
        elif colNumber != mapSize - 1:
            colNumber += 1
        else:
            rowNumber, colNumber = backtrack(map, rowNumber, colNumber, mapSize)
        if rowNumber >= mapSize:
            if numpyExist:
                print(np.matrix(map), end='\n\n')
            else:
                printMap(map)
            rowNumber, colNumber = backtrack(map, rowNumber, colNumber, mapSize)
            foundSolutions += 1
        if rowNumber < 0:
            break
    endTime = time.time()
    if foundSolutions:
        print(f"execution time: {endTime- startTime}")
    print(f"Found Solutions: {foundSolutions}")

if __name__ == "__main__": # if the file is not imported
    main(sys.argv) # run the main function and pass the arguments 
