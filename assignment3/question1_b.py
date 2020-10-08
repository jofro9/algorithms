def dups(L, i, j):
    return L[i] == L[j]

def checkForUnique(the_list):
    i = 0

    while i < len(the_list) - 1:
        j = i + 1

        while j < len(the_list):

            if dups(the_list, i, j):
                the_list.pop(j)
                print(the_list)

            elif not dups(the_list, i, j):
                j += 1

        i += 1

    return len(the_list)

n = [1, 1, 2, 1, 5, 6, 7, 1, 2, 5, 8, 4, 9, 7, 3, 2, 5, 6, 88, 1, 44, 5, 6, 9, 8, 3, 3, 77, 7, 7, 7, 7, 7, -1, -1]
print(checkForUnique(n))
