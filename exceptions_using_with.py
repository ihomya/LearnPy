# 在 try 块中获取资源，然后在 finally 块中释放资源是一种常见的模式。
# 因此，还有一个 with 语句使得这一过程可以以一种干净的姿态得以完成
with open("poem.txt") as f:
    for line in f:
        print(line, end='')
# 程序输出的内容应与上一个案例所呈现的相同。本例的不同之处在于我们使用的是 open 函数与 with 语句——我们将关闭文件的操作交由 with open 来自动完成。
# 在幕后发生的事情是有一项 with 语句所使用的协议（Protocol）。它会获取由 open 语句返回的对象，在本案例中就是“thefile”
#
# 它总会在代码块开始之前调用 thefile.__enter__ 函数，并且总会在代码块执行完毕之后调用 thefile.__exit__
# 因此，我们在 finally 代码块中编写的代码应该格外留心 __exit__ 方法的自动操作。这能够帮助我们避免重复显式使用 try..finally 语句
