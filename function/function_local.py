x = 50
def func(x):
    print('x is', x)
    x = 2 #此处的x为局部变量
    print('Changed local x to', x)
func(x)
print('x is still', x)
