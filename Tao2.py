import turtle
t=turtle.Pen()
t.color('green')
t.shape('turtle')
t.penup()
t.goto(-400,-300)
t.pendown()

for i in range(18):
    t.forward(100)
    t.lt(220)
for i in range(18):
    t.forward(200)
    t.rt(220)
for i in range(18):
    t.forward(400)
    t.rt(220)
for i in range(18):
    t.forward(800)
    t.rt(220)
t.lt(180)
t.penup()
t.forward(250)
turtle.done()




