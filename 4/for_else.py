for n in range(10):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, '是质数')

# 等价于
for n in range(10):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, '是质数')
