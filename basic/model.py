import sys
import mymodule


print('command args:')
for i in sys.argv:
    print(i)

print('\n\nPython path:',sys.path,'\n')

mymodule.hello()



