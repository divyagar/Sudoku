# importing important libraries
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import copy
import random

def func1():
    pass

def func2():
    pass

def func3():
    pass

#---------algorithm that will solve sudoku----------------------------------
done = False
def sudoku(row, col):
    global done, ansMatrix
    if(col == 9):
        sudoku(row+1, 0)
        return
    if(ansMatrix[row][col] == 0):
        for i in range(1, 10):
            if(valid(row, col, i, ansMatrix)):
                ansMatrix[row][col] = i
                if((row == 8) and (col == 8)):
                    done = True
                    return
                sudoku(row, col+1)
                if(done):
                    return

        ansMatrix[row][col] = 0
        return

    else:
        if(row == 8 and col == 8):
            done = True
            return
        sudoku(row, col+1)

#------------function that will check whether a value is valid at a certain place or not-------------------------
def valid(row, col, k, matrix):
    for i in range(9):
        if matrix[i][col] == k:
            return False
        if matrix[row][i] == k:
            return False
    startingRow = row // 3
    startingCol = col // 3
    for i in range(startingRow*3, (startingRow+1) * 3):
        for j in range(startingCol*3, (startingCol+1) * 3):
            if(matrix[i][j] == k):
                return False

    return True


#--------------function that will check whether a value is valid or not whenever user will enter value in a certain cell-------------
def keyPressed(event):
    widget = event.widget
    widgetRow = widget.grid_info()['row']
    widgetCol = widget.grid_info()['column']
    parentFrame = widget.master
    parentRow = parentFrame.grid_info()['row']
    parentCol = parentFrame.grid_info()['column']
    row = (parentRow * 3) + widgetRow
    col = (parentCol * 3) + widgetCol
    value = widget.get()
    if(len(value) > 1):
        messagebox.showerror("Invalid value", "Value can be between 0 and 9 only")
        return
    if(value != ''):
        value = int(value)
        userMatrix[row][col] = value
        #---if value entered is correct, change its color to green, else to red---------
        if(userMatrix[row][col] == ansMatrix[row][col]):
            widget.config(foreground = "green")
        else:
            widget.config(foreground = "red")

    else:
        userMatrix[row][col] = 0

    #-----if user has completed sudoku---------
    if(checkComplete()):
        checkSudoku()


#----------------function to check if user has completed matrix----------------
def checkComplete():
    for i in range(9):
        if(0 in userMatrix[i]):
            return False

    return True

#----------------check whether the answer is correct or not---------------
def checkSudoku():
    if(str(ansMatrix) == str(userMatrix)):
        messagebox.showinfo("Result", "Congratulations! You solved sudoku correctly")


#----------------creating list of various sudokus-----------------------------
sudokuList = []
sudokuList.append([[0,1,0,0,4,0,0,5,0],
                   [4,0,7,0,0,0,6,0,2],
                   [8,2,0,6,0,0,0,7,4],
                   [0,0,0,0,1,0,5,0,0],
                   [5,0,0,0,0,0,0,0,3],
                   [0,0,4,0,5,0,0,0,0],
                   [9,6,0,0,0,3,0,4,5],
                   [3,0,5,0,0,0,8,0,1],
                   [0,7,0,0,2,0,0,3,0]])

sudokuList.append([[0,0,0,0,5,1,0,9,0],
                   [0,2,4,3,0,8,0,0,0],
                   [0,0,3,0,7,0,6,0,0],
                   [6,0,0,0,0,0,5,4,0],
                   [8,1,0,0,0,7,0,0,0],
                   [0,0,9,0,0,2,0,0,0],
                   [0,0,6,4,0,0,7,0,8],
                   [3,0,0,0,0,0,0,0,4],
                   [5,0,0,1,0,9,0,2,0]])

sudokuList.append([[5,3,0,0,7,0,0,0,0],
                   [6,0,0,1,9,5,0,0,0],
                   [0,9,8,0,0,0,0,6,0],
                   [8,0,0,0,6,0,0,0,3],
                   [4,0,0,8,0,3,0,0,1],
                   [7,0,0,0,2,0,0,0,6],
                   [0,6,0,0,0,0,2,8,0],
                   [0,0,0,4,1,9,0,0,5],
                   [0,0,0,0,8,0,0,7,9]])

