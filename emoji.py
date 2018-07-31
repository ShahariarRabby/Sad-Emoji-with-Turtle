import turtle
sad=turtle.Turtle()
sad.up()
sad.goto(0, -100)  
sad.down()

sad.begin_fill()
sad.fillcolor("yellow")  
sad.circle(100)
sad.end_fill()

sad.up()

sad.goto(65, -40)
sad.setheading(-60)
sad.width(5)
sad.down()
sad.circle(-80, -120)  
sad.fillcolor("black")

for i in range(-35, 105, 70):
    sad.up()
    sad.goto(i, 35)
    sad.setheading(0)
    sad.down()
    sad.begin_fill()
    sad.circle(10)   
    sad.end_fill()
    
sad.hideturtle()
turtle.mainloop()
