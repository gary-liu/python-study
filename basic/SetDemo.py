# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
basket = {'apple','orangle','pear'}
print(basket)
print('apple' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a-b) # 集合a中包含而集合b中不包含的元素

print(a|b) # 集合a或b中包含的所有元素

print(a&b)  # 集合a和b中都包含了的元素
print(a^b) # 不同时包含于a和b的元素

# 类似列表推导式，同样集合支持集合推导式(Set comprehension):
a = {x for x in 'abkcda' if x not in 'abc'}
print(a)

set1 = set(("google","runoob",'taobao'))
print(set1)
print(set1.add("facebook"))
print(set1)
set1.update({12,3})
print(set1)
set1.update([12,3],[3,5])
print(set1)
set1.remove(12) # 不存在会发生错误
print(set1)
# set1.remove(12)
set1.discard(12) # 不存在不会发生错误
set1.pop() #我们也可以设置随机删除集合中的一个元素
print(set1)

print(len(set1))



