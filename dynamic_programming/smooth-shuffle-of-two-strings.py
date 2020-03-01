# Problem:

# A shuffle of two strings X and Y is formed by interspersing the characters
# into a new string, keeping the characters of X and Y in the same order.
# For example, the string BANANAANANAS is a shuffle of the strings BANANA and
# ANANAS in several different ways.
# BANANAANANAS BANANAANANAS BANANAANANAS
# Similarly, the strings PRODGYRNAMAMMIINCG and DYPRONGARMAMMICING are
# both shuffles of DYNAMIC and PROGRAMMING:
# PRODGYRNAMAMMIINCG DYPRONGARMAMMICING

# A smooth shuffle of X and Y is a shuffle of X and Y that never uses
# more than two consecutive symbols of either string. For example,
# 126
# Exercises
# • PRDOYGNARAMMMIICNG is a smooth shuffle of the strings DYNAMIC and
# PROGRAMMING.
# • DYPRNOGRAAMMMICING is a shuffle of DYNAMIC and PROGRAMMING, but
# it is not a smooth shuffle (because of the substrings OGR and ING).
# • XXXXXXXXXXXXXXXXXXX is a smooth shuffle of the strings XXXXXXX
# and XXXXXXXXXXX.
# • There is no smooth shuffle of the strings XXXX and XXXXXXXXXXXX.
# Describe and analyze an algorithm to decide, given three strings X, Y ,
# and Z, whether Z is a smooth shuffle of X and Y


# Solution:



def is_smooth_shuffle(a, b, c):
    if len(a) + len(b) != len(c):
        return False
    temp_matrix = [[False for i in range(len(b) + 1)] for j in range(len(a) + 1)]
    temp_matrix[0][0] = True
    i = 1
    while i < len(a) + 1:
        temp_matrix[i][0] = temp_matrix[i - 1][0] and (a[i - 1] == c[i - 1] and (not (a[i - 2] == c[i - 2]
                                                                                      and a[i - 3] == c[
                                                                                          i - 3]) if i > 2 else True))
        i = i + 1
    j = 1
    while j < len(b) + 1:
        temp_matrix[0][j] = temp_matrix[0][j - 1] and (b[j - 1] == c[j - 1] and (not (b[j - 2] == c[j - 2]
                                                                                      and b[j - 3] == c[
                                                                                          j - 3]) if j > 2 else True))
        j = j + 1

    i = 1
    while i < len(a) + 1:
        j = 1
        while j < len(b) + 1:
            temp_matrix[i][j] = (((c[i + j - 1] == a[i - 1])
                                  and (
                                      not (a[i - 2] == c[i + j - 2] and a[i - 3] == c[
                                          i + j - 3]) if i > 2 else True) and
                                  temp_matrix[i - 1][j])
                                 or ((c[i + j - 1] == b[j - 1])
                                     and (not (
                                    b[j - 2] == c[i + j - 2] and b[j - 3] == c[i + j - 3]) if j > 2 else True) and
                                     temp_matrix[i][j - 1]))
            j = j + 1
        i = i + 1

    return temp_matrix[len(a)][len(b)]


if __name__ == '__main__':
    print(is_smooth_shuffle("DYNAMIC", "PROGRAMMING", "PRDOYGNARAMMMIICNG"))
