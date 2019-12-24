import pprint ,pickle
pk1_file =open('E:/python_code/python_study/data.pk1', 'rb')
data1 = pickle.load(pk1_file)
pprint.pprint(data1)

data2 = pickle.load(pk1_file)
pprint.pprint(data2)
pk1_file.close()