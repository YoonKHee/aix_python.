my_info = {"id":"aaa","pw":"1111","money":10_000_000,"bonusPoint":0}

s_arr = [
    {"prd_name":"컴퓨터","price":1_000_000},
    {"prd_name":"냉장고","price":2_000_000},
    {"prd_name":"오디오","price":500_000},
    {"prd_name":"세탁기","price":1_500_000},
]

def p_cal(choice):
    if my_info['money']<s_arr[choice-1]["price"]:
        print("잔액이 부족합니다. 충전후 이용해주세요.")
        return
    print(f"구매 상품:{s_arr[choice-1]["prd_name"]}")
    print(f"가격:{s_arr[choice-1]["price"]:,}원")
    my_info['money'] -= s_arr[choice-1]["price"]
    print(f"삼품구매후 보유금액 : {my_info['money']:,}원")
    

while True:
    for i,v in enumerate(s_arr):
        print(f"{i+1}.{v["prd_name"]}:{v["price"]:,}")
    choice = int(input("번호입력:"))
    if choice ==1: # 컴퓨터 100만원
        p_cal(choice)
    if choice ==2: # 냉장고 200만원
        p_cal(choice)
    if choice ==3: # 오디오 50만원
        p_cal(choice)
    if choice ==4: # 세탁기 150만원
        p_cal(choice)