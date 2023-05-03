
l_test = []

test2 = [5, 6, 7, 8, 9]

test1 = [1, 2, 3, 4]


def change(lst):
    for i in range(len(lst)):
        lst[i] *= 2


change(test1)
print(test1)
