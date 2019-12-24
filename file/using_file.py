# file1 = open("E:/python_code/python_study/file1.txt",'w')
# file1.write("python is a very nice language")
# file1.close()

file2 = open("E:/python_code/python_study/file1.txt",'r')
# str = file2.read()
# print(str)
# # file2.close()


# str = file2.readline()
# print(str)
# file2.close()

# str = file2.readlines()
# print(str)
# file2.close()

for line in file2:
    print(line,end=" ")

file2.close()





