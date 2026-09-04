stu = []
f = open("C:\\aaa\\test2.txt","r",encoding = "utf-8")
while True:
    line = f.readline()
    # 문자열을 각각의 문자열로 분리.
    line = line.strip()
    arr = line.split(",")
    for i,a in enumerate(arr):
        if 5>=i>=2:
            arr[i] = int(a)
        elif i==6:
            arr[i] = float(a)
    #stu 리스트에 저장
    if not line:break
    stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})

    print(line,end="")    
f.close()
print(stu)
