def ChangeInt (a):
    a = 10

b =2
ChangeInt(b)
print(b)

def changeme(mylist):
    "update transtport list "
    mylist.append([1,2,3,4,5])
    print("function data:",mylist)
    return
mylist = [10,39,40]
changeme(mylist)
print("out of function data:",mylist)


def printme (str):
    print(str)
    return
printme(str="hello")

def printInfo(name,age=23):
    print("name:",name)
    print("age:",age)
    return
printInfo(age=212,name="gary")
printInfo(name="test")

def printInfo(arg1,*vartuple):
    "打印任何传入的参数"
    # print("output:",arg1)
    print("output:")
    print(arg1)

    for var in vartuple:
        print(var)
    return
printInfo(10)
printInfo(70,69,50)

def printDis(arg1,**varDict):
     "打印任何传入的参数"
     print("output:")
     print(arg1)
     print(varDict)
     return
printDis(1,a =2,b =3 )






