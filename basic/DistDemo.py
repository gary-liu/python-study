'''
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
'''

dict = {"name":"gary",'age':20,'class':'first'}
dict1 = {'abc':12,12.3:37}
print(dict['name'])
print('dict[age]:',dict['age'])

dict["age"]= 21
dict['school'] ="luban"
print(dict)

del dict['name']
print(dict)
# dict.clear()
print(dict)
# del dict
print(dict)
print(dict['age'])
'''
字典键的特性
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
'''
# 字典内置函数&方法
print(len(dict))
print(str(dict))

# print(dict.fromkeys(0))
print(dict.get("age"))







