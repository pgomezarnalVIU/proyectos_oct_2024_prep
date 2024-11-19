import os
import random
import readchar

my_name = input("escribe tu nick de entrenador\n")

#Definition of the general variables
POSITION_IN_X = 0
POSITION_IN_Y = 1

map_environment = """\
██████████████████████████████████████████████████
            █████████████████           ██████████
█████████   █████████████████████████   ██████████
█████████   █████████████████████████            █ 
█████████                                        █ 
██                                               █ 
█         █████████████   ██████████████████    ██
█    ██████████████████   ██████████████████    ██
~╦  ╦~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~╦  ╦~~
~╬  ╬~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~╬  ╬~~
~╩  ╩~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~╩  ╩~~
█   ██████   ██████████   ███████████████████   ██
██   █████   ██████████                         ██
██           ██████████   █████████    ███████████
█████   ███████████████   █████████    ███████████
█████                     █████████    ███████████
█████   ███████████████   █████████              █
        ███████████████      █████████████████   █
        ███████████████      █████████████████   █
██████████████████████████████████████████████████\
"""
my_position = [0,1]
num_of_trainers = (random.randint(7, 10))
pokemon_trainers = []

#comprehesion of map into lists
map_environment = [list(row) for row in map_environment.split("\n")]

MAP_WIDTH = len(map_environment[0])
MAP_HEIGHT = len(map_environment)

#generate Trainers

while num_of_trainers > len(pokemon_trainers):
    pokemon_trainers.append([random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)])

    new_trainer = pokemon_trainers[-1]
    new_trainer_in_x = new_trainer[0]
    new_trainer_in_y = new_trainer[1]
    char_to_mod = map_environment[new_trainer_in_y][new_trainer_in_x]

    # Check if isnt a obstacle in cell to draw new trainer
    if char_to_mod == " ":
        map_environment[new_trainer_in_y][new_trainer_in_x] = "×"
    else:
        pokemon_trainers.pop()


