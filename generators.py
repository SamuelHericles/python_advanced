"""
    Returns the object and used to create iterators.
"""

# Seq 1 to 9.000.000
import sys


def mygenerator(n):
    for x in range(n):
        yield x ** 3


# Usually this function run up to 9kk, but not, yield keywords its lazy.
values = mygenerator(9000000)
# print(next(values))  # 0
# print(next(values))  # 1
# print(next(values))  # 8
# print(next(values))  # 27
# print(next(values))  # 64
# print(next(values))  # 125

print(sys.getsizeof(values))

values = mygenerator(100)
# for x in values:
#     print(x)

# Not increase size variables
# print(sys.getsizeof(values))
del values

# -------------------------------


def infinite_sequece():
    result = 1
    while True:
        yield result
        result *= 5


values = mygenerator(9000000)
print(next(values))  # 1
print(next(values))  # 5
print(next(values))  # 25
print(next(values))  # 125
print(next(values))  # 625
print(next(values))  # 3125
print(sys.getsizeof(values))

values = mygenerator(9000000)

# diff the last loop because while its true
# for x in values:
#     print(x)
