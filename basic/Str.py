str ="Runoob"
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
print(str)
print(str[0:-1])
print(str[2])
print(str[2:6])
print(str[2:])
print(str*2)  # 输出字符串两次

print(str+' hello ')
print("--------------------------")
print('hello\n runnbob')  # 使用反斜杠(\)+n转义特殊字符

print(r'hello\n runoob') # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

x = 'a'
y = 'b'
# 换行输出
print(x)
print(y)
# 不换行输出
print(x,end=" ")
print(y,end=" ")
print()

print("我叫 %s 今年 %d 岁 ！" % ('小明',10))

para_str = """
这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)
# Python 的字符串内建函数
str = "hello world "
print(str.capitalize())
print(str.center(2,"H"))

