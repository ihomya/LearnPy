x = 50
def func():
    global x
    # 当我们在函数中为 x 进行赋值时，这一改动将影响到我们在主代码块中使用的 x 的值
    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)
