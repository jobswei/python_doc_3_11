## 函数的定义
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
"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
"""


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
