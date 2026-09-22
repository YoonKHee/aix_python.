class Student:
    def __init__(self,no,name,kor,eng,math):
        self.no = no
        self.name = name
        self.__kor = kor # 캡슐화 : 클내스 내부에서만 값을 수정할 수 있음.
        self.eng = eng
        self.math = math
        # self.total = kor+eng+math
        # self.avg = (kor+eng+math)/3
        
    def get_kor(self):
        return self.__kor

    def set_kor(self,kor):
        self.__kor = kor

    def sum(self):
        return self.__kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3         

    def __str__(self):
        return (f"{self.no},{self.name},{self.__kor},{self.eng},{self.math},{self.sum()},{self.avg():.2f}")
    
    # def print(self):
    #     print(f"{self.no},{self.name},{self.__kor},{self.eng},{self.math},{self.total},{self.avg:.2f}")





stuList = []
s = Student(1,"홍길동",100,100,100)
stuList.append(s)
s.kor = 98  # 클래스 변수값 수정
s.set_kor(50)
s.sum
s.avg
s.math = 10 # 클래스 변수값 수정
# s.print()
print(s)