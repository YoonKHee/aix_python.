title = ["번호","이름","국어","영어","수학","합계","평균"]
k_title = ["no","name","kor","eng","math","total","avg"]
stu = []
sno = 1

def main(): # 메인프로그램
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    choice = int(input("번호입력:"))
    return choice
#-----------------------------------------------------
while True:
    choice = main()

    if choice == 1:

        while True:
            print("[ 학생성적입력 ]")
            no = sno
            name = input("이름(0:이전화면):")
            if name =="0":
                print("이전화면으로 돌아갑니다.")
                break
            score = [0]*3
            for i in range(3):
                score[i] = int(input(f"{title[i+2]}점수:"))
            total = score[0] + score[1] + score[2]
            avg = total/3
            sno += 1
            stu.append({"no":no,"name":name,"kor":score[0],"eng":score[1],"math":score[2],"total":total,"avg":avg})
            print(f"{name}학생 성적이 저장되었습니다.")

    elif choice == 2:
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        for i in stu:
            print(f"{i['no']}\t{i['name']}\t{i['kor']}\t{i['eng']}\t{i['math']}\t{i['total']}\t{i['avg']:.2f}")
        print()


    elif choice == 3:
        print("[ 학생성적수정 ]")
        print("학생이름 검색")
        name = input("학생이름(0.이전화면):")
        if name ==0:
            print("이전화면")
            break
        temp = 0
        for i,s in enumerate(stu):
            if s['name'] == name:
                print(f"{name}학생을 찾았습니다.")
                temp = 1
                print(f"{name}학생은 {i+1}번입니다.")
        if temp == 0:
            print("학생을 찾지 못하였습니다.")
        elif temp ==1:
            while True:
                print("[ 과목수정선택 ]")
                print("1. 국어 2. 영어 3.수학")
                ch = int(input("번호입력"))
                if ch ==0:
                    break
                print(f"현재{title[ch+1]}점수:{s[k_title[ch+1]]}")

            

        
        

                choice = int(input("번호입력:"))
                if choice ==0:
                    break

                print(f"현재{title[choice+1]}점수:{s[k_title[choice+1]]}")
                s[k_title[choice+1]] = int(input(f"변경하려는 {title[choice+1]}점수:"))
                s['total'] = s['kor']+s['eng']+s['math']
                s['avg'] = s['total']/3
                print(f"{s[k_title[choice+1]]}점으로 {title[choice+1]}점수 변경.")