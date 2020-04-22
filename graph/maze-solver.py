
# Program for solving an input number maze. A number maze M[1..n, 1..n] is an n by n grid of non-negative integers.
# A token is initially placed in the upper left corner, on the square (1,1).
# We want to move it to the lower right corner,
# the square (n,n), using a minimum number of moves.
# If the token is on square (i,j), then in a single move,
# we can move it up, down, left, or right, by M[i,j] squares.
# (Of course, any such move is valid only if we stay within the grid.)
# Note that in this assignment we allow M[i,j] to be 0;
# if the token reaches such a square (i,j), it cannot move any further.
# Assume that the input number maze is specified in a file whose first line specifies n,
# the length of the grid.
# The next n*n likes specify the entries of the maze M row by row -- so the first n of these lines specify M[1,1..n],
# the next n lines specify M[2,1..n], and so on. #
# Program reads the input file that contains the input number maze M in the above format,
# and outputs the minimum number of moves required to solve the maze.

import time
from queue import Queue


# checks whether given position is out of bounds or not
# and it is already visited or not
def is_valid_move(maze, visited, row_no, col_no):
    if 0 <= row_no < len(maze) \
            and 0 <= col_no < len(maze)\
            and not visited[row_no][col_no]:
        return True
    return False


# function to find shortest path from source to destination with the help of
# breadth first traversal of the graph
def bfs(maze, source_x, source_y, dest_x, dest_y):

    # array to keep track of visited cells in maze
    visited = [[False for i in range(len(maze))] for j in range(len(maze))]
    q = Queue()

    visited[source_x][source_y] = True

    # node to store cell properties
    # x is the row number of cell
    # y is the column number of cell
    # val is the value of the current cell
    # min_dist is the minimum path / moves from source to cell
    node = {'x': source_x, 'y': source_y, 'val': maze[source_x][source_y],
            'min_dist': 0}
    q.put(node)

    # minimum moves required to go from source to destination
    min_moves = float("inf")

    while not q.empty():

        node = q.get()

        curr_x = node['x']
        curr_y = node['y']

        dist = node['min_dist']

        if curr_x == dest_x and curr_y == dest_y:
            min_moves = dist
            break

        curr_value = maze[curr_x][curr_y]

        if curr_value >= 0:

            # pushing all the cells in queue
            # that can be reached from current cell

            # move left
            new_x = curr_x
            new_y = curr_y - curr_value
            if is_valid_move(maze, visited, new_x, new_y):
                visited[new_x][new_y] = True
                node = {'x': new_x, 'y': new_y,
                        'val': maze[new_x][new_y],
                        'min_dist': dist + 1}
                q.put(node)

            # move right
            new_x = curr_x
            new_y = curr_y + curr_value
            if is_valid_move(maze, visited, new_x, new_y):
                visited[new_x][new_y] = True
                node = {'x': new_x, 'y': new_y,
                        'val': maze[new_x][new_y],
                        'min_dist': dist + 1}
                q.put(node)

            # move up
            new_x = curr_x - curr_value
            new_y = curr_y
            if is_valid_move(maze, visited, new_x, new_y):
                visited[new_x][new_y] = True
                node = {'x': new_x, 'y': new_y,
                        'val': maze[new_x][new_y],
                        'min_dist': dist + 1}
                q.put(node)

            # move down
            new_x = curr_x + curr_value
            new_y = curr_y
            if is_valid_move(maze, visited, new_x, new_y):
                visited[new_x][new_y] = True
                node = {'x': new_x, 'y': new_y,
                        'val': maze[new_x][new_y],
                        'min_dist': dist + 1}
                q.put(node)

    return min_moves


# reads maze from the input file
def read_maze(input_file):
    lines = []
    with open(input_file) as file:
        lines = [line.strip() for line in file]

    if '' in lines:
        lines.remove('')

    maze_size = 0
    maze = []
    temp = []
    for i in range(0, len(lines)):
        if i == 0:
            maze_size = int(lines[i])
        else:
            temp.append(int(lines[i]))
            if i % maze_size == 0:
                maze.append(temp)
                temp = []

    return maze, maze_size


if __name__ == '__main__':

    input_file = input("Enter path to input file: ")

    start_time = time.time()


    maze, maze_size = read_maze(input_file)
    min_moves = bfs(maze, 0, 0, maze_size - 1, maze_size - 1)
    if min_moves != float("inf"):
        print("Minimum number of moves: " + str(min_moves))
    else:
        print("Destination can't be reached from given source")

    end_time = time.time()
    elapsed_time = float((end_time - start_time) * 1000)
    print("Total time taken (milliseconds) : " + str(elapsed_time))
