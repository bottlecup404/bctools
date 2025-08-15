import turtle
import random

def draw_rectangle(width: int, height: int, color: str = "blue"):
    """
    绘制矩形
    
    Args:
        width: 矩形宽度
        height: 矩形高度
        color: 填充颜色
    """
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    turtle.done()

def draw_sun():
    """绘制太阳"""
    t = turtle.Turtle()
    t.speed(0)
    t.color("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
    for _ in range(12):
        t.forward(70)
        t.backward(70)
        t.left(30)
    
    turtle.done()

def draw_flower():
    """绘制花朵"""
    t = turtle.Turtle()
    t.speed(0)
    
    # 花茎
    t.color("green")
    t.pensize(3)
    t.right(90)
    t.forward(200)
    
    # 花朵
    t.backward(100)
    t.color("pink")
    t.begin_fill()
    for _ in range(6):
        t.circle(20, 180)
        t.right(60)
    t.end_fill()
    
    # 花蕊
    t.color("yellow")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
    turtle.done()

def draw_house():
    """绘制房子"""
    t = turtle.Turtle()
    t.speed(0)
    
    # 房子主体
    t.color("brown")
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()
    
    # 屋顶
    t.color("red")
    t.begin_fill()
    t.left(45)
    t.forward(70)
    t.right(90)
    t.forward(70)
    t.end_fill()
    
    # 门
    t.penup()
    t.goto(40, -100)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()
    
    turtle.done()