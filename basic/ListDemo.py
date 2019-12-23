list = ['abck',38,8.34,'ruunoob',802.2]
tinylist = [12,'ruunoob']
print(list)# 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist*2) # 输出两次列表
print(list+tinylist) # 连接列表

# 更新列表
list[2]= 3
print(list[2])
del list[2]
print(list)

print(len(list))

print(3 in list)

for x in list:
    print(x ,end=" ")

l = ["google",'runoob','raobao']

print(l[2])
print(l[-2])
print(l[1:])

squrars = [1,4,9,16]
squrars += [2,3,6]
print(squrars)

# 嵌套列表
a = ['a','b','c']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0])
print(x[0][1])
# Python列表函数&方法
print(len(list))
# print(max(list))

print(list.append("a"))
print(list)
print(list.count("a"))
print(list.extend(tinylist))
print(list)
print(list.index("a"))
print(list.insert(5,"c"))
print(list.pop())
print(list.remove("c"))
print(list.reverse())
# print(list.sort())
print(list)

for i in enumerate(list):
    print(i,end=" ")

for index ,char in enumerate(list,start=1):
    print(f'index {index},word is {char}')
# 列表推导式
list = [i for i in range(10)]
print(list)


















