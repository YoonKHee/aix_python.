my = {"id":"aaa","pw":"1111","money":10_000_000,"point":0}

s_arr = [
    {"prd_name":"컴퓨터","price":1_000_000},
    {"prd_name":"냉장고","price":2_000_000},
    {"prd_name":"오디오","price":500_000},
    {"prd_name":"세탁기","price":1_500_000},
]

def a(choice):
    if my['money'] < s_arr[choice-1]['price']:
        print(f"잔액이 부족합니다. 남은잔액{my['money']:,}원")
        return
    print(f"구매상품:{s_arr[choice-1]['prd_name']}")
    print(f"상품금액:{s_arr[choice-1]['price']:,}원")
    my['money'] -= s_arr[choice-1]['price']
    print(f"상품 구매후 남은 금액 :{ my['money']:,}원")
    my['point'] += int(s_arr[choice-1]['price']*0.1)
    print(f"상품값의 10퍼센트가 포인트로 적립됩니다. 현재 내 포인트:{my['point']:,}포인트")


def login():
    id = input("아이디:")
    pw = input("패스워드:")
    if my['id']==id and my['pw']==pw:
        print("로그인 성공")
        break
    else:
        print("로그인 실패")
while True:
    login()

    for i,v in enumerate(s_arr):
        print(f"{i+1}.{v['prd_name']}/{v['price']:,}원")
    choice = int(input("번호입력:"))

    if choice==1:
        a(choice)
    elif choice==2:
        a(choice)
    elif choice==3:
        a(choice)
    elif choice==4:
        a(choice)
    else:
        pass