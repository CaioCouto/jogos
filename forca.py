from os import system, getcwd, path
from random import randint

def presentation_message():
    print("*********************************")
    print("   Bem vindo ao jogo da Forca!   ")
    print("*********************************")

def select_secret_word():
    this_folder = getcwd()
    file_path = path.join(this_folder, 'Projetos','Jogos','words.txt')
    words = list()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip().upper()
            words.append(line)

    random_index = randint(0, len(words)-1)
    return words[random_index]

def feedback_to_user(secret, correct_letters, total_mistakes, mistakes):
    missing_letters = correct_letters.count('_')
    tries_remaining = total_mistakes-mistakes

    print(f'Ao todo, a palavra secreta tem {len(secret)} letras!')

    if(missing_letters == 1): print(f'Delas, {missing_letters} falta ser descobertas.\n')
    else: print(f'Delas, {missing_letters} faltam ser descobertas.\n')
    
    print(f'Você tem {tries_remaining} chances para vençer.\n')

def get_user_entry():
    guess = input('Digite uma letra qualquer: ').strip().upper()

    system('cls')

    if(len(guess) > 1): return guess[0]
    elif(guess == ''): 
        print('Você deve digitar uma letra. Tente de novo.\n')
        return 0
    
    return guess

def process_guess(user_guess, secret, correct_letters):
    index = 0
    indexes = list()

    for letter in secret:
        if(letter == user_guess):
            correct_letters[index] = user_guess
            indexes.append(str(index+1))
        index+=1

    found_indexes = ', '.join(indexes)

    if(len(indexes) > 1): print(f'>>> Letra \"{user_guess}\" encontrada nas posições {found_indexes}')
    else: print(f'>>> Letra \"{user_guess}\" encontrada na posição {found_indexes}')

    return correct_letters

def finishing_message(won, secret):
    if(won): 
        print(f'>>> Parabéns, você venceu! A palavra é: {secret}')
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else: 
        print('>>> Que pena, você foi enforcado. :(')
        print(f'>>> A palavra era: {secret}')
        print("    _______________         ")
        print("   /               \\       ")
        print("  /                 \\      ")
        print("//                   \\/\\  ")
        print("\\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \\__      XXX      __/     ")
        print("   |\\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \\_             _/       ")
        print("     \\_         _/         ")
        print("       \\_______/           ")

    print("\nFim do jogo.")

def draw_hangman(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \\     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
    system('cls')

    presentation_message()

    secret = select_secret_word()

    won = False
    hanged = False
    mistakes = 0
    total_mistakes = 7

    correct_letters = list('_' for letter in secret)
    
    while(not won and not hanged):

        feedback_to_user(secret, correct_letters, total_mistakes, mistakes)

        user_entry = get_user_entry()
        
        if(user_entry == 0): continue
        elif(user_entry in secret): 
            correct_letters = process_guess(user_entry, secret, correct_letters)
        else: 
            print(f'>>> Oops. A letra \"{user_entry}\" não foi encontrada!')
            mistakes+=1
        
        draw_hangman(mistakes)

        user_final_string = ''.join(correct_letters)
        won = user_final_string == secret
        hanged = mistakes == total_mistakes
        
        print(user_final_string, end='\n\n')

    system('cls')

    finishing_message(won, secret)

if(__name__ == "__main__"): jogar()