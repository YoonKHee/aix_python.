# import func #: func.hap(),func.hap2(),func.hap3()
# import func as fn # 별칭사용 fn.hap(), fn.hap2(),fn.hap3()
from func import hap,hap2,hap3 # 그대로 사용
# 1. 매개변수X, return X - hap()
hap()
print("hap() 완료")


# 2. 매개변수 O, return X - hap2()
num3 = int(input("1번수:"))
num4 = int(input("1번수:"))
hap2(num3,num4)
print("hap2() 완료")

# 3. 매개변수 O, return O - hap3()
num5 = int(input("1번수:"))
num6 = int(input("1번수:"))
sum = hap3(num5,num6)
print(sum)
print("hap3() 완료")

