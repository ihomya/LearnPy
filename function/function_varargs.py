# 可变参数
# 有时你可能想定义的函数里面能够有任意数量的变量，也就是参数数量是可变的，这可以通过使用星号*来实现

def total(a=5, *numbers, **phonebook):
    # 此处*numbers 代表 元组numbers
    # 此处**phonebook 代表 字典phonebook
    print('a', a)

    #遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    #遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
print(total(1,2,3))
