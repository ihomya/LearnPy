for i in range(1, 5):
    # range 函数生成这一数字序列
    # range(1,5) 将输出序列 [1, 2, 3, 4]
    # range(1,5,2) 将会输出 [1, 3]
    # 第三个数字将成为逐步递增的加数
    # 如果你希望获得完整的数字列表，要在使用 range() 时调用 list()。
    # 例如下面这样：list(range(5)) ，它将会返回 [0, 1, 2, 3, 4]
    print(i)
# 可选部分
else:
    # 会在 for 循环结束后开始执行
    print('The for loop is over')
# 特点是会在一系列对象上进行迭代（Iterates），意即它会遍历序列中的每一个项目
