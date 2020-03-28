while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        # len 函数和来获取字符串的长度
        print('Too small')
        continue
        # 用以告诉 Python 跳过当前循环块中的剩余语句，并继续该循环的下一次迭代
    print('Input is of sufficient length')
    # 自此处起继续进行其它任何处理
