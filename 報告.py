while True:
    print("歡迎來到販賣機系統")
    print("1.洋芋片,價格:25元")
    print("2.可樂,價格:40元")
    print("3.菸,價格:100元")
    print("4.衛生紙,價格:20元")
    print("5.泡麵,價格:30元")
    print("6.手機配件,價格:50元")
    print("7.冰品,價格:30元")
    print("8.離開系統")
    x=int(input("請輸入編號"))
    
    if x==1:
        y=int(input("請輸入數量:"))
        ans=25*y
        print("總共:",ans,"元")
    if x==2:
        y=int(input("請輸入數量:"))
        ans=40*y
        print("總共:",ans,"元")
    if x==3:
        y=int(input("請輸入數量:"))
        ans=100*y
        print("總共:",ans,"元") 
    if x==4:
        y=int(input("請輸入數量:"))
        ans=20*y
        print("總共:",ans,"元")
    if x==5:
        y=int(input("請輸入數量:"))
        ans=30*y
        print("總共:",ans,"元")
    if x==6:
        y=int(input("請輸入數量:"))
        ans=50*y
        print("總共:",ans,"元")
    if x==7:
        y=int(input("請輸入數量:"))
        ans=30*y
        print("總共:",ans,"元")
    if  x==8:
        print("謝謝惠顧")
        break
    