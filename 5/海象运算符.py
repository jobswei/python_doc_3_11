# https://peps.python.org/pep-0572/

lis = [3, 2, 2]
if (a := lis[0]) != 1:
    print(a)
if a := lis[0] != 1:
    print(a)


def f(x):
    return x + 1


lis = [y := f(1), y**2, y**3]
print(lis)
lis2 = [[y := f(x), y**2, y**3] for x in range(3)]
print(lis2)

# 不可直接用于赋值
# y := f(x)  # INVALID
# (y := f(x))  # Valid, though not recommended
