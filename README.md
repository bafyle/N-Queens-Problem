# N-Queens-Problem
N Queens problem solving algorithm using backtracking written in Python

## About the problem:
N Queens problem is the problem of placing N chess queens on an NxN chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal.

## About the script:
* This Python script displays all possible solutions for N-size board and their quantity

* You can change the size of the board by passing an integer to the script:
~~~
$ python3 NQueensProblem.py 8
~~~

* If no arguments passed, the sciprt creates a 4x4 board and tries to solve it.
* The script also display how much time did it take to calculate and print the solutions.
* The execution time is started from the moment the algorithm started, not from the beginnig of the script

* Example of the output:
~~~
$ python3 NQueensProblem.py 4
. q . .
. . . q
q . . .
. . q .


. . q .
q . . .
. . . q
. q . .


execution time: 0.0020051002502441406
Found Solutions: 2
~~~
