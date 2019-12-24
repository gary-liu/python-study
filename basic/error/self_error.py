# class MyError(Exception):
#     def __init__(self,value):
#         self.value = value
#     def __str__(self):
#         return repr(self.value)
#
# try:
#     raise MyError(2*3)
# except MyError as e :
#     print('My exceptino occured ,value:',e.value)

#
# for line in open("myfile.txt"):
#     print(line, end="")

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")