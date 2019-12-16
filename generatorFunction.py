def gen():
    yield 1
    yield 2
    yield 3
x=gen()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
print(next(x))