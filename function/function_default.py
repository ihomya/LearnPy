def say(message, times=1):
    # 此处已设置times的默认参数值为1
    print(message * times)

say('Hello')
# 当无参数times时将默认为1
say('World', 5)
# 值是按参数所处的位置依次分配的，因此参数顺序不可更改
