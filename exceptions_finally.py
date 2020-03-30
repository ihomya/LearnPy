import sys
import time

f = None
try:
    f = open("poem.txt")
    # 我们常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        # 使用了 sys.stout.flush()，以便它能被立即打印到屏幕上
        sys.stdout.flush()
        print("Press ctrl+c now")
        # 为了确保它能运行一段时间
        # 通过使用 time.sleep 函数任意在每打印一行后插入两秒休眠，使得程序运行变得缓慢
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")

# 假设你正在你的读取中读取一份文件。
# 你应该如何确保文件对象被正确关闭，
# 无论是否会发生异常？这可以通过 finally 块来完成
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
# 在 try 块中获取资源，然后在 finally 块中释放资源是一种常见的模式
