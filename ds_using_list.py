# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
# 列表是一种用于保存一系列有序项目的集合
# 它是可变的，你可以对一个项目进行增删改查
print('I have', len(shoplist), 'items to purchase.')
# len函数返回一个集合的项目数
print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')
# 通过for...in循环来遍历集合
print('\nI also have to buy rice.')
shoplist.append('rice')
# append方法是为列表添加一个项目
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
# sort方法是用于对列表进行排序
# 这将影响列表本身，而不会返回一个修改过的列表
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
# del语句是从列表删除对应项目
print('I bought the', olditem)
print('My shopping list is now', shoplist)
# help(list) 可了解更多
