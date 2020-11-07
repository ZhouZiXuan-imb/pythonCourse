# count的简单练习

# 1.
# mystr = '1.txt 2.txt 3.txt 4.txt 5.txt'
#
# newmystr = mystr.count(' ')
#
# print(newmystr + 1)


# 2.
# content = 'kjshadjkfgsjhdfg13243246@163.comasjhdgjkasgdrjjhasreg@qq.comjkhgsadjhfgjhsadfjhbdasfkjhk@qq.com'
#
# count = content.count('@')
#
# # %d是占位符，字符串中占位后  在字符串的后面加一个 % 变量使用字符串中的占位符
# print("一共有%d个电子邮箱" % count)


# 3. 切片和replace方法练习
# 要求：输入一个手机号，例如13140203536，将其显示为1314****536

# tel = "13140203536"
#
# str = tel[4:8]
#
# newStr = tel.replace(str,"****")
#
# print(newStr)


# 4.endswith的使用 它是用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
# 可选参数"start"与"end"为检索字符串的开始与结束位置

# while True:
#     houzhui = input('请输入一个文件名')
#     if houzhui.endswith(".png") or houzhui.endswith('.jpg') or houzhui.endswith('gif'):
#         print('符合要求')


# 5.lower和upper的使用
# lower把字符转小写 upper转大写

# 发送给用户的验证码
# security = 'Qj7s68'
#
# # 让用户输入收到的验证码
# userSecurity = input('请输入一个验证码')
#
# # 判断用户输入的验证码全都转成小写之后是否和验证码一样 如果一样就提示成功
# if(userSecurity.lower() == security.lower()) :
#     print('输入正确')









