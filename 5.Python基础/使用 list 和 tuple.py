
# list  数组
classmates = ['张三', '李四', '王五']
print(classmates)

# classmatesLength 长度
classmatesLength = len(classmates)
print(classmatesLength)

# 通过索引访问每个同学的名字：
first_classmate = classmates[0]  # 获取第一个同学
last_classmate = classmates[-1]  # 获取最后一个同学

print("第一个同学:", first_classmate)
print("最后一个同学:", last_classmate)

# 修改 list 中的元素
classmates[1] = '赵六'
print("修改后的班级同学名单:", classmates)

# 添加元素到 list
classmates.append('孙七')
print("添加新同学后的名单:", classmates)

classmates.insert(1, '周八')  # 在索引位置 1 插入新同学
print("插入新同学后的名单:", classmates)

# 删除元素
classmates.remove('王五')  # 删除指定的同学
print("删除 '王五' 后的名单:", classmates)

last_removed_classmate = classmates.pop()  # 默认删除并返回最后一个元素  pop(i)
print("删除的最后一个同学:", last_removed_classmate)
print("删除后的名单:", classmates)

