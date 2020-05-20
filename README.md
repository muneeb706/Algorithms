# Algorithms
Contains implementation of solution in [python](https://www.python.org/) for different types of classic algorithm problems.

Following is description of the programming problems:

- ## Dynamic Programming Problems

  - ## Longest Convex Subsequence
    A program for finding longest convex subsequence in the given array.
    
    A sequence X[1..m] of integers is said to be convex
    if X[i+1] - X[i] > X[i] - X[i-1] for every integer i between 2 and m-1.
    Thus, the sequence [0, 1, 3, 7, 12, 20] is convex, and so is [5, 3, 2, 2, 4, 8].
    On the other hand, [0, 3, 7, 8, 13] is not convex because 8 - 7 < 7 - 3.
    Note that a sequence with 0, 1, or 2 integers is convex by definition.
    Here is another way of thinking about convex sequences.
    Given X[1..m], define Y[2..m] by letting Y[i] = X[i] - X[i-1].
    Thus, Y is the sequence consisting of differences between successive terms of X.
    The sequence X is convex if and only if the sequence Y is increasing.
    The name convex comes from the fact that is we plot the points (i, X[i]) in the plane, one gets a convex shape. 
    The algorithmic problem we wish to solve is this. We are given as input a sequence A[1..n] of non-negative integers,
    and we wish to find a longest convex subsequence of A.
    For example, if A = [0, 3, 7, 8, 13], then a longest convex subsequence is [0, 3, 7, 13].
    
    [Program](https://github.com/muneeb706/Algorithms/blob/master/dynamic_programming/longest_convex_subsequence.py)
    
  - ## Play Card Game
    You and your eight-year-old nephew Elmo decide to play a simple card
    game. At the beginning of the game, the cards are dealt face up in a long
    row. Each card is worth a different number of points. After all the cards are
    dealt, you and Elmo take turns removing either the leftmost or rightmost
    card from the row, until all the cards are gone. At each turn, you can decide
    which of the two cards to take. The winner of the game is the player that
    has collected the most points when the game ends.
    Having never taken an algorithms class, Elmo follows the obvious greedy
    strategy—when it’s his turn, Elmo always takes the card with the higher
    point value. Your task is to find a strategy that will beat Elmo whenever
    possible. (It might seem mean to beat up on a little kid like this, but Elmo
    absolutely hates it when grown-ups let him win.)

    Given the initial sequence
    of cards, This program determines the maximum number of points that you can collect
    playing against Elmo.
    
    [Program](https://github.com/muneeb706/Algorithms/blob/master/dynamic_programming/play-card-game.py)
  
  - ## Smooth Shuffle of Two Strings
    A program that determines whether Z is a smooth shuffle of X and Y. Three strings X, Y ,
    and Z are given as input to the program.
    
    Shuffle of two strings X and Y is formed by interspersing the characters
    into a new string, keeping the characters of X and Y in the same order.
    For example, the string BANANAANANAS is a shuffle of the strings BANANA and
    ANANAS in several different ways.
    BANANAANANAS BANANAANANAS BANANAANANAS
    Similarly, the strings PRODGYRNAMAMMIINCG and DYPRONGARMAMMICING are
    both shuffles of DYNAMIC and PROGRAMMING:
    PRODGYRNAMAMMIINCG DYPRONGARMAMMICING

    A smooth shuffle of X and Y is a shuffle of X and Y that never uses
    more than two consecutive symbols of either string. For example,
    PRDOYGNARAMMMIICNG is a smooth shuffle of the strings DYNAMIC and
    PROGRAMMING.
    DYPRNOGRAAMMMICING is a shuffle of DYNAMIC and PROGRAMMING, but
    
    [Program](https://github.com/muneeb706/Algorithms/blob/master/dynamic_programming/smooth-shuffle-of-two-strings.py)

- ## Graph Problems
  - ## Maze Solver
    Program for solving an input number maze. A number maze M[1..n, 1..n] is an n by n grid of non-negative integers.
    A token is initially placed in the upper left corner, on the square (1,1).
    We want to move it to the lower right corner,
    the square (n,n), using a minimum number of moves.
    If the token is on square (i,j), then in a single move,
    we can move it up, down, left, or right, by M[i,j] squares.
    (Of course, any such move is valid only if we stay within the grid.)
    Note that in this assignment we allow M[i,j] to be 0;
    if the token reaches such a square (i,j), it cannot move any further.
    Assume that the input number maze is specified in a file whose first line specifies n,
    the length of the grid.
    The next n*n likes specify the entries of the maze M row by row -- so the first n of these lines specify M[1,1..n],
    the next n lines specify M[2,1..n], and so on. #
    Program reads the input file that contains the input number maze M in the above format,
    and outputs the minimum number of moves required to solve the maze.
    
    [Program](https://github.com/muneeb706/Algorithms/blob/master/graph/maze-solver.py)
