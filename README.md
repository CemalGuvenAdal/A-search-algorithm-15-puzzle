# A-search-algorithm-15-puzzle
blankfinder() function is used for finding the index of the blank space in the puzzle
getDepth() returns the depth of the given state.
isgoal() function is used to test if the current state is the goal state.
successors() function finds and returns the childrens of the state.
drawState() function draws the steps and the moves taken for that step in GUI.
puzzleGenerator() function randomize the goal state by random number of times to create a
random puzzle initial state.
a_star() function implements the A* algorithm.
CS 461 Homework 4
1.04..2021
getpathlen() function calculates the length of the path taken..
drawSolution() function calls the draw state function in a loop to display solution path.
hfunc() function is used for understanding how similar a given state is to the goal state.
Because each element of the array has its distinct place in the goal state each of the elements
in a given array(1 to 15) and the blank space which is described as 0 in the code is evaluated
with its place in the matrix compared to its goal place. For example 1 should be 0,0 indexes
in the matrix and difference between its current place is calculated and for each 16 elements
its added.
