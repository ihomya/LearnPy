# coding=UTF-8

class SchoolMember:
    '''代表任何学校里的成员。'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")
        # end 参数用在超类的 tell() 方法的 print 函数中，
        # 目的是打印一行并允许下一次打印在同一行继续。
        # 这是一个让 print 能够不在打印的末尾打印出 \n （新行换行符）符号的小窍门


class Teacher(SchoolMember):
    '''代表一位老师。'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        # 在 Teacher 和 Student 子类中定义了 __init__ 方法，
        # Python 不会自动调用基类 SchoolMember 的构造函数，你必须自己显式地调用它
        # 相反，如果我们没有在一个子类中定义一个 __init__ 方法，
        # Python 将会自动调用基类的构造函数
        self.salary = salary  # 薪水
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        # 当我们使用 SchoolMember 类的 tell 方法时，
        # 我们可以将 Teacher 或 Student 的实例看作 SchoolMember 的实例
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''代表一位学生。'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks  # 分数
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# 打印一行空白行
print()

members = [t, s]
# 如果继承元组（Inheritance Tuple）中有超过一个类，
# 这种情况就会被称作多重继承（Multiple Inheritance
for member in members:
    # 对全体师生工作
    member.tell()
