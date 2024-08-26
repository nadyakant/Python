import turtle
import time
import random

############## SET ##############

delay = 0.1

# Set the SCORE to 0
score = 0
high_score = 0

# SCREEN
wn = turtle.Screen()
wn.title("The Snake")
wn.bgcolor("black")  # Background COLOR
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Draw border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-300, -300)
border.pendown()
for _ in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")  # Snake COLOR
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake bait
bait = turtle.Turtle()
bait.speed(0)
bait.shape("circle")
bait.color("red")
bait.penup()
bait.goto(0, 100)

segments = []

# Text box
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Lucida Console", 24, "normal"))

############## FUNCTIONALITY ##############

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

############## GAME LOOP ##############
while True:
    wn.update()
    
############## LOSING ##############

    # Snake head touches the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide body segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear body segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Lucida Console", 24, "normal"))

############## CATCHING THE BAIT ##############

    # Check for a collision with the bait
    if head.distance(bait) < 20:
        # Move the bait to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        bait.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Lucida Console", 24, "normal"))

############## ALIGN SNAKE ##############

    # Segments will move in reverse order - the last added moves first
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

############## RESET ##############

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Lucida Console", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
