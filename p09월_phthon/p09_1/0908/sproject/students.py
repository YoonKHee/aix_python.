class Students:
    stus = []

    def __init__(self):
        pass

    def add(self,s):
        self.stus.append(s)

    def print(self):
        print("번호","이름","국어","영어","수학","합계","평균",sep="\t")
        for s in self.stus:
            print(s)