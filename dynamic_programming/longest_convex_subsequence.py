import datetime


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
                m[i][j] = 2 if integer_list[i] < integer_list[j] else 1
                k = j + 1
                while k < len(integer_list):
                    if integer_list[i] + integer_list[k] > 2*integer_list[j]:
                        m[i][j] = max(m[i][j], 1 + m[j][k])
                    k += 1
                j -= 1
            i -= 1
        return m[0][1]
    else:
        return len(integer_list)


if __name__ == '__main__':

    print("Enter 'exit' to terminate the program.")
    input_file = input("Enter name of the input file: ")
    while input_file != "exit":
        integers = read_integers(filename=input_file)
        if len(integers) > 0:
            total_integers = integers[0]
            integer_list = integers[1:total_integers+1]
            if validate_length(total_integers, integer_list):
                start_time = datetime.datetime.now().microsecond
                print("Length of longest convex subsequence ( " + input_file + " ) : " + str(
                    get_longest_convex_subsequence_length(integer_list)))
                end_time = datetime.datetime.now().microsecond
                elapsed_time_millis = (end_time - start_time) / 1000
                print("Execution time in miliseconds: " + str(elapsed_time_millis))
            else:
                print("Total number of integers are not according to size mentioned in first line of file")

        print("Enter 'exit' to terminate the program.")
        input_file = input("Enter name of the input file: ")


