class Student:

    # 생성자
    def __init__(self,no,name,kor,eng,math):
        # self.__no = no # 캡슐화 : 클래스 내부에서만 값을 수정가능
        # 캡슐화시 값을 수정할 수 있도록, setter, getter을 만들어줌.
        self.no = no
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}"

    def cal_total(self):
        self.total = self.kor+self.eng+self.math

    def cal_avg(self):
        self.avg = self.total/3
# 객체선언을 하면
# s1 = Student() # s->3개 변수가 생성됨.
# no=1
# name="홍길동"
# total=50
s1 = Student(1,"홍길동",90,90,100)
s2 = Student(2,"유관순",100,100,99)

# 출력 : 참조변수명.변수명
print(s1.name)
# 수정 : 참조변수명.변수명 = 수정값
s1.name = "홍길자"
s1.kor = 20
s1.cal_total()
s1.cal_avg()
print(s1.name)
# 추가 : 참조변수명.변수명 : 없는변수 입력시 추가
s1.rank = 1
print(s1.rank)

# 전체출력
print(s1)
print(s2)

