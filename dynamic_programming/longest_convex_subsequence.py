# Problem:

# A sequence X[1..m] of integers is said to be convex if X[i+1] - X[i] > X[i] - X[i-1] for every integer i between 2 and m-1. Thus, the sequence [0, 1, 3, 7, 12, 20] is convex, and so is [5, 3, 2, 2, 4, 8]. On the other hand, [0, 3, 7, 8, 13] is not convex because 8 - 7 < 7 - 3.
#
# Note that a sequence with 0, 1, or 2 integers is convex by definition. Here is another way of thinking about convex sequences. Given X[1..m], define Y[2..m] by letting Y[i] = X[i] - X[i-1]. Thus, Y is the sequence consisting of differences between successive terms of X. The sequence X is convex if and only if the sequence Y is increasing.
#
# The name convex comes from the fact that is we plot the points (i, X[i]) in the plane, one gets a convex shape.
#
# The algorithmic problem we wish to solve is this. We are given as input a sequence A[1..n] of non-negative integers, and we wish to find a longest convex subsequence of A. For example, if A = [0, 3, 7, 8, 13], then a longest convex subsequence is [0, 3, 7, 13].


# Solution:

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


if __name__ == '__main__':

    input_file = input("Enter name of the input file: ")
    integers = read_integers(filename=input_file)
    total_integers = integers[0]
    integers_list = integers[1:total_integers+1]
    if validate_length(total_integers, integers_list):
        print("File contents are valid")
    else:
        print("Total number of integers are not according to size mentioned in first line of file")