sudokuList.append([[6,0,0,0,0,3,0,0,5],
                   [9,0,3,0,8,0,0,0,0],
                   [0,5,1,0,0,0,6,0,0],
                   [0,0,0,4,3,0,0,0,7],
                   [0,0,8,5,0,7,1,0,0],
                   [4,0,0,0,6,8,0,0,0],
                   [0,0,7,0,0,0,9,8,0],
                   [0,0,0,0,7,0,4,0,2],
                   [8,0,0,3,0,0,0,0,6]])

sudokuList.append([[0,0,0,0,0,4,0,9,0],
                   [8,0,2,9,7,0,0,0,0],
                   [9,0,1,2,0,0,3,0,0],
                   [0,0,0,0,4,9,1,5,7],
                   [0,1,3,0,5,0,9,2,0],
                   [5,7,9,1,2,0,0,0,0],
                   [0,0,7,0,0,2,6,0,3],
                   [0,0,0,0,3,8,2,0,5],
                   [0,2,0,5,0,0,0,0,0]])

# Sudoku to be solved---------------------------------------------------------
alreadyDone = []
sudokuMatrix = NONE
ansMatrix = NONE
userMatrix = NONE

def getRandomMatrix():
    global alreadyDone, sudokuMatrix, ansMatrix, userMatrix, done
    randomNo = random.randint(0, 4)
    if(len(alreadyDone) == len(sudokuList)):
        alreadyDone = []

    while randomNo in alreadyDone:
        randomNo = random.randint(0, 4)

    sudokuMatrix = sudokuList[randomNo]
    alreadyDone.append(randomNo)
    ansMatrix = copy.deepcopy(sudokuMatrix)  # to save answer
    userMatrix = copy.deepcopy(sudokuMatrix)  # to save values entered by user
    # print(ansMatrix)
    sudoku(0, 0)
    done = False
    print(ansMatrix)

getRandomMatrix()

#----------------button functions------------------------------------
def resetIt():
    createSudoku()

def Change():
    getRandomMatrix()
    createSudoku()

#--------------------------Creating GUI----------------------------------
root = Tk()

def createSudoku():
    subframes = [] # list of subframes

    #---------creating 9 subframes--------------
    for i in range(3):
        row = []
        for j in range(3):
            row.append(LabelFrame(root, borderwidth = 1, relief = SOLID, highlightcolor = "red"))
        subframes.append(row)

    for i in range(3):
        for j in range(3):
            subframes[i][j].grid(row = i, column = j)

    ttk.Style().configure('pad.TEntry', padding = '15 8 15 8')

    #---------creating each cell of sudoku------------------
    for i in range(9):
        for j in range(9):
            subFrameRow = i//3
            subFrameCol = j//3

            if(sudokuMatrix[i][j] == 0):
                widget = ttk.Entry(subframes[subFrameRow][subFrameCol], width=1,font = "helvetica 15", justify='center', style='pad.TEntry')
            else:
                widget = Label(subframes[subFrameRow][subFrameCol], text = sudokuMatrix[i][j], padx = 15, pady = 8, borderwidth = 1, relief = SOLID, bg = "#ddd", font = "helvetica 15")
            relativeRow = (i - (3 * subFrameRow))
            relativeCol = (j - (3 * subFrameCol))
            widget.grid(row = relativeRow, column = relativeCol)
            widget.bind('<KeyRelease>', keyPressed)

createSudoku()
#------------creating buttons-----------------------

reset = Button(root, text = "Reset", command = resetIt, padx = 20, pady = 10)
reset.grid(row = 3, column = 0, padx = 60, pady = 10, columnspan = 2)

another = Button(root, text = "Change", command = Change, padx = 20, pady = 10)
another.grid(row = 3, column = 1, padx = 30, pady = 10, columnspan = 2)


#------running GUI------------
root.mainloop()





