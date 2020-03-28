# 列表、元组、字典均为序列的表现形式
# 序列主要功能是资格测试（i与not in表达式）和索引操作
# 列表、元组、字典拥有一种切片运算符：它能够允许我们序列中的某段切片——也就是序列之中的一部分。
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
# 索引或“下标（Subscription）”操作符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])
print("")
# Slicing on a list #
# 列表中切片
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
print("")
# 从某一字符串中切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
# 切片中数字是可选的，冒号却不是
# 第一个数字（冒号前面的那位）指的是切片开始的位置
# 第二个数字（冒号后面的那位）指的是切片结束的位置
# 如果第一位数字没有指定，Python 将会从序列的起始处开始操作
# 如果第二个数字留空，Python 将会在序列的末尾结束操作
# 序列切片将包括起始位置，但不包括结束位置。
# shoplist[:] 返回的是整个序列
# 你同样可以在切片操作中提供第三个参数，这一参数将被视为切片的步长（Step）（在默认情况下，步长大小为 1）
print(shoplist[::2])
