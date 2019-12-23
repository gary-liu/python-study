tup1 = ('google','runoob',1934,2000)
print(tup1)
tup2 = (1,2,3,4,5)
tup3 = "a","b","c","d"
print(tup3)
print(tup2)
print(type(tup2))

tup4 = (50)  # 不加逗号，类型为整型
print(type(tup4))

tup4 = (50,)
print(type(tup4))

print(tup1[1])
print("tup2[1:5]:",tup2[1:5])

tup1 = (12,34,45.56)
tup2 = ('abc','xyz')
# tup1[0]= 100 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
print(tup1+tup2)

# del tup1 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组

# 元组运算符
'''
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。
这就意味着他们可以组合和复制，运算后会生成一个新的元组。
元组索引，截取
因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，
也可以截取索引中的一段元素
'''
# Python元组包含了以下内置函数
print(len(tup2))
print(max(tup2))
print(min(tup2))
list = [1,2,3]
print(tuple(list))

# 关于元组是不可变的
# 所谓元组的不可变指的是元组所指向的内存中的内同不可变。
# 从以上实例可以看出，重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对象。

tup = (12,3,4)
print(id(tup))# 查看内存地址
tup = ('a')
print(id(tup))  # 内存地址不一样了






