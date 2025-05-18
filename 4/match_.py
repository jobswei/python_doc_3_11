a = 0

match a:
    case 0:
        print(0)
    case 1 | 2:
        print(1)
    case _:
        print("other")


class Point:
    __match_args__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)


def where_point(p: Point):
    match p:
        case Point(0, 0):
            print("origin")
        case Point(1, y):
            print(f"y={y}")
        case Point(x, 2):
            print(f"x={x}")
        case Point(x, y) if x == y:
            print(f"x=y={y}")
        case Point(x, y) as p:
            print(f"x={x}, y={y}")
            print(p)


where_point(Point(1, 2))
where_point(Point(8, 8))
where_point(Point(7, 8))

from enum import Enum


class Color(Enum):
    RED = "red"
    YELLOW = "yellow"


color = Color("red")
match color:
    case Color.RED:
        print("red")
    case Color.YELLOW:
        print("yellow")


def f(a, L=[]):
    L.append(a)
    return L


def g(a, L=0):
    L += a
    return L


print(f(1))
print(f(1))
print(g(1))
print(g(1))


def any(x: int, y: int, /, p: int, *, k: int = 1) -> None:
    """any

    Args:
        x (_type_): _description_
        y (_type_): _description_
        p (_type_): _description_
        k (_type_): _description_
    """
    print("doc:", any.__doc__)
    print("ann:", any.__annotations__)


any(1, 2, 3, k=4)
any(1, 2, p=3, k=4)
# any(1, y=2, p=3, k=4) # 报错，y is position only
