# “ab”是地址（Address）簿（Book）的缩写
# 字典：ab = {唯一键:值}
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
# 键为不可变对象
# 只能使用简单对象作为键值
print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值—值配对
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
# 字典是无序的
# 字典中的成对的键值—值配对不会以任何方式进行排序。
# 如果你希望为它们安排一个特别的次序，只能在使用它们之前自行进行排序
# 字典是属于 dict 类下的实例或对象
# help(dict)
