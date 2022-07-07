# N-Queens-Problem
N Queens problem generator using backtracking technique written in Python

## About the problem:
N Queens problem is the problem of placing N chess queens on an NxN chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal.

## About the script:
* This Python script displays all possible solutions for N-size board. It has two optional arguments:
~~~ 
    -s, --size      # Specify the board size, default size is 4
    -f, --file      # Tell the script to save all solutions to a text file
    -c, --console   # Print all solutions to the console
~~~


* If the size argument isn't passed, the script creates a 4x4 board and generate all possible solutions for it.
* The script also displays how much time it took calculating all solutions.

* Example of the output:
~~~
$ python3 NQueensProblem.py -s 4 -c
Execution time: 0.0002091000000000176
Found Solutions: 2
Printing solutions...
. q . .
. . . q
q . . .
. . q .

. . q .
q . . .
. . . q
. q . .

Done

~~~
