import turtle
def main():
    window = turtle.Screen()
    window.bgcolor("white")
    turtle.title("I Love You")
    turtle.setup(width=500, height=500)
    boy = turtle.Turtle()
    boy.width(2)
    boy.color("black")
    boy.speed(3)
    boy.penup()
    boy.goto(-100, 100)
    
    
    turtle.mainloop()


if __name__ == "__main__": 
    main()