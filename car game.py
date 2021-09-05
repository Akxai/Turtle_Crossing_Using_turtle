from turtle import Screen, Turtle
import time
from car_manager import CarManager
from player import Player
from car_scoreboard import Scoreboard

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.goto(-250, 270)
tim.pendown()
tim.speed("fastest")
tim.forward(500)
tim.penup()
tim.goto(0, 270)
tim.write("FINISH LINE", align="center", move=True, font=("Courier", 20, "normal"))
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # scoreboard.level()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # detect success
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()

