# file = open('E:/python_code/python_study/file2.txt','w')
# # 如果要写入一些不是字符串的东西, 那么将需要先进行转换
# value = ('www.baidu.com',123)
# file.write(str(value))
# print(file.tell())
# file.close()

file = open('E:/python_code/python_study/foo.txt','rb+')
f = file.write(b'0123456789abcdef')
print(f)

print(file.seek(5))
print(file.read(1))





