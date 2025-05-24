a = 0

match a:
    case 0:
        print(0)
    case 1 | 2:
        print(1)
    case _:
        print("other")

## 带有捕获变量的


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

from traitlets import default


class Color(Enum):
    RED = "red"
    YELLOW = "yellow"


color = Color("red")
match color:
    case Color.RED:
        print("red")
    case Color.YELLOW:
        print("yellow")

## 其他

print("==== match list =======")


def match_list(lis):
    match lis:
        case [x, y, *rest] if x == y:
            print(f"first two items are the same,x=y={y}")
            print("rest", rest)
        case [x, y, *_]:
            print(f"first two items are x={x}, y={y}")


match_list([1, 1, 3])
match_list([1, 2, 2, 3])

print("==== match dict =======")


def match_dict(dic):
    match dic:
        case {"x": x, "y": y}:
            print("origin", x, y)
        case {"z": z}:
            print(f"z={z}")


match_dict({"x": 1, "y": 2, "sd": 3})  # 多余的键会被忽略
match_dict({"z": 3})


