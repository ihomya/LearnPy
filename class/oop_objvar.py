# coding=UTF-8
class Robot:
    """表示一个带右名字的机器人"""

    # 一个类变量，用来计数机器人的数量
    population = 0

    def __init__(self,name):
        """初始化数据"""
        self.name = name # 对象变量
        print("(Initializing {})".format(self.name))

        # 当有人被创建时，机器人
        # 将增加人口增加
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))
        # 只能使用 self 来引用同一对象的变量与方法。这被称作属性引用（Attribute Reference）
        Robot.population -=1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚恳问候

        没问题，你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod # 装饰器
    # 将装饰器想象为调用一个包装器（Wrapper）函数的快捷方式，
    # 因此启用 @classmethod 装饰器等价于调用：how_many = classmethod(how_many)

    # how_many 实际上是一个属于类而非属于对象的方法
    # 这就意味着我们可以将它定义为一个 classmethod（类方法） 或是一个 staticmethod（静态方法）
    # 由于我们已经引用了一个类变量，因此我们使用 classmethod（类方法）
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
# 当一个对象变量与一个类变量名称相同时，类变量将会被隐藏
# 除了 Robot.popluation，
# 我们还可以使用 self.__class__.population，
# 因为每个对象都通过 self.__class__ 属性来引用它的类。
# 通过 Robot.__doc__ 访问类的 文档字符串，对于方法的文档字符串，则可以使用 Robot.say_hi.__doc__
# print(Robot.__doc__)
# 所有的类成员都是公开的。但有一个例外：如果你使用数据成员并在其名字中使用双下划线作为前缀，形成诸如 __privatevar 这样的形式，Python 会使用名称调整（Name-mangling）来使其有效地成为一个私有变量。
# 你需要遵循这样的约定：任何在类或对象之中使用的变量其命名应以下划线开头，其它所有非此格式的名称都将是公开的，并可以为其它任何类或对象所使用。请记得这只是一个约定，Python 并不强制如此（除了双下划线前缀这点）。
