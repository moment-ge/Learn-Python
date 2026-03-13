# if 语句
age = 20
if age >= 18:
    print("你是成年人")

# elif 语句
age = 15
if age >= 18:
    print("你是成年人")
elif age >= 13:
    print("你是青少年")

# else 语句
age = 10
if age >= 18:
    print("你是成年人")
elif age >= 13:
    print("你是青少年")
else:
    print("你是儿童")

# input() 函数
birth = int(input('birth: '))
if birth < 2000:
    print('00前')
else:
    print('00后')
