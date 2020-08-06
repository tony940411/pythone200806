import os.path

d={}
if os.path.isfile('myfile.txt'):
    print('file存在')
else:
    print('file不存在')
    
def buildMenu():
        print("1.登錄成績")
        print("2.列出所有成績")
        print("3.查詢成績")
        print("4.離開")
        x=int(input("請輸入數字"))
        return x
if os.path.isfile('myfile.txt'):
    print('file存在')
else:
    print('file不存在')
while True:
    if x==1:
        z=input("請輸入名字")
        c=input("請輸入成績")
        fo=open('myfile.txt','a')
        fo.write(z)
        fo.write(c)   
        fo.close()
        if x==2: