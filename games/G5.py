import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),0)

import mysql.connector as s
file=open('store.txt')
pasadusn=((file.read()).strip()).split()
file.close()
bsq=s.connect(host='localhost',user='root',passwd=pasadusn[0],database='gaming')
cur=bsq.cursor()

from turtle import Turtle, Screen
import random
winner='None'

def close(z):
    cur.execute('update gaming_details_{} set score="{}" where gamename="{}"'.format(pasadusn[1],z,pasadusn[2]))
    bsq.commit()
    bsq.close()
    screen.bye()
    

screen = Screen()
screen.setup(width=500, height=400)
screen.bgpic(r'tuback.png')
turtle_bet = screen.textinput(title="Make your bet!", prompt="Which turtle do you think will win? Enter a colour: ")
turtle_bet=turtle_bet.lower()

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = (-100, -60, -20, 20, 60, 100)
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=(y_positions[turtle_index]))
    all_turtles.append(new_turtle)

race_active=True
while race_active:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_active = False
            winning_colour = turtle.pencolor()
            if winning_colour == turtle_bet:
                winner='You win!'
                close(winner)
            else :
                winner='You lose'
                close(winner)

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    

