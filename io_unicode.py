# encoding=utf-8
import io

# 如果你正在使用 Python 2，我们又希望能够读写其它非英语语言，我们需要使用 unicode 类型，
# 它全都以字母 u 开头，例如 u"hello world"
# Unicode 有“统一码”“万国码”“国际码”等多种译名

f = io.open("abc.txt", "wt", encoding="utf-8")
# 我们使用 io.open 并提供了“编码（Encoding）”与“解码（Decoding）”参数来告诉 Python 我们正在使用 Unicode
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)
