# 所有字符串都是 str 类下的对象
# help(str)
# 这是一个字符串对象
name = 'Swaroop'
# startswith 方法用于查找字符串是否以给定的字符串内容开头
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
# in 运算符用以检查给定的字符串是否是查询的字符串中的一部分
if 'a' in name:
    print('Yes, it contains the string "a"')
# find 方法用于定位字符串中给定的子字符串的位置
if name.find('war') != -1:
    print('Yes, it contains the string "war"')
# str 类同样还拥有一个简洁的方法用以 联结（Join）序列中的项目
# 其中字符串将会作为每一项目之间的分隔符，并以此生成并返回一串更大的字符串
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
