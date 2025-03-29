# # import turtle
# # t=turtle.Turtle()
# # t.speed(0)
# # # t.width(10)
# # # 1st one
# # # for i in range(4):
# # #     t.pendown()
# # #     t.forward(100)
# # #     t.right(90)
# # # t.penup()
# # # t.goto(100,100)
# # # t.pendown()
# # # t.circle(100)
# # # turtle.done()
# # # 2nd one
# # for i in range(100):
# #     t.penup()
# #     t.goto(0,-(i*10))
# #     t.pendown()
# #     t.circle(i*10)
    
# # turtle.done()
# import turtle

# def draw_rectangle(color, x, y, width, height):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.fillcolor(color)
#     turtle.begin_fill()
#     for _ in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)
#     turtle.end_fill()

# def draw_triangle(color, x, y, length):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.fillcolor(color)
#     turtle.begin_fill()
#     for _ in range(3):
#         turtle.forward(length)
#         turtle.left(120)
#     turtle.end_fill()

# def draw_house():
#     turtle.speed(3)
    
#     draw_rectangle("lightblue", -100, -100, 200, 200)
    
#     draw_triangle("brown", -120, 100, 240)
    
#     draw_rectangle("darkred", -30, -100, 60, 120)
    
#     draw_rectangle("white", -80, 20, 50, 50)
#     draw_rectangle("white", 30, 20, 50, 50)
    
#     turtle.hideturtle()
#     turtle.done()

# draw_house()


import turtle
t=turtle.Turtle()
t.speed(0)
def rec(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.right(90)
def cir(x,y,r):
    t.penup()
    t.goto(x,y)
    if r :
        t.right(90)
    
    t.pendown()
    t.circle(50)
rec(0,0)
t.left(135)
cir(0,0,1)

cir(100,0,1)

cir(100,-100,1)

cir(0,-100,1)
# screen=turtle.Screen()
# screen.screensize(800,800)
# # print(screen.screensize())
# rec(0,0)
# rec(850,500)
# rec(-950,500)
# rec(-950,-400)
# rec(850,-400)
turtle.done()