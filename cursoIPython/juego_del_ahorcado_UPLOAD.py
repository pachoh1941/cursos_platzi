import random
import os


def read_data(): #Data must be in the same folder
    words = []
    with open("./data.txt","r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    return words


def display_setup(number_of_letters):
    display = {}
    for i in range(number_of_letters):
        display[i] = '_'
    return display


def play(database,lifes):
    alive = True
    word = random.choice(database)
    playing_word = dict(enumerate(word))
    playing_word.pop(len(playing_word)-1) #Eliminates de line step \n from the word
    length = len(playing_word)
    display = display_setup(length)

    #Variable to be returned upon playing
    param_return = {}

    while alive == True:
        while lifes > 0:
            os.system("cls")

            #Game Display
            if display == playing_word:
                param_return = {0:alive, 1:word}
                return param_return
            game_display = ""
            for i in range(len(display)):
                game_display += str(display.get(i)).upper() + " "
            life_display = "Tienes " + str(lifes) + " vidas\n" +"❤" * lifes
            print(life_display ,"\n\nAdivina la palabra\n\n", game_display)
        
            #Backend
            letter_guess = input("\n Inserta una letra: ")
            test = [i for i in range(length) if letter_guess == playing_word[i]]
            if len(test) == 0:
                lifes -= 1
            else:
                for i in test:
                    display[i] = playing_word[i]
        if lifes == 0:
            alive = False

        param_return = {0:alive, 1:word}
    
    return param_return
    

def run():
    #Loading word data file to the game
    words = []
    words = read_data()
    game_status = []
    playing_word = ''
    
    easy_words = [word for word in words if len(word) <= 5]
    hard_words = [word for word in words if len(word) <= 7 and len(word) >= 6]
    legend_words = [word for word in words if len(word) >= 7]

    difficulty = int(input("""
BIENVENIDO AL JUEGO DEL AHORCADO
Escoge la dificultad del juego:
1 - Fácil
2 - Difícil
3 - Legendario
Escribe el número que corresponde: """))
    if difficulty == 1:
        game_status = play(easy_words,10)
    if difficulty == 2:
        game_status = play(hard_words,10)
    if difficulty == 3:
        game_status = play(legend_words,10)

    playing_word = game_status[1].upper()

    VICTORY = '¡GANASTE!'
    LOSS = '¡PERDISTE! Tu palabra era ' + playing_word
    
    if game_status[0] == True:
        os.system("cls")
        print(VICTORY)
    else:
        os.system("cls")
        print(LOSS)
    

if __name__=='__main__':
    run()