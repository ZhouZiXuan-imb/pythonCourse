count = 0

while (True):
    username = input('请输入用户名:')

    password = input('请输入密码:')

    result = username.find(password)

    if (count >= 5):
        print('今日不能再次注册')
        break

    if (result != -1):
        print('请重新输入')
        count += 1
    else:
        print('登陆成功')

