# -*- coding:utf-8 -*-
from sys import exit	#����ϵͳexit����
#���庯��
def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = raw_input(">")
	if "0" in next or "1" in next:
			how_much = int(next)
	else:
		dead("Man,learn to type a number.") #����dead����
	
	
	if how_much < 50:
		print "Nice,you're not greedy,you win!"
		exit(0)
	else:
		dead("You greedy bastard!") #����dead����
#���庯��		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	#whileѭ��Ƕ��ifѭ��
	while True:
		next = raw_input(">")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door.You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()	#���ú���
		else:
			print "I got no idea what that means."

#���庯��			
def cthulh_room():
	print "Here you see the great evil Cthulhu."
	print "He,it,whatever startes at you and you go insane."
	print "Do you flee for your life or eat your head?"
	#if�ж�
	next = raw_input(">")
	if "flee" in next:
		start()	#����start����
	elif "head" in next:
		dead("Well that was tasty!")  #����dead����
	else:
		cthulhu_room()	#���ú���
	
#���庯��
def dead(why):
	print why,"Good job!"
	exit()	#����ϵͳexit����
#���庯��
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input(">")
	#if�ж�
	if next == "left":
		bear_room() 	#���ú���
	elif next == "right":
		cthulhu_room()	#���ú��� 
	else:
		dead("You stumble around the room until you starve.")

start()#���ú���
