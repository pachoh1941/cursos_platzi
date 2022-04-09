import random
import os


def read_data():
    words = []
    with open("./data.txt","r", encoding="utf-8") as f:
        for line in f:
            # line.replace("\n","")
            words.append(line)
    # print (words)
    return words


def display_setup(number_of_letters):
    display = {}
    for i in range(number_of_letters):
        display[i] = '_'
    return display


def play(database,lifes):
    # os.system("cls")
    alive = True
    VICTORY = '¡GANASTE!'
    LOSS = '¡PERDISTE!'
    playing_word = dict(enumerate(random.choice(database)))
    playing_word.pop(len(playing_word)-1)
    length = len(playing_word)
    display = display_setup(length)
    while alive == True:
        # print(playing_word)
        while lifes > 0:
            os.system("cls")

            #Game Display
            if display == playing_word:
                return VICTORY
            game_display = ""
            for i in range(len(display)):
                game_display += str(display.get(i)).upper() + " "
            life_display = "Tienes " + str(lifes) + " vidas\n" +"❤" * lifes
            print(life_display ,"\nAdivina la palabra\n", game_display)
        
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
    
    return LOSS
    

def run():
    #Loading word data file to the game
    words = []
    words = read_data()
    # print(words)

    #Steps of the game:
    #1. Game choses a random word from 'words'
    #2. Game shows to user the game title, number of words (as low-dashes '_'), number of lifes (as heart emojis) an dlevel of difficulty
    #Levels of difficulty will be:
    #   Easy: 10 lifes, maximmum 4 letter words
    #   Hard: 5 lifes, 5 to 6 letter words
    #   Legend: 3 lifes, 6 or more letter words
    #Debugging:
    #   Error if user enters something different form a letter.'

    #Step 1
    easy_words = [word for word in words if len(word) <= 5]
    hard_words = [word for word in words if len(word) <= 7 and len(word) >= 6]
    legend_words = [word for word in words if len(word) >= 7]

    # print(easy_words)
    # print(hard_words)
    # print(legend_words)

    #Step 2
    #Hacer a futuro dos modos de juego para el jugador: continuo o selección de un solo nivel
    difficulty = int(input("""
BIENVENIDO AL JUEGO DEL AHORCADO
Escoge la dificultad del juego:
1 - Fácil
2 - Difícil
3 - Legendario
Escribe el número que corresponde: """))
    if difficulty == 1:
        play(easy_words,10)
    if difficulty == 2:
        play(hard_words,5)
    if difficulty == 3:
        play(legend_words,3)
    

if __name__=='__main__':
    run()