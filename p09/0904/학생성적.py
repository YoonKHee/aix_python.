title = ["번호","이름","국어","영어","수학","합계","평균"]
k_title = ["no","name","kor","eng","math","total","avg"]
stu = []
sno = 1 # 학생성적인원변수 - 나중엔 db에서 부여함
#----------------------------------------------------------------------------------
# 파일 불러오기


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
    stu.append({'no':arr[0],'name':arr[1],
                'kor':arr[2],'eng':arr[3],
                'math':arr[4],'total':arr[5],
                'avg':arr[6]})  
f.close()

print(stu2)


#----------------------------------------------------------------------------------
# 메인함수선언
def s_mainPrint():
    print(" [ 학생성적프로그램 ] ")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("-"*60)
    choice = int(input("번호 입력>>"))
    print()
    return choice


# 학생성적입력함수선언
def s_input():
    global sno
    while True: # 입력을 멈추고 싶을때까지 입력받음
        no = sno
        print("[ 학생성적입력 ]")
        name = input(f"{no}번째 이름입력 (0.이전화면이동):")
        if name =="0": break
        score = [0]*3
        for i in range(3):
            score[i] = int(input(f"{title[i+2]}점수:"))
        total = score[0]+score[1]+score[2]
        avg = total/3
        sno += 1
        stu.append({'no':no,'name':name,'kor':score[0],'eng':score[1],'math':score[2],'total':total,'avg':avg})
        print(f"{name}학생 성적이 저장되었습니다.")
        s_output()
    return sno

#학생성적출력함수선언
def s_output():
    print()
    print("[ 학생성적출력 ]")
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    for s in stu:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}")
    print()


def s_update():# 학생성적수정
    while True:
        print()
        print("[학생성적수정]")
        name = input("찾을학생이름:")
        if name == "0":
            break
        temp = 0
        for i,s in enumerate(stu):
            if s['name'] ==name:
                print(f"{name}학생을 찾았습니다")
                print(f"{name}학생의 번호는 {i+1}번입니다")
                temp = 1
                break
        if temp== 0:
            print("학생이없습니다")
        elif temp ==1:
            while True:
                print("[ 과목수정선택 ]")
                print("1. 국어 2. 영어 3.수학")
                choice = int(input("번호입력:"))
                if choice ==0:
                    break
                elif choice<1 or choice>3:
                    print("다시입력하세요.")
                    continue
                print(f"현재{title[choice+1]}점수:{s[k_title[choice+1]]}")
                s[k_title[choice+1]] = int(input(f"변경하려는 {title[choice+1]}점수:"))
                s['total'] = s['kor']+s['eng']+s['math']
                s['avg'] = s['total']/3
                print(f"{s[k_title[choice+1]]}점으로 {title[choice+1]}점수 변경.")



#------------------------------------------------------
while True:
    choice = s_mainPrint()
    if choice == 1: # 학생성적 입력부분
        s_input()
    if choice == 2: # 학생성적 출력부분
        s_output()
    elif choice ==3:
        s_update()




