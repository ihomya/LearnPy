# 引用（Reference）
# 当你创建了一个对象并将其分配给某个变量时，变量只会查阅（Refer）某个对象，并且它也不会代表对象本身。
# 变量名只是指向你计算机内存中存储了相应对象的那一部分。这叫作将名称绑定（Binding）给那一个对象
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist 只是指向同一对象的另一种名称
mylist = shoplist

# 我购买了第一项项目，所以我将其从列表中删除
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到 shoplist 和 mylist 二者都
# 打印出了其中都没有 apple 的同样的列表，以此我们确认
# 它们指向的是同一个对象

print('Copy by making a full slice')
# 通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:]
# 删除第一个项目
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到现在两份列表已出现不同
# 必须使用切片操作来制作副本。如果你仅仅是将一个变量名赋予给另一个名称，那么它们都将“查阅”同一个对象
# 记住列表的赋值语句不会创建一份副本。你必须使用切片操作来生成一份序列的副本。
