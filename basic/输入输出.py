s = "hello ruuoob"
str(s)
repr(s)

for x in range (1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=" ")
    print(repr(x*x*x).rjust(4))

for x in range (1,11):
    print('{0:2d} {1:3d}{2:4d}'.format(x,x*x,x*x*x))

a = '12'
print(a.zfill(5))

print('{0} and {1}'.format("google","baidu"))
print('{1} and {0}'.format("google","baidu"))
print('{name} :{site}'.format(name='www',site='baidu'))