#Main Loop
lose = False
while lose == False:
    #Map Draw
    os.system("cls")

    print("╔" + "═" * MAP_WIDTH + "╗\n"
        "║▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄[Laberinto Pokemon]▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄║")

    for coordinate_y in range(MAP_HEIGHT):
        print("║", end="")

        for coordinate_x in range(MAP_WIDTH):
            character_to_draw = " "
            object_in_cell = None

            if map_environment[coordinate_y][coordinate_x] == "×":
                character_to_draw = "×" #Enemy character
                object_in_cell = map_environment
            if map_environment[coordinate_y][coordinate_x] == "█":
                character_to_draw = "█" #Obstacle character
            if map_environment[coordinate_y][coordinate_x] == "~":
                character_to_draw = "~" #Water character
            if map_environment[coordinate_y][coordinate_x] == "╦":
                character_to_draw = "╦" #Bridge character
            if map_environment[coordinate_y][coordinate_x] == "╬":
                character_to_draw = "╬" #Bridge character
            if map_environment[coordinate_y][coordinate_x] == "╩":
                character_to_draw = "╩" #Bridge character
            if my_position[POSITION_IN_X] == coordinate_x and my_position[POSITION_IN_Y] == coordinate_y:
                character_to_draw = "®" #Player character

                if object_in_cell: #Redraw to remove the enemy character
                    x_in_x = my_position[0]
                    x_in_y = my_position[1]
                    map_environment[x_in_y][x_in_x] = " "

                    #Pokemon fight

                    #Define values of pokemon of trainers (max 10 trainers defined by var: num_of_trainers)
                    TRAINER_NAMES = [my_name, "Pedro", "Pablo", "Manuel", "Isa", "Sofia", "Tomas", "Ana", "José",
                                     "Adrian", "Maria", "Karen"]
                    POKEMON_NAMES = ["Pikachu", "Vulpix", "Mankey", "Machop", "Onix", "Cubone", "Hitmonchan",
                                     "Bulbasaur", "Squirtle", "Charmander", "Pidgey", "Lugia"]
                    PS_VALUES = [150, 100, 110, 120, 130, 100, 100, 100, 100, 110, 90, 130]
                    ATK_WEAK_VALUES = [20, 20, 18, 16, 14, 20, 20, 20, 20, 18, 22, 16]
                    ATK_STRONG_VALUES = [30, 30, 27, 24, 21, 30, 30, 30, 30, 27, 33, 24]
                    ATK_WEAK_NAMES = ["Chispa", "Roer", "Patada baja", "Patada", "Cabezazo", "Placaje", "Jab",
                                      "Hoja afilada", "Burbuja", "Llama", "Picotear", "Garra dragon"]
                    ATK_STRONG_NAMES = ["Trueno", "Llamarada", "Punio infalible", "Golpe dinamico", "Impacto pesado"
                                        "Hueso Abrumador", "Uppercut", "Latigo cepa", "Pistola agua", "Ascuas",
                                        "Tornado", "Hiper Rayo"]
                    DODGE_SKILL = [4, 4, 3, 2, 1, 4, 4, 4, 4, 3, 5, 2]
                    AIM_SKILL = [4, 3, 4, 5, 6, 3, 3, 3, 3, 4, 2, 5]
                    PIKACHU_KAOMOJI = "ϞϞ૮(๑⚈ ․̫ ⚈๑)ა"
                    ENEMY_KAOMOJI = " (￣▵—▵￣)ƶƵ"
                    # Define the index of enemy
                    new_enemy_index = random.randint(1, len(pokemon_trainers) - 1 )
                    initial_ps_enemy = PS_VALUES[new_enemy_index]
                    initial_ps_pikachu = PS_VALUES[0]
                    ps_pikachu = PS_VALUES[0]
                    ps_enemy = PS_VALUES[new_enemy_index]

                    os.system("cls")
                    combat = True
                    while combat == True:
                        # draw the combat screen
                        print("╔" + "═" * MAP_WIDTH + "╗\n"
                            "║▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄[Combate Pokemon]▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄║\n"
                            "║" + ("█" * MAP_WIDTH) + "║\n"
                            "║" + " " * (MAP_WIDTH - len(POKEMON_NAMES[new_enemy_index])) +
                              POKEMON_NAMES[new_enemy_index] + "║\n"  # pokemon enemy´s name
                            "║" + (" " * (MAP_WIDTH - 3 - (len(str(PS_VALUES[new_enemy_index]))))) + "PS:" +
                               str(ps_enemy) + "║\n"  # PS VALUE
                            "║" + " " * MAP_WIDTH + "║\n"
                            "║" + (" " * (MAP_WIDTH - (len(ENEMY_KAOMOJI) + 2))) + ENEMY_KAOMOJI + "║\n"  # pokemon enemy´s face
                            "║" + " " * MAP_WIDTH + "║\n"
                            "║" + POKEMON_NAMES[0] + (" " * (MAP_WIDTH - len(POKEMON_NAMES[0]))) + "║\n"  # Pikachu´s name
                            "║" + "PS:"+ str(ps_pikachu) + (" " * (MAP_WIDTH - 3 - (len(str(PS_VALUES[0]))))) + "║\n"  # Pikachu´s PS
                            "║" + (" " * MAP_WIDTH) + "║\n"
                            "║" + PIKACHU_KAOMOJI + (" " * (MAP_WIDTH - len(PIKACHU_KAOMOJI))) + "║\n"  # Pikachu´s face
                            "║" + ("_" * MAP_WIDTH) + "║\n"
                            "║" + ("█" * MAP_WIDTH) + "║\n"
                            "╚" + "═" * MAP_WIDTH + "╝\n")
                        input("\nenter para empezar el combate")

                        while PS_VALUES[0] > 0 and PS_VALUES[new_enemy_index] or len(pokemon_trainers) > 0:
                            #enemy´s turn
                            print("Turno de {}\n".format(TRAINER_NAMES[new_enemy_index]))
                            enemys_attack = random.randint(1, 4) #random select to enemy´s action
                            enemys_defence = 0 #increase dodge ability
                            enemys_speed = 0 #increase hitting ability
                            pikachus_defence = 0 #increase dodge ability
                            pikachus_speed = 0 #increase hitting ability

                            if enemys_attack == 1: #weak attack
                                print("{} usa {}:".format(POKEMON_NAMES[new_enemy_index], ATK_WEAK_NAMES[new_enemy_index]))
                                if (((DODGE_SKILL[0] + pikachus_defence) + random.randint(1, 5))
                                        < ((AIM_SKILL[new_enemy_index] + enemys_speed) + random.randint(1 , 5))):
                                    ps_pikachu -= ATK_WEAK_VALUES[new_enemy_index]
                                    print("ha dado en el blanco")
                                else:
                                    print("{} ha esquivado el ataque".format(POKEMON_NAMES[0]))
                            elif enemys_attack == 2: #strong attack
                                print("{} usa {}:".format(POKEMON_NAMES[new_enemy_index], ATK_STRONG_NAMES[new_enemy_index]))
                                if (((DODGE_SKILL[0] + pikachus_defence) + random.randint(1, 5))
                                        < ((AIM_SKILL[new_enemy_index] + enemys_speed) + random.randint(1 , 5))):
                                    ps_pikachu -= ATK_STRONG_VALUES[new_enemy_index]
                                    print("Ha sido un golpe limpio")
                                else:
                                    print("{} lo ha esquivado por los pelos".format(POKEMON_NAMES[0]))
                            elif enemys_attack == 3: #increase hitting ability
                                print("{} ha usado velocidad, ahora tendra mas chance de acestar un "
                                      "golpe".format(POKEMON_NAMES[new_enemy_index]))
                                enemys_speed += random.randint(1,3)
                            elif  enemys_attack == 4: #increase dodge ability
                                print("{} ha usado escudo, ahora podra esquivar un golpe mas "
                                      "facil".format(POKEMON_NAMES[new_enemy_index]))
                                enemys_defence += random.randint(1,3)
                            input("\nenter para seguir")

                            os.system("cls")
                            #redraw the combat screen
                            print("╔" + "═" * MAP_WIDTH + "╗\n"
                                "║▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄[Combate Pokemon]▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄║\n"
                                "║" + ("█" * MAP_WIDTH) + "║\n"
                                "║" + " " * (MAP_WIDTH - len(POKEMON_NAMES[new_enemy_index])) +
                                  POKEMON_NAMES[new_enemy_index] + "║\n"  # pokemon enemy´s name
                                "║" + (" " * (MAP_WIDTH - 3 - (len(str(PS_VALUES[new_enemy_index]))))) + "PS:" +
                                  str(ps_enemy) + "║\n"  # PS VALUE
                                "║" + " " * MAP_WIDTH + "║\n"
                                "║" + (" " * (MAP_WIDTH - (len(ENEMY_KAOMOJI) + 2))) + ENEMY_KAOMOJI + "║\n"  # pokemon enemy´s face
                                "║" + " " * MAP_WIDTH + "║\n"
                                "║" + POKEMON_NAMES[0] + (" " * (MAP_WIDTH - len(POKEMON_NAMES[0]))) + "║\n"  # Pikachu´s name
                                "║" + "PS:" + str(ps_pikachu) + (" " * (MAP_WIDTH - 3 - (len(str(PS_VALUES[0]))))) + "║\n"  # Pikachu´s PS
                                "║" + (" " * MAP_WIDTH) + "║\n"
                                "║" + PIKACHU_KAOMOJI + (" " * (MAP_WIDTH - len(PIKACHU_KAOMOJI))) + "║\n"  # Pikachu´s face
                                "║" + ("_" * MAP_WIDTH) + "║\n"
                                "║" + ("█" * MAP_WIDTH) + "║\n"
                                "╚" + "═" * MAP_WIDTH + "╝\n")
                            if ps_pikachu <= 0:
                                os.system("cls")
                                print("\nhas perdido el combate, fin del juego")
                                lose = True
                                break

                            #User´s turn
                            users_choice = input("Turno de atacar de Pikachu,¿que deseas hacer?\n"
                                            "[z]{}   [x]{}   [c]escudo   "
                                                 "[v]velocidad".format(ATK_WEAK_NAMES[0], ATK_STRONG_NAMES[0]))
                            while (users_choice != "z" and users_choice != "x" and users_choice != "c" and
                                   users_choice != "v"):
                                users_choice = input("Turno de atacar de Pikachu,¿que deseas hacer?\n"
                                                     "[z]{}   [x]{}   [c]escudo   \n"
                                                     "[v]velocidad".format(ATK_WEAK_NAMES[0], ATK_STRONG_NAMES[0]))
                            if users_choice == "z":
                                print("Pikachu usa {}".format(ATK_WEAK_NAMES[0]))
                                if (((DODGE_SKILL[new_enemy_index] + enemys_defence) + random.randint(1,5)) <=
                                        ((AIM_SKILL[0] + pikachus_speed) + random.randint(1,5))):
                                    ps_enemy -= ATK_WEAK_VALUES[0]
                                    print("ha dado en el blanco")
                                else:
                                    print("{} ha esquivado tu ataque".format(POKEMON_NAMES[new_enemy_index]))
                            elif users_choice == "x":
                                print("Pikachu usa {}".format(ATK_STRONG_NAMES[0]))
                                if (((DODGE_SKILL[new_enemy_index] + enemys_defence) + random.randint(1,5)) <=
                                        ((AIM_SKILL[0] + pikachus_speed) + random.randint(1,5))):
                                    ps_enemy -= ATK_STRONG_VALUES[0]
                                    print("eso ha tenido que doler")
                                else:
                                    print("{} Se ha escapado por poco".format(POKEMON_NAMES[new_enemy_index]))
                            elif users_choice == "v":
                                pikachus_speed += random.randint(1,3)
                                print("Pikachu es mas veloz y golpeara con mas facilidad")
                            elif users_choice == "c":
                                pikachus_defence += random.randint(1,3)
                                print("{} ahora es mas duro, sera mas dificil que te golpeen".format(POKEMON_NAMES[0]))
                            if ps_enemy <= 0:
                                os.system("cls")
                                pokemon_trainers.remove(pokemon_trainers[new_enemy_index])
                                TRAINER_NAMES.remove(TRAINER_NAMES[new_enemy_index])
                                POKEMON_NAMES.remove(POKEMON_NAMES[new_enemy_index])
                                PS_VALUES.remove(PS_VALUES[new_enemy_index])
                                ATK_WEAK_VALUES.remove(ATK_WEAK_VALUES[new_enemy_index])
                                ATK_STRONG_VALUES.remove(ATK_STRONG_VALUES[new_enemy_index])
                                ATK_WEAK_NAMES.remove(ATK_WEAK_NAMES[new_enemy_index])
                                ATK_STRONG_NAMES.remove(ATK_STRONG_NAMES[new_enemy_index])
                                DODGE_SKILL.remove(DODGE_SKILL[new_enemy_index])
                                AIM_SKILL.remove(AIM_SKILL[new_enemy_index])
                                os.system("cls")
                                print("\nhas ganado el combate :D")
                                break
                            input("\nenter para seguir")

                            os.system("cls")
                            # redraw the combat screen
                            print("╔" + "═" * MAP_WIDTH + "╗\n"
                                "║▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄[Combate Pokemon]▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄║\n"
                                "║" + ("█" * MAP_WIDTH) + "║\n"
                                "║" + " " * (MAP_WIDTH - len(POKEMON_NAMES[new_enemy_index])) +
                                  POKEMON_NAMES[new_enemy_index] + "║\n"  # pokemon enemy´s name
                                "║" + (" " * (MAP_WIDTH - 3 - (len(str(PS_VALUES[new_enemy_index]))))) + "PS:" +
                                  str(ps_enemy) + "║\n"  # PS VALUE
                                "║" + " " * MAP_WIDTH + "║\n"
                                "║" + (" " * (MAP_WIDTH - (len(ENEMY_KAOMOJI) + 2))) + ENEMY_KAOMOJI + "║\n"  # pokemon enemy´s face
                                "║" + " " * MAP_WIDTH + "║\n"
                                "║" + POKEMON_NAMES[0] + (" " * (MAP_WIDTH - len(POKEMON_NAMES[0]))) + "║\n"  # Pikachu´s name
                                "║" + "PS:" + str(ps_pikachu) + (" " * (MAP_WIDTH - 3 - (len(str(PS_VALUES[0]))))) +
                                  "║\n"  # Pikachu´s PS
                                "║" + (" " * MAP_WIDTH) + "║\n"
                                "║" + PIKACHU_KAOMOJI + (" " * (MAP_WIDTH - len(PIKACHU_KAOMOJI))) + "║\n"  # Pikachu´s face
                                "║" + ("_" * MAP_WIDTH) + "║\n"
                                "║" + ("█" * MAP_WIDTH) + "║\n"
                                "╚" + "═" * MAP_WIDTH + "╝\n")
                        combat = False

            if lose == True:
                break




            print("{}".format(character_to_draw), end="")
        if lose == True:
            break
        print("║")
    if lose == True:
        break
    print("╚" + "═" * MAP_WIDTH + "╝")
    print("Controles: [wasd] para mover [q] para salir")
    if len(pokemon_trainers) < 2:
        print("\nFelicidades, has completado el desafio")

    #Movement (wasd)

    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POSITION_IN_X],(my_position[POSITION_IN_Y] - 1)]
    elif direction == "s":
         new_position = [my_position[POSITION_IN_X], (my_position[POSITION_IN_Y] + 1)]
    elif direction == "a":
        new_position = [(my_position[POSITION_IN_X] - 1), my_position[POSITION_IN_Y]]
    elif direction == "d":
        new_position = [(my_position[POSITION_IN_X] + 1), my_position[POSITION_IN_Y]]
    elif direction == "q":
        break

    if new_position:
        if map_environment[new_position[POSITION_IN_Y]][new_position[POSITION_IN_X]] != "█"\
                and map_environment[new_position[POSITION_IN_Y]][new_position[POSITION_IN_X]] != "~"\
                and map_environment[new_position[POSITION_IN_Y]][new_position[POSITION_IN_X]] != "╦"\
                and map_environment[new_position[POSITION_IN_Y]][new_position[POSITION_IN_X]] != "╬"\
                and map_environment[new_position[POSITION_IN_Y]][new_position[POSITION_IN_X]] != "╩"\
                and map_environment[new_position[POSITION_IN_Y]][new_position[POSITION_IN_X]] != "║":
                    my_position = new_position