list1 = [i for i in range(0,10,2)]
print(list1)

list2 = []
for i in range(10):
    if i%2 ==0:
        list2.append(i)
print(list2)

list3 = [i for i in range(10) if i%2 ==0]
print(list3)

#[(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
list4 = []
for i in range(1,3):
    for j in range(3):
        list4.append((i,j))
print(list4)
# 多for循环嵌套
list5 = [(i,j) for i in range(1,3) for j in range(3)]
print(list5)

#  创建一个字典：字典的key 1-5数字  value 是这个数字的2次方
dict1 = {i:i**2 for i in range(1,5)}
print(dict1)

# 将两个列表合并为一个字典

list1 = ['name','age','gender']
list2 = ['tom',20,'man']

dict2 = { list1[i]:list2[i] for i in range(len(list1))}
print(dict2)

# 提取字典中目标数据
counts={'MBP':234,'HP':256,'DELl':201,'Levo':21,'acer':23}
print(counts.items())
dict = { key:value for key,value in counts.items() if value>=200}
print(dict)




