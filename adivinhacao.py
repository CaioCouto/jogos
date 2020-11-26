from random import randint
from os import system

def chooseDificulty():
    while(True):
        print('''
            (1) Fácil
            (2) Médio
            (3) Difícil
            (4) Sair
        ''')

        dificulty = int(input('>>> Escolha o nível de dificuldade: '))

        if(dificulty == 1): return 20
        elif(dificulty == 2): return 10
        elif(dificulty == 3): return 5
        elif(dificulty == 4): return 0
        else: print('>>> Oops. Não reconheço esse valor. Tente de Novo\n.')

def jogar():
    lower_limit = 1
    upper_limit = 100
    points = 500

    print('\n*********************************')
    print('Bem vindo ao jogo de Adivinhação!')
    print('*********************************')

    total_tries = chooseDificulty()
    secret_number = randint(lower_limit, upper_limit)

    system('cls')

    if(total_tries != 0): 
        print('Boa sorte!\n')

        for current_round in range(1, total_tries+1):
            print('Rodada {} de {}: \n'.format(current_round, total_tries))
            
            user_choice = int(input(f'>>> Digite um número inteiro de {lower_limit} a {upper_limit}: '))

            got_it_right = user_choice == secret_number
            bigger_number = user_choice > secret_number
            out_of_range = user_choice > upper_limit or user_choice < lower_limit

            if(out_of_range): print(f'>>> Oops. Seu palpite deve ser de {lower_limit} a {upper_limit}! Tente outro.')
            elif(got_it_right): 
                print('>>> Parabéns, Você acertou e fez {} pontos!\n'.format(points))
                break
            elif(bigger_number): print('>>> Você errou! Seu palpite foi mais alto do que o número secreto.')
            else: print('>>> Você errou! Seu palpite foi abaixo do número secreto.')
            
            points = points - abs(secret_number - user_choice)

            if(points <= 0): 
                print('\n>>> Oh, não. Seus pontos chegaram a zero!')
                break
            print('\n')

        if(got_it_right == False): print('>>> Que pena. Você perdeu. O número secreto era: {} :(\n'.format(secret_number))

    print('Fim de Jogo.\n')

if(__name__ == "__main__"): jogar()