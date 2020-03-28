def maximum(x, y):
    if x > y:
        return x
        # return 语句用于从函数中返回，也就是中断函数。
        # 我们也可以选择在中断函数时从函数中返回一个值。
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
        #return

print(maximum(2, 3))
