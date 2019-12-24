try:
    runoo()
except AssertionError as error:
    print(error)
else:
    try:
        with open("file.log") as file:
            read_data= file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('finally')
    