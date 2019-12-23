import sys

list = [1,3,4,5]
it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))

for x in it :
    print(x,end=" ")

list = [1, 3, 4, 5]
it = iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()




