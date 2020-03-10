import time

# Problem:

# A sequence X[1..m] of integers is said to be convex
# if X[i+1] - X[i] > X[i] - X[i-1] for every integer i between 2 and m-1.
# Thus, the sequence [0, 1, 3, 7, 12, 20] is convex, and so is [5, 3, 2, 2, 4, 8].
# On the other hand, [0, 3, 7, 8, 13] is not convex because 8 - 7 < 7 - 3.
# Note that a sequence with 0, 1, or 2 integers is convex by definition.
# Here is another way of thinking about convex sequences.
# Given X[1..m], define Y[2..m] by letting Y[i] = X[i] - X[i-1].
# Thus, Y is the sequence consisting of differences between successive terms of X.
# The sequence X is convex if and only if the sequence Y is increasing.
# The name convex comes from the fact that is we plot the points (i, X[i]) in the plane, one gets a convex shape.
# The algorithmic problem we wish to solve is this. We are given as input a sequence A[1..n] of non-negative integers,
# and we wish to find a longest convex subsequence of A.
# For example, if A = [0, 3, 7, 8, 13], then a longest convex subsequence is [0, 3, 7, 13].

# Solution:
# Running time of following solution is O (n^3)


def read_integers(filename):
    try:
        with open(filename) as f:
            return [int(x) for x in f]
    except FileNotFoundError as e:
        print("Invalid input file name")
        return []


def validate_length(length, integer_list):
    if len(integer_list) == length:
        return True
    return False


def get_longest_convex_subsequence_length(integer_list):

    if len(integer_list) > 1:
        m = [[0 for i in range(len(integer_list))] for j in range(len(integer_list))]
        i = len(integer_list) - 2
        while i >= 0:
            j = len(integer_list) - 1
            while j >= i + 1:
                m[i][j] = 2
                k = j + 1
                while k < len(integer_list):
                    if integer_list[k] - integer_list[j] > integer_list[j] - integer_list[i]:
                        m[i][j] = max(m[i][j], 1 + m[j][k])
                    k += 1
                j -= 1
            i -= 1
        return m[0][1]
    else:
        return len(integer_list)


if __name__ == '__main__':

    print("Enter 'exit' to terminate the program.")
    input_file = input("Enter path of the input file (relative to program file location): ")
    while input_file != "exit":
        integers = read_integers(filename=input_file)
        if len(integers) > 0:
            total_integers = integers[0]
            integer_list = integers[1:total_integers+1]
            if validate_length(total_integers, integer_list):
                start_time = float(round(time.time()*1000))
                print("Length of longest convex subsequence ( " + input_file + " ) : " + str(
                    get_longest_convex_subsequence_length(integer_list)))
                end_time = float(round(time.time()*1000))
                elapsed_time_millis = (end_time - start_time)
                print("Execution time in milliseconds: " + str(elapsed_time_millis))
            else:
                print("Total number of integers are not according to size mentioned in first line of file")

        print("Enter 'exit' to terminate the program.")
        input_file = input("Enter name of the input file: ")