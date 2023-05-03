

def even_n(max_n):
    n = 1
    while n <= max_n:
        yield n*2
        n += 1


i = even_n(11)
# print(i.__next__())
# print(next(i))
# print(next(i))
# print(next(i))
# print(i.__next__())
j = iter(i)
print(j)
