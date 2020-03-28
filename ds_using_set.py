# 集合（Set）是简单对象的无序集合
# 当集合中的项目存在与否比起次序或其出现次数更加重要时，我们就会使用集合。
# 通过使用集合可以测试某些对象的资格或情况，检查它们是否是其它集合的子集，找到两个集合的交集
bri = {'brazil', 'russia', 'india'}
print('india' in bri)
print('usa' in bri)
bric = bri.copy()
bric.add('china')
# 判断是否为其他集合的父集
print(bric.issuperset(bri))
bri.remove('russia')
# 以下是取集合交集的两种方法
print(bri & bric)
print(bri.intersection(bric))
