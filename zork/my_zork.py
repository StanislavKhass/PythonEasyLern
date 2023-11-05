# Introduction narration of game


loop = 4
print("---------------------------------------------------------")
print("Добро пожаловать в Хаск - Официальная версия игры на python")

while True:
	# First Input Loop
	while loop == 4:
		if loop == 4:
			print("---------------------------------------------------------")
			print("Вы стоите в открытом поле, к западу от белого дома с заколоченной дверью")
			print("(Секретный путь ведет на юго-запад в лес.)")
			print("Перед вами маленький почтовый ящик")
			second = input("Что будите делать? ")

		if second.lower() == ("взять почтовый ящик"):
			print("---------------------------------------------------------")
			print("Он надежно закреплен")
		elif second.lower() == ("открыть почтовый ящик"):
			print("---------------------------------------------------------")
			print("Открыв небольшой почтовый ящик, вы найдете листовку")
		elif second.lower() == ("идти на восток"):
			print("---------------------------------------------------------")
			print("Дверь заколоченна и вы не сможете снять доски")
		elif second.lower() == ("открыть дверь"):
			print("---------------------------------------------------------")
			print("Дверь не может быть открыта")
		elif second.lower() == ("взять доски"):
			print("---------------------------------------------------------")
			print("Доски надежно закрепленны")
		elif second.lower() == ("посмотреть на дом"):
			print("---------------------------------------------------------")
			print("Дом представляет собой красивый колониальный дом, выкрашенный в белый цвет. Понятно, что владельцы должны были быть очень богатыми")
		elif second.lower() == ("идти на юго запад"):
			loop = 8
		elif second.lower() == ("читать листовку"):
			print("---------------------------------------------------------")
			print("Добро пожаловать в Хаск. Ваша миссия найти нефритовую статую")
		else:
			print("---------------------------------------------------------")


	# Southwest Loop
	while loop == 8:
		if loop == 8:
			print("---------------------------------------------------------")
			print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
			forest_inp = input("What do you do? ")

		if forest_inp.lower() == ("go west"):
			print("---------------------------------------------------------")
			print("You would need a machete to go further west.")
		elif forest_inp.lower() == ("go north"):
			print("---------------------------------------------------------")
			print("The forest becomes impenetrable to the North.")
		elif forest_inp.lower() == ("go south"):
			print("---------------------------------------------------------")
			print("Storm-tossed trees block your way.")
		elif forest_inp.lower() == ("go east"):
			loop = 9
		else:
			print("---------------------------------------------------------")


	# East Loop and Grating Input
	while loop == 9:
		if loop == 9:
			print("---------------------------------------------------------")
			print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
			print("There is an open grating, descending into darkness.")
			grating_inp = input("What do you do? ")

		if grating_inp.lower() == ("go south"):
			print("---------------------------------------------------------")
			print("You see a large ogre and turn around.")
		elif grating_inp.lower() == ("descend grating"):
			loop = 10
		else:
			print("---------------------------------------------------------")


	# Grating Loop and Cave Input
	while loop == 10:
		if loop == 10:
			print("---------------------------------------------------------")
			print("You are in a tiny cave with a dark, forbidding staircase leading down.")
			print("There is a skeleton of a human male in one corner.")
			cave_inp = input("What do you do? ")

		if cave_inp.lower() == ("descend staircase"):
			loop = 11
		elif cave_inp.lower() == ("take skeleton"):
			print("---------------------------------------------------------")
			print("Why would you do that? Are you some sort of sicko?")
		elif cave_inp.lower() == ("smash skeleton"):
			print("---------------------------------------------------------")
			print("Sick person. Have some respect mate.")
		elif cave_inp.lower() == ("light up room"):
			print("---------------------------------------------------------")
			print("You would need a torch or lamp to do that.")
		elif cave_inp.lower() == ("break skeleton"):
			print("---------------------------------------------------------")
			print("I have two questions: Why and With What?")
		elif cave_inp.lower() == ("go down staircase"):
			loop = 11
		elif cave_inp.lower() == ("scale staircase"):
			loop = 11
		elif cave_inp.lower() == ("suicide"):
			print("---------------------------------------------------------")
			print("You throw yourself down the staircase as an attempt at suicide. You die.")
			print("---------------------------------------------------------")
			suicide_inp = input("Do you want to continue? Y/N ")
			if suicide_inp.lower() == ("n"):
				exit()
			if suicide_inp.lower() == ("y"):
				loop = 4
		elif cave_inp.lower() == ("scale staircase"):
			loop = 11
		else:
			print("---------------------------------------------------------")


	# End of game
	while loop == 11:
		if loop == 11:
			print("---------------------------------------------------------")
			print("You have entered a mud-floored room.")
			print("Lying half buried in the mud is an old trunk, bulging with jewels.")
			last_inp = input("What do you do? ")

		if last_inp.lower() == ("open trunk"):
			print("---------------------------------------------------------")
			print("You have found the Jade Statue and have completed your quest!")
		else:
			print("---------------------------------------------------------")

		# Exit loop at the end of game
		exit_inp = input("Do you want to continue? Y/N ")
		if exit_inp.lower() == ("n"):
			exit()
		if exit_inp.lower() == ("y"):
			loop = 4
