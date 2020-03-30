try:
    text = input('Enter something -->')
except EOFError:
    # 如果没有提供错误或异常的名称，它将处理所有错误与异常
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    # 要注意到必须至少有一句 except 字句与每一句 try 字句相关联,否则try代码块是无意义的
    print('You cancelled the operation.')
else:
    # else 子句将在没有发生异常的时候执行
    print('You entered {}'.format(text))
