# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 21:58:55 2021

@authors: GÜVEN ADAL
          BATUHAN BUDAK
          CANKAT ANDAY KADİM
          FURKAN AHİ
          Umut Baştepe
"""
import random
import numpy as np
import PySimpleGUI as sg
import matplotlib.pyplot as plt

from queue import Queue
import sys

# State Class
class PuzzleState(object):
    # Constructor(state)
    def __init__(self, blanklocation1, blanklocation2, array):
        self.coloumn = 4
        self.row = 4
        self.blankLocation = (blanklocation1, blanklocation2)
        self.array = array
        self.parent = None

    # Checks if the given state is goal or not
    def isgoal(self):
        goal = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
        goalState = PuzzleState(3,3,goal)

        if np.array_equal(self.array, goalState.array):
            return True
        else:
            return False

    # Finds the blank space in matrix and returns its location
    def blankfinder(self):
        place = np.where(self.array == 0)
        return place

    # Returns depth of the given state
    def getDepth(self):
        state = self

        depth = 0
        while state.parent is not None:
            depth += 1
            state = state.parent
        return depth


    # Heuristic function ranks alternatives in search algorithm decide which branch to follow
    """Heuristic function is used for understanding how similar a given state is to the goal state. Because each element of the 
array has its distinct place in the goal state each of the elements in a given array(1 to 15) and the blank space which is 
described as 0 in the code is evaluated with its place in the matrix compared to its goal place. For example 1 should be 0,0 indexes 
in the matrix and difference between its current place is calculated and for each 16 elements its added. This heuristic function
gives 0 for the goal state because each elements distance to their desired matrix place is 0 and when they are all added it becomes 0
which holds for the requirment which goal state heristic value is 0. 
"""
    def hfunc(self):
        stateArr = self.array
        y2 = np.where(stateArr == 2)  # goal indexes Checking the index of 2
        y2Row = y2[0]
        y2Col = y2[1]
        len2= (abs(0-y2Row) +abs (1-y2Col))
        y3 = np.where(stateArr == 3)  # goal indexes Checking the index of 3
        y3Row = y3[0]
        y3Col = y3[1]
        len3 = (abs(0 - y3Row)  + abs(2- y3Col) )
        y4 = np.where(stateArr == 4)  # goal indexes Checking the index of 4
        y4Row = y4[0]
        y4Col = y4[1]
        len4=(abs(0 - y4Row)  + abs(3- y4Col) )
        y5 = np.where(stateArr == 5)  # goal indexes Checking the index of 5
        y5Row = y5[0]
        y5Col = y5[1]
        len5= (abs(1 - y5Row)  + abs(0 - y5Col) )
        y6 = np.where(stateArr == 6)  # goal indexes Checking the index of 6
        y6Row = y6[0]
        y6Col = y6[1]
        len6 = (abs(1 - y6Row) + abs(1 - y6Col) )
        y7 = np.where(stateArr == 7)  # goal indexes Checking the index of 7
        y7Row = y7[0]
        y7Col = y7[1]
        len7 = (abs(1 - y7Row)  + abs(2 - y7Col) )
        y8 = np.where(stateArr == 8)  # goal indexes Checking the index of 8
        y8Row = y8[0]
        y8Col = y8[1]
        len8 = (abs(1 - y8Row)  + abs(3- y8Col) )
        y9 = np.where(stateArr == 9)  # goal indexes Checking the index of 9
        y9Row = y9[0]
        y9Col = y9[1]
        len9 = (abs(2 - y9Row)  + abs(0 - y9Col) )
        y10 = np.where(stateArr == 10)  # goal indexes Checking the index of 10
        y10Row = y10[0]
        y10Col = y10[1]
        len10 = (abs(2 - y10Row) +abs (1 - y10Col) )
        y11 = np.where(stateArr == 11)  # goal indexes Checking the index of 11
        y11Row = y11[0]
        y11Col = y11[1]
        len11= (abs(2 - y11Row)  + abs(2 - y11Col) )
        y12 = np.where(stateArr == 12)  # goal indexes Checking the index of 12
        y12Row = y12[0]
        y12Col = y12[1]
        len12 = (abs(2 - y12Row)  + abs(3 - y12Col) )
        y13 = np.where(stateArr == 13)  # goal indexes Checking the index of 13
        y13Row = y13[0]
        y13Col = y13[1]
        len13 = (abs(3 - y13Row) + abs(0 - y13Col))
        y14 = np.where(stateArr == 14)  # goal indexes Checking the index of 14
        y14Row = y14[0]
        y14Col = y14[1]
        len14 = (abs(3 - y14Row) + abs(1 - y14Col))
        y15 = np.where(stateArr == 15)  # goal indexes Checking the index of 15
        y15Row = y15[0]
        y15Col = y15[1]
        len15 = (abs(3 - y15Row) + abs(2 - y15Col))
        y0= np.where(stateArr == 0)  # goal indexes Checking the index of 0
        y0Row = y0[0]
        y0Col = y0[1]
        len0 = (abs(3 - y0Row) + abs(3 - y0Col))
        y1 = np.where(stateArr == 1)  # goal indexes Checking the index of 1
        y1Row = y1[0]
        y1Col = y1[1]
        len1 = (abs(0 - y1Row) + abs(0 - y1Col))

        toReturn = len4 + len3 + len2 + len1+ len5 + len6 + len7 + len8+len9 + len10 + len11 + len12+ len13 + len14 + len15 + len0
        return toReturn[0]  #antisimilarity number which we retrn in the end of our H function. Smaller this number is a state takes less step to solve


    # Successors function returns children of the given state
    def successors(self):
        children = []

        x = self.blankfinder() # x is the location of blank space

        # left
        if (x[1] != 0):  # if blank space is not at left side of the puzzle
            deneme131 = self.array.copy()
            newState = PuzzleState(x[0], x[1], deneme131)
            newState.parent = self

            newState.array[x[0], x[1]] = newState.array[x[0], x[1] - 1]

            newState.array[x[0], x[1] - 1] = 0
            children.append(newState)

        # right
        if (x[1] != 3):  # if blank space is not at right side of the puzzle
            deneme131 = self.array.copy()
            newState = PuzzleState(x[0], x[1], deneme131)
            newState.parent = self


            newState.array[x[0], x[1]] = newState.array[x[0], x[1] + 1]

            newState.array[x[0], x[1] + 1] = 0
            children.append(newState)

        # up
        if (x[0] != 0):  # if blank space is not at up side of the puzzle
            deneme131 = self.array.copy()
            newState = PuzzleState(x[0], x[1], deneme131)
            newState.parent = self

            newState.array[x[0], x[1]] = newState.array[x[0] - 1, x[1]]

            newState.array[x[0] - 1, x[1]] = 0
            children.append(newState)

        # down
        if (x[0] != 3):  # if blank space is not at down side of the puzzle
            deneme131 = self.array.copy()
            newState = PuzzleState(x[0], x[1], deneme131)
            newState.parent = self

            newState.array[x[0], x[1]] = newState.array[x[0] + 1, x[1]]

            newState.array[x[0] + 1, x[1]] = 0

            children.append(newState)

        return children


    # Draw state and its moves
    def drawState(self,window,stepNo,moves):
        # Arranging Locations for steps with respect to step number
        if(stepNo < 8):
            rectangle_x = stepNo*230
            rectangle_y = 25
        elif(stepNo >= 8 and stepNo < 16):
            rectangle_x = 1610 - abs(stepNo -8)*230
            rectangle_y = 200
        elif(stepNo >= 16 and stepNo < 24):
            rectangle_x = (stepNo-16)*230
            rectangle_y = 375
        elif(stepNo >= 24 and stepNo < 32):
            rectangle_x = 1610 - abs(stepNo -24)*230
            rectangle_y = 550
        elif(stepNo >= 32 and stepNo < 40):
            rectangle_x = (stepNo - 32) * 230
            rectangle_y = 725
        else:   # If step no > 40 cannot display so locations are assigned as 1
            rectangle_x = 1
            rectangle_y = 1
        graph = window.Element("graph")

        for i in range(4):
            for j in range(4):
                # Arrange colors to display better
                if(self.array[j][i] == 0):
                    fill_color = "red"
                else:
                    fill_color = "white"

                # Draw squares
                graph.draw_rectangle((rectangle_x + i * 30, rectangle_y + j * 30),
                                     (rectangle_x + (i + 1) * 30, rectangle_y + (j + 1) * 30),
                                     fill_color,
                                     line_color="black")
                if (self.array[j][i] != 0): # If square is not blank the draw number
                    graph.draw_text(int(self.array[j][i]), (rectangle_x + 15 + i * 30, rectangle_y + 15 + j * 30))
                if(not self.isgoal()):  # If self is not goal indicate movement of the next step
                    if(stepNo < 7):
                        graph.DrawImage(filename="arrowRight.png",location=(rectangle_x + 160,rectangle_y + 48))
                        graph.draw_text(moves[stepNo],location=(rectangle_x + 180, rectangle_y + 30))
                        if(stepNo == 0):    # If state is initial write "Initial State" under it
                            graph.draw_text("Initial State",location=(rectangle_x + 60,rectangle_y + 130))
                    elif(stepNo == 7 or stepNo == 15 or stepNo == 23 or stepNo == 31):
                        graph.DrawImage(filename="arrowDown.png",location=(rectangle_x + 48,rectangle_y + 130))
                        graph.draw_text(moves[stepNo], location=(rectangle_x + 85, rectangle_y + 145))
                    elif(stepNo > 7 and stepNo < 16):
                        graph.DrawImage(filename="arrowLeft.png",location=(rectangle_x - 70,rectangle_y + 46))
                        graph.draw_text(moves[stepNo], location=(rectangle_x - 50, rectangle_y + 30))
                    elif(stepNo > 15 and stepNo < 24):
                        graph.DrawImage(filename="arrowRight.png", location=(rectangle_x + 160, rectangle_y + 48))
                        graph.draw_text(moves[stepNo], location=(rectangle_x + 180, rectangle_y + 30))
                    elif(stepNo > 23 and stepNo < 32):
                        graph.DrawImage(filename="arrowLeft.png", location=(rectangle_x - 70, rectangle_y + 46))
                        graph.draw_text(moves[stepNo], location=(rectangle_x - 50, rectangle_y + 30))
                    elif(stepNo > 31 and stepNo < 40):
                        graph.DrawImage(filename="arrowRight.png", location=(rectangle_x + 160, rectangle_y + 48))
                        graph.draw_text(moves[stepNo], location=(rectangle_x + 180, rectangle_y + 30))
                else:   # If state is goal write "GOAL" under it
                    graph.draw_text("GOAL",location=(rectangle_x + 60,rectangle_y + 130))
        return graph

# Shuffles the 4 x 4 matrix randomly to get a random initial state
# randomizer method starts shuffling from goal state thus inital state created at the end
# is 100 % solveable
def puzzleGenerator():
    goal = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    initial_state = PuzzleState(3, 3, goal)  # initial state is defined as goal at first
    x = initial_state.blankfinder()
    b = random.randint(10, 15)
    for i in range(0, b):
        x = initial_state.blankfinder()  # x is the location of blank space in the puzzle
        a = random.randint(1, 4)  # Creates random int "a" to decide where the blank space will go
                                  # 1 is up 2 is down 3 is left 4 is right
        # up
        if a == 1:
            if (x[0] != 0):  # if blank space is not at upside of the puzzle
                initial_state.array[x[0], x[1]] = initial_state.array[x[0] - 1, x[1]]
                initial_state.array[x[0] - 1, x[1]] = 0

        # down
        elif a == 2:
            if (x[0] != 3):  # if blank space is not at downside of the puzzle
                initial_state.array[x] = initial_state.array[x[0] + 1, x[1]]
                initial_state.array[x[0] + 1, x[1]] = 0


        # left
        elif a == 3:
            if (x[1] != 0):  # if blank space is not at leftside of the puzzle
                initial_state.array[x] = initial_state.array[x[0], x[1] - 1]
                initial_state.array[x[0], x[1] - 1] = 0


        # right
        elif a == 4:
            if (x[1] != 3):  # if blank space is not at rightside of the puzzle
                initial_state.array[x] = initial_state.array[x[0], x[1] + 1]
                initial_state.array[x[0], x[1] + 1] = 0
    blankLoc = initial_state.blankfinder()

    initial_state.blankLocation = blankLoc  #Set blank location of shuffled state

    return initial_state  # returns shuffled array which will be used as initial state

# Check if two numpy arrays are equal or not (check their values)
def checkEqual(arr1,arr2):

    for i in range(4):
        for j in range(4):
            if(arr1[i][j] != arr2[i][j]):
                return True;

    return False

# Initialize window with given title
def window_init(title):

    # Initialize layout
    layout = [
        [
            sg.Graph(
                canvas_size=(1850, 950),
                graph_bottom_left=(0, 950),
                graph_top_right=(1850, 0),
                key="graph"
            )
        ]
    ]
    window = sg.Window(title, layout)
    window.Finalize()
    return window

# returns path length (depth) of the given node
def getPathLen(state):
    len = 1
    parent = state.parent
    while parent:
        parent = parent.parent
        len += 1

    return len

# returns state that has min a star score in the given queue
def getMinState(queue):
    min = 10000000
    toReturn = queue[0]
    index = 0

    for i in range (len(queue)):
        if getPathLen(queue[i]) + queue[i].hfunc() < min:
            min = getPathLen((queue[i]))
            toReturn = queue[i]
            index = i

    queue.pop(index)

    return toReturn

# returns index of the node with min depth
def getMinLen(queue):
    min = 100000
    toReturn = 0

    for i in range (len(queue)):
        if getPathLen(queue[i]) < min:
            min = getPathLen((queue[i]))
            toReturn = i

    return toReturn

# returns a star score of the given node
def getAScore(state):
    return getPathLen(state) + state.hfunc()

# A* search algorithm
def a_star(initial_state):
    explored = []   # explored list to keep visited nodes
    queue = []      # queue
    children = []   # childrens
    goalsFound = [] # goalsFound list to keep goals found
    queue.append(initial_state) # append inital state to queue

    while True:
        while queue:    # while queue is not empty
            state = getMinState(queue)  # select node with min A star score

            explored.append(state)  #append node to explored list

            if(state.isgoal()): # if goal return
                goalsFound.append(state)    # append solution to goalsFound list


            if(len(goalsFound) > 0):
                minPathIndex = getMinLen(goalsFound)    # min solutions index
                minPath = goalsFound[minPathIndex].getDepth()   # min solution's length
                for q in queue:
                    if(q.getDepth() >= minPath): # remove nodes from queue which are longer than min solution's length
                        queue.remove(q)

            for child in state.successors():    # get children of the state
                if child not in children:   # if not already in children append
                    children.append(child)

            for child in children:  # loop through children
                check = True
                for exp in explored:
                    if(not checkEqual(exp.array,child.array)):
                        check = False
                if(check):   # if check is true then child is not in explored, append to queue
                    queue.append(child)
                    explored.append(child)
            children.clear()    # clear children list
        minPathIndex = getMinLen(goalsFound)
        shortestPath = goalsFound[minPathIndex]
        return shortestPath # return solution

# Calculates movements and add them into a list
# Calls drawState function in a loop to display solution path
def drawSolution(path,window):
    ok = "null"
    a = []
    for i in range(len(path)):
        if (i > 0):
            c = np.where(path[i - 1].array == 0)
            d = np.where(path[i].array == 0)
            ##right
            if (d[1] > c[1]):
                if (path[i - 1].array[d] == 1):
                    ok = "1 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 2):
                    ok = "2 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 3):
                    ok = "3 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 4):
                    ok = "4 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 5):
                    ok = "5 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 6):
                    ok = "6 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 7):
                    ok = "7 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 8):
                    ok = "8 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 9):
                    ok = "9 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 10):
                    ok = "10 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 11):
                    ok = "11 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 12):
                    ok = "12 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 13):
                    ok = "13 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 14):
                    ok = "14 left"
                    a.append(ok)
                if (path[i - 1].array[d] == 15):
                    ok = "15 left"
                    a.append(ok)

            if (d[1] < c[1]):
                if (path[i - 1].array[d] == 1):
                    ok = "1 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 2):
                    ok = "2 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 3):
                    ok = "3 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 4):
                    ok = "4 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 5):
                    ok = "5 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 6):
                    ok = "6 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 7):
                    ok = "7 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 8):
                    ok = "8 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 9):
                    ok = "9 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 10):
                    ok = "10 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 11):
                    ok = "11 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 12):
                    ok = "12 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 13):
                    ok = "13 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 14):
                    ok = "14 right"
                    a.append(ok)
                if (path[i - 1].array[d] == 15):
                    ok = "15 right"
                    a.append(ok)


            if (d[0] > c[0]):
                if (path[i - 1].array[d] == 1):
                    ok = "1 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 2):
                    ok = "2 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 3):
                    ok = "3 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 4):
                    ok = "4 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 5):
                    ok = "5 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 6):
                    ok = "6 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 7):
                    ok = "7 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 8):
                    ok = "8 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 9):
                    ok = "9 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 10):
                    ok = "10 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 11):
                    ok = "11 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 12):
                    ok = "12 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 13):
                    ok = "13 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 14):
                    ok = "14 up"
                    a.append(ok)
                if (path[i - 1].array[d] == 15):
                    ok = "15 up"
                    a.append(ok)

            if (d[0] < c[0]):
                if (path[i - 1].array[d] == 1):
                    ok = "1 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 2):
                    ok = "2 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 3):
                    ok = "3 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 4):
                    ok = "4 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 5):
                    ok = "5 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 6):
                    ok = "6 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 7):
                    ok = "7 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 8):
                    ok = "8 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 9):
                    ok = "9 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 10):
                    ok = "10 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 11):
                    ok = "11 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 12):
                    ok = "12 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 13):
                    ok = "13 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 14):
                    ok = "14 down"
                    a.append(ok)
                if (path[i - 1].array[d] == 15):
                    ok = "15 down"
                    a.append(ok)

    for i in range(len(path)):
        path[i].drawState(window, i, a)

# ------------------------------MAİN-------------------------------

# Creating 10 distinct states
while True:
    s1 = puzzleGenerator()
    s2 = puzzleGenerator()
    s3 = puzzleGenerator()
    s4 = puzzleGenerator()
    s5 = puzzleGenerator()
    s6 = puzzleGenerator()
    s7 = puzzleGenerator()
    s8 = puzzleGenerator()
    s9 = puzzleGenerator()
    s10 = puzzleGenerator()
    statelist=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
    stateset=set(statelist)
    if not (s1.isgoal() or s2.isgoal() or s3.isgoal() or s4.isgoal() or s5.isgoal() or s6.isgoal() or s7.isgoal() or s8.isgoal() or s9.isgoal() or s10.isgoal()) and(len(statelist) == len(stateset)):
        break
print("-----S1-----")
print(s1.array)
print("------------")
print("-----S2-----")
print(s2.array)
print("------------")
print("-----S3-----")
print(s3.array)
print("------------")
print("-----S4-----")
print(s4.array)
print("------------")
print("-----S5-----")
print(s5.array)
print("------------")
print("-----S6-----")
print(s6.array)
print("------------")
print("-----S7-----")
print(s7.array)
print("------------")
print("-----S8-----")
print(s8.array)
print("------------")
print("-----S9-----")
print(s9.array)
print("------------")
print("-----S10-----")
print(s10.array)
print("------------")


solution1 = a_star(s1)
print("1. solution found")
solution2 = a_star(s2)
print("2. solution found")
solution3 = a_star(s3)
print("3. solution found")
solution4 = a_star(s4)
print("4. solution found")
solution5 = a_star(s5)
print("5. solution found")
solution6 = a_star(s6)
print("6. solution found")
solution7 = a_star(s7)
print("7. solution found")
solution8 = a_star(s8)
print("8. solution found")
solution9 = a_star(s9)
print("9. solution found")
solution10 = a_star(s10)
print("10. solution found")

path1 = list()
path2 = list()
path3 = list()
path4 = list()
path5 = list()
path6 = list()
path7 = list()
path8 = list()
path9 = list()
path10 = list()

# 1
path1.append(solution1)
parent = solution1.parent

while parent:
    path1.append(parent)
    parent = parent.parent
path1.reverse()

# 2
path2.append(solution2)
parent = solution2.parent

while parent:
    path2.append(parent)
    parent = parent.parent
path2.reverse()


# 3
path3.append(solution3)
parent = solution3.parent

while parent:
    path3.append(parent)
    parent = parent.parent
path3.reverse()

# 4
path4.append(solution4)
parent = solution4.parent

while parent:
    path4.append(parent)
    parent = parent.parent
path4.reverse()

# 5
path5.append(solution5)
parent = solution5.parent

while parent:
    path5.append(parent)
    parent = parent.parent
path5.reverse()

# 6
path6.append(solution6)
parent = solution6.parent

while parent:
    path6.append(parent)
    parent = parent.parent
path6.reverse()

# 7
path7.append(solution7)
parent = solution7.parent

while parent:
    path7.append(parent)
    parent = parent.parent
path7.reverse()

# 8
path8.append(solution8)
parent = solution8.parent

while parent:
    path8.append(parent)
    parent = parent.parent
path8.reverse()

# 9
path9.append(solution9)
parent = solution9.parent

while parent:
    path9.append(parent)
    parent = parent.parent
path9.reverse()

# 10
path10.append(solution10)
parent = solution10.parent

while parent:
    path10.append(parent)
    parent = parent.parent
path10.reverse()


window1 = window_init("Sym-15 Puzzle, Hw4, S1")  # To display solution of S1
window2 = window_init("Sym-15 Puzzle, Hw4, S2")  # To display solution of S2


drawSolution(path1,window1)  # Draw solution for S1

drawSolution(path2,window2)  # Draw solution for S2



window1.read()
window2.read()


# plotting a bar chart
left = [1,2,3,4,5,6,7,8,9,10]


    # heights of bars
height = [len(path1),len(path2),len(path3),len(path4),len(path5),len(path6),len(path7),len(path8),len(path9),len(path10)]
plt.bar(left, height, tick_label=left,
            width=0.8, color=['red', 'green'])
plt.xticks(rotation=90)

    # naming the x-axis
plt.xlabel('x - axis')
    # naming the y-axis
plt.ylabel('y - axis')
plt.legend()
    # plot title
plt.title('STEP COUNT vs. INITIAL STEPS')

    # function to show the plot
plt.show()


