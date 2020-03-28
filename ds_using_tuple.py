# 我会推荐你总是使用括号
# 来指明元组的开始与结束
# 尽管括号是一个可选选项。
# 明了胜过晦涩，显式优于隐式。
zoo = ('python', 'elephant', 'penguin')
# 元组用于将多个对象保存到一起
# 它是不可变
# 它同时也是一个序列
print('Number of animals in the zoo is', len(zoo))
# 元组是通过特别指定项目来定义的
# 在指定项目时，你可以给它们加上括号，并在括号内部用逗号进行分隔。
# 元组通常用于保证某一语句或某一用户定义的函数可以安全地采用一组数值
# 意即元组内的数值不会改变。
new_zoo = 'monkey', 'camel', zoo
# 元组中所包含的元组不会失去其所拥有的身份。
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))
# 一个空的元组由一对圆括号构成，就像 myempty = ()
# 一个只拥有一个项目的元组，你必须在第一个（也是唯一一个）项目的后面加上一个逗号来指定它
# 比如 singleton = (2, )
