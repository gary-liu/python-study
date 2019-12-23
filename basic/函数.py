def print_line():
    print('-'*20)
print_line()

def print_lines(num):
    i = 0
    while i<num:
        print_line()
        i+=1
print_lines(5)

def sum_num (a,b, c):
    return  a+b+c
result =sum_num(1,2,4)
print(result)


def avg_num(a,b,c ):
    return sum_num(a,b,c)/3

print(avg_num(1,2,3))





