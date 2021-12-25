# N-Queens-Problem
N Queens problem generator using backtracking technique written in Python

## About the problem:
N Queens problem is the problem of placing N chess queens on an NxN chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal.

## About the script:
* This Python script displays all possible solutions for N-size board.

* You can change the size of the board by passing an integer to the script:
~~~
$ python3 NQueensProblem.py 8
~~~

* If no arguments are passed, the script creates a 4x4 board and generate all possible solutions to it.
* The script also displays how much time it took to calculate all solutions.

* Example of the output:
~~~
$ python3 NQueensProblem.py 4
INFO:root:Execution time: 0.004106900000000024
INFO:root:Found Solutions: 2
. q . .
. . . q
q . . .
. . q .


. . q .
q . . .
. . . q
. q . .

~~~
