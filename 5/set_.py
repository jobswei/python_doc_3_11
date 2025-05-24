# set 里面可以放迭代类型
a = set('abracadabra')
print(a)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

a = {"a": 1, "b": 2}
lis = list(a.keys())
lis = list(a)  # 直接返回键的列表
sorted_lis = sorted(a)

b = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)
