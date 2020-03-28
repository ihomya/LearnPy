import sys
# 导入模块流程 模块->字节码.pyc->二进制
from math import sqrt
# 尽量避免使用 from...import ,避免在你的程序中出现名称冲突，同时也为了使程序更加易读

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')


print("Square root of 16 is", sqrt(16))
# sqrt函数是指定正方形面积取边长
