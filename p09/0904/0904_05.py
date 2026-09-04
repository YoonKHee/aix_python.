stu = []
with open("C:\\aaa\\test2.txt","r",encoding="utf-8") as f:

    while True:
        line = f.readline()
        arr = line.split(",")
        for i,s in enumerate(arr):
            if 5>=i>=2:
                arr[i] = int(s)
            elif i ==6:
                arr[i] = float(s)
        if not line: break
        stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})

    print(stu)