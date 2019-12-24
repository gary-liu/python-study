import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("could not convert data to interger")
except:
    print("Unexpected error:",sys.exc_info()[0])
    raise






