# 일반적인 프로그램
color = ""
speed = 0

def upSpeed():
    global speed
    speed += 10

def downSpeed():
    global speed
    speed -= 10


color = "white"
print("색상 :",color)
print("속도 :",speed)

upSpeed()
print("속도 :",speed)

# 일반적인 프로그램
color2 = ""
speed2 = 0

def upSpeed():
    global speed2
    speed2 += 10

def downSpeed():
    global speed2
    speed2 -= 10


color2 = "white"
print("색상2 :",color)
print("속도2 :",speed)

upSpeed()
print("속도2 :",speed)