from turtle import Turtle, Screen
import random
color = ["red", "purple", "green", "Yellow", "blue", "indigo"]


screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet",prompt="Choose which color turtle is gonna win : ")
y_pos = [-100, -50, 0, 50, 100, 150]

for turtle in range(6):
    tim = Turtle(shape="turtle")
    tim.color(color[turtle])
    tim.penup()
    tim.goto(-230, y_pos[turtle])

screen.exitonclick()
