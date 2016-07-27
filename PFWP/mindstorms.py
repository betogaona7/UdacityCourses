
import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("white")
	#Create the turtle brad - Draw a square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("black")
	brad.speed(8)

	#Draw a circle of squares
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)

	#Create the turtle Angie - Draw a circle
	angie = turtle.Turtle()
	angie.shape("turtle")
	angie.color("green")
	angie.circle(100)

	window.exitonclick()

draw_art()