import os.path
if os.path.isfile('myfile.txt'):
    print('file存在')
else:
    print('file不存在')
    




fo=open('myfile.txt','w')
fo.write('test')
fo=open('myfile.txt','a')
fo.write(' and test')
fo=open('myfile.txt','r')
x=fo.read()
print(x)
fo.close()
