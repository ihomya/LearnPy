# Python 提供了一个叫作 Pickle 的标准模块，
# 通过它你可以将任何纯 Python 对象存储到一个文件中，并在稍后将其取回。
# 这叫作持久地（Persistently）存储对象
import pickle

# 我们存储相关对象的文件的名称
shoplistfile = 'shoplist.data'
# 需要购买的物品清单
shoplist = ['apple', 'mango', 'carrot']

# 准备写入文件(二进制 write binary)
f = open(shoplistfile, 'wb')
# 转储对象至文件
pickle.dump(shoplist, f)
f.close()

# 清除 shoplist 变量
del shoplist

# 重新打开存储文件(二进制读取 read binary)
f = open(shoplistfile, 'rb')
# 从文件中载入对象
storedlist = pickle.load(f)
# 通过 pickle 模块的 load 函数接收返回的对象。
# 这个过程被称作拆封（Unpickling）
print(storedlist)
