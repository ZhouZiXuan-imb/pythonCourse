names = ['zhufengjiao', 'zhouzixuan', 'zhouzhou']

# while循环

# i = 0
# while (i < len(names)):
#     print("我是%d个名字%s" % (i + 1, names[i]))
#     i += 1

# for循环
# for 临时变量名 in 需要遍历的变量名(例如列表的变量名):
#     可以使用临时变量...
#     ...

# 如果列表中的数据已经遍历完成了 for循环会自动停止
# enumerate方法每次执行的时候会自动给i赋值为0，1，2，3，4.....
for i, key in enumerate(names):
    print("第%d个名字是%s" % (i + 1, key))

