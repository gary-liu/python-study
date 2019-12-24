# x = 10
# if x>5:
#     raise Exception ('x is not lager 5')

try:
    raise NameError('hiThree')
except NameError:
    print('ANn exception flew by!')
    raise

