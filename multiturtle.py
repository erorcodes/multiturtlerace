#!/usr/bin/env python
# coding: utf-8

#Multi turtle race!! 
#Created by erikaetc

import turtle
import random
import time

wn = turtle.Screen()
wn.bgcolor('black')

# Jag vill om möjligt skapa turtlarna utifrån en matris

turtles = list()

lance = turtle.Turtle()
lance.color('red')
lance.shape('turtle')
lance.up()
lance.speed(10)
lance.goto(-290,-40)
lance.down()
lance.name = "Lance"
turtles.append(lance)

andy = turtle.Turtle()
andy.color('blue')
andy.shape('turtle')
andy.up()
andy.speed(10)
andy.goto(-290,-80)
andy.down()
andy.name = "Andy"
turtles.append(andy)

bernt = turtle.Turtle()
bernt.color('green')
bernt.shape('turtle')
bernt.up()
bernt.speed(10)
bernt.goto(-290,-120)
bernt.down()
bernt.name = "Bernt"
turtles.append(bernt)

#for t in turtles:
#	print t.name

# Jag vill: Spara turtlarnas position i en matris
# och sen skapa en if-slinga (?) för att jämföra turtlarnas position...

def no_turtle_finished():
	position = list()
	for t in turtles:
		position.append(t.xcor())
	return max(position) <= 250

def move_turtle(t):
	speed = random.randrange(0,10)
	t.forward(speed)

while no_turtle_finished():
	for t in turtles:
		move_turtle(t)


#print "Lance's finishing position:" + " " + str(lance.xcor()) + ", Andy's finishing position:" + " " + str(andy.xcor())

# print the name of the turtle that won, which is the one that has come furthest

position = list()

print "Results:"

for t in turtles:
	position.append(t.xcor())
	print t.name + " " + str(t.xcor())


print " "

winner = max(position)

for t in turtles:
	if winner == t.xcor():
		print "And the winner is " + t.name + "!!!!!!"
		t.turtlesize(3, 3, 3)

#winner = list()

#def tie():
#	for p in position:
#		if winner == p:
#			return True
	# om antalet turtlar som har vinnarpositionen är fler än en

#if tie():
#	print "IT'S A TIE!! How exciting!"

#else:
#	for t in turtles:
#		if winner == t.xcor():
#			print "And the winner is " + t.name + "!!!!!!"
#			t.turtlesize(3, 3, 3)




# Förstora den vinnande turtlen
# Printa vem som vann


time.sleep(2)
