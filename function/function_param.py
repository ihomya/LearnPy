def print_max(a, b):
    # 此处的参数为形参
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
# 在定义函数时给定的名称称作“形参”（Parameters）
# 在调用函数时你所提供给函数的值称作“实参”（Arguments）。

print_max(3, 4) # 直接传递字面值

x = 5
y = 7
print_max(x, y) # 以参数的形式传递变量,此处的参数为实参

