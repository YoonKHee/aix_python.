my = {"id":"aaa","pw":"1111","money":10_000_000,"bonusPoint":0}
cart = []
pd = [
    {"p_name":"컴퓨터","price":1000000,"bonusPoint":1000000*0.1},
    {"p_name":"냉장고","price":2000000,"bonusPoint":2000000*0.1},
    {"p_name":"오디오","price":500000,"bonusPoint":500000*0.1}
]

def cal1(choice):
    no = int(input(f"{pd[choice-1]['p_name']}를 구매하시겠습니까?(1:구매,0:취소)"))
    if no ==1:
        print(f"{pd[choice-1]['p_name']},구매완료")
        #------계산--------
        my['money'] -= pd[0]['price']
        my['bonusPoint'] += pd[0]['bonusPoint']

        print(f"m돈 :{my['money']:,}원")
        print(f"m보너스포인트 :{my['bonusPoint']:,}포인트")
    else:
        print("이전화면으로 이동합니다.")


# 아이디 패스워드 확인
while True:
    print("[ 쇼핑몰에 오신것을 환영합니다. ]")
    id = input("아이디:")
    pw = input("패스워드:")
    if my["id"] ==id and my["pw"]==pw:
        print("로그인 성공")
        break
    else:("로그인 실패")
print(f"현재보유금액:{my['money']:,}원")
print(f"현재보너스포인트:{my['bonusPoint']:,}원")
print("-"*40)
while True:
    print(" 쇼핑몰 구매사이트 ")
    for i,p in enumerate(pd):
        print(f"{i+1}. {p['p_name']}:{p['price']:,}원")
    print("9. 구매상품리스트")    
    print("-"*30)
    choice = int(input("원하는 번호 입력:"))
    if choice==1:
        cal1(choice)
    elif choice==2:
        cal1(choice)
    elif choice==3:
        cal1(choice)
    else:
        pass
        



# # 일반매개변수, 초기화매개변수
# # 가변매개변수, 키워드매개변수

# def cal(start=1,end=50,step=10): #초기화 매개변수
#     print(start,end,step)
# cal(0)


# # 가변매개변수 - 맨뒤쪽에 배치
# # 키워드매개변수 - 맨뒤쪽에 배치
# def str_print(*v,n): # *는 가변매개변수, 키워드 매개변수: 가변매개변수뒤의 n을 사용하려면 n값을 지정해줘야 한다.
#     print(n)

# str_print(1,2,3,4,5,n="안녕") # 키워드 매개변수 n=은 맨뒤로 보내야 한다.




# print(1,2,3,4,5,sep="--")
# print("번호","이름","국어","영어",sep="\t")
# arr = ["번호","이름","국어","영어"]
# print(*arr,sep="\t") #*는 전개연산자


# def str_print(n,*v): # 매개변수 2개, *는 가변매개변수
#     for i in range(n):
#         for j in v:
#             print(j,end="  ")
#         print()

# str_print(3,"안녕","반가워","잘있어")