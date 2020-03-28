age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name,age))
print('Why is {0} playing with that python?'.format(name))
# format函数是将变量按序逐一带入字符串中{}的位置，从而达到格式化字符的效果
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
# {}中的数字是可以选的
print('{0:.3f}'.format(1.0/3)) # 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:_^11}'.format('hello'))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('abc',end='')
print('efg',end='')
# end可以指定字符串以特定字符结尾，字符串默认以新一行结尾，即\n
