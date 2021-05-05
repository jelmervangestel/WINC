# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
""""Part One"""
first= 'Ruud Gullit'
second= 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = str(first) + ' ' + str(goal_0) + ', ' + str(second) + ' ' + str(goal_1)
print(scorers)

report = f"{first} scored in the {goal_0}nd minute\n{second} scored in the {goal_1}th minute"
print(report)


""""Part Two"""
player = "Ruud Gullit"

first_name = player[:player.find(" ")] #Voornaam loopt tot spatie
print(first_name)

last_name_len = len(player[player.find(" "):])-1 #Lengte achternaam vanaf eerste spatie
print(last_name_len)

name_short = f"{first_name[0]}. {player[-last_name_len:]}" #Eerste letter plus volledige achternaam
print(name_short)

chant = (f"{first_name}! " * len(first_name))[:-1]
print(chant)

good_chant = chant[-1] != " "
print(good_chant)
