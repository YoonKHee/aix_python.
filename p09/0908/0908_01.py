# 변수와 함수를 모두 포함해서 구현한다.
class Car:
    color = ""
    speed = 0
    tire = 0
    door = 0

    # 생성자 - 생성함수 : Car() 선언될때 실행되는 함수
    def __init__(self,color,speed,tire,door):
        self.color = color
        self.speed = speed
        self.tire = tire
        self.door = door





    def upSpeed(self):
        self.speed += 10

    def downSpeed(self):
        self.speed -= 10

#--------------------------
# 클래스를 1개 생성
# c = Car() # 객체(인스턴스) 생성 / 4개 변수, 2개 함수
# c.color = "white"
# c.speed = 100
# c.tire = 5
# c.door = 3
# c.upSpeed()
# 클래스 객체선언 
c2 = Car("skyblue",200,4,5)
c2.upSpeed()
c3 = Car("gray",50,5,5)
c3.upSpeed()

# print(c.speed)
print(c2.speed)
print(c3.speed)