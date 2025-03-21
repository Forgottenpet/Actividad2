from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors_list = ('black', 'green', 'darkorange', 'navy', 'blue')
color_snake = None
color_food = None

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    directions=[vector(10,0),vector(-10,0),vector(0,10),vector(0,-10)]
    move_direction=directions[randrange(len(directions))]
    new_food_pos=food + move_direction

    if inside(new_food_pos):
        food.move(move_direction)

    ontimer(move_food,1000)

def color():
    global color_snake, color_food
    color_snake = choice(colors_list)  
    color_food = choice(colors_list)

    # Asegurar que la comida y la serpiente no tengan el mismo color
    while color_food == color_snake:
        color_food = choice(colors_list)


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    

    for body in snake:
        square(body.x, body.y, 9, color_snake)

    
    
    square(food.x, food.y, 9, color_food)
    update()
    ontimer(move, 100)



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

color()
move()
move_food()
done()
 
