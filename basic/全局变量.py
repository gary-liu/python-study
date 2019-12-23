a = 100
def testA():
    print(a)

def testB():
    global a #声明a是全局变量 修改全局变量要加上global关键字
    a = 200
    print(a)

testA()
testB()
print(a)


def num():
    return 1,2
result = num()
print(result)
a ,b = num()
print(a)
print(b)

