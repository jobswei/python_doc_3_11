# 比较运算
# 比较运算符 in 和 not in (成员检测)，
# is 和 is not 用于比较两个对象是否是同一个对象。
# 所有比较运算符的优先级都一样，且低于任何数值运算符
# 支持链式操作。例如，a < b == c 校验 a 是否小于 b，且 b 是否等于 c。
# 比较操作可以用布尔运算符 and 和 or 组合，用not取反
# 这些操作符的优先级低于比较操作符，且not 的优先级最高， or 的优先级最低
# A and not B or C 等价于 (A and (not B)) or C

# 短路 运算符 and 和 or
# 从左到右，如果遇到一个满足，则不会对后面的求值
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)  # 返回最后一个求了值的参数
