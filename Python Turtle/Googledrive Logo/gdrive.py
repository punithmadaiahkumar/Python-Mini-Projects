import turtle as t

t.title("Google Drive Logo")
t.hideturtle()
t.Screen().bgcolor("Black")
t.pencolor("white")
t.pensize(0)
#blue
t.begin_fill()
t.fillcolor('#4688F4')
t.forward(170)
t.left(60)
t.forward(50)
t.left(120)
t.forward(220)
t.left(120)
t.forward(50)
t.end_fill()

#green
t.begin_fill()
t.fillcolor('#1FA463')
t.left(120)
t.forward(200)
t.left(120)
t.forward(50)
t.left(60)
t.forward(150)
t.left(60)
t.forward(50)
t.end_fill()

t.penup()
t.left(120)
t.forward(200)
t.left(120)
t.forward(50)
t.pendown()


#yellow
t.begin_fill()
t.fillcolor('#FFD048')
t.left(125)
t.forward(160)
t.left(55)
t.forward(53)
t.left(126)
t.forward(163)
t.end_fill()
t.done