def reverse(text):
    return text[::-1]
# 使用 seq[a:b] 来从位置 a 开始到位置 b 结束来对序列进行切片
# 默认的步长为 1，它会返回一份连续的文本。如果给定一个负数步长，如 -1，将返回翻转过的文本

def replace_mark(text):
    forbidden = ("!","?","."," ","...",",")
    text = text.casefold()
    for i in forbidden:
        if i in text:
            text = text.replace(i,"")
    return text


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
# input() 函数将返回用户输入的文本
something = replace_mark(something)
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
