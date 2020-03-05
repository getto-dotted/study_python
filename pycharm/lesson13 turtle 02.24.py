# 터틀 그래픽 프로그램
# 두근두근 파이썬( 생능출판사)

import turtle

t = turtle.Turtle()

t.shape("turtle")

t.speed(0)
t.pensize(3)
length = 10
while length < 500:
    t.forward(length)
    t.left(89)
    length +=5




"""
t.color('red')

t.begin_fill();

for i in range(4):
    t.forward(100)

    t.left(90)

t.end_fill();
"""
