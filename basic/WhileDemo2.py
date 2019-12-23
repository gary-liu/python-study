count = 0
while count < 5:
    print(count,"less 5")
    count += 1
else:
    print(count, "count larger 5 ")

# 类似if语句的语法，如果你的while循环体中只有一条语句，
# 你可以将该语句与while写在同一行中， 如下所示：
# flag = 1
# while (flag): print("welcome python study")
# print('Good bye!')

sites = ['baidu','Google','Runoob',"Taobao"]
for site in sites:
    if site == "Runoob":
        print("cailiao")
        break
    print("loop data:",site)
else:
    print("no data loop")
print("loop over")

n = 5
while n >0:
    n -= 1
    if n==2:
        continue
    print(n)
print('loop over')

# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句，如下实例
while True:
    pass

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")
