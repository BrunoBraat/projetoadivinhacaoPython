print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentivas = 3
'rodada = 1'

"""while(rodada <= total_de_tentivas):
    print("Tentativa {} de {}".format(rodada, total_de_tentivas))
    chute_string = input("Digite o seu numero: ")
    chute = int(chute_string)
    print("Voce digitou o numero", chute_string)

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if(acertou):
        print("Voce acertou!")
    else:
        if(chute_maior):
            print("Errou! O seu chute foi maior do que número secreto.")
        elif(chute_menor):
            print("Errou! O seu chute foi menor do que número secreto.")

    rodada  = rodada + 1

print("Fim do jogo")"""

'#Usando for'
'o Range ira selecionar um derterminado alcance entre 1 e 3(valor da variavel total_de_tentivas'
for rodada in range(1, total_de_tentivas + 1):
    'Incluimos + 1 devido a função range que exlui o ultimo numero na hora de imprimir'
    print("Tentativa {} de {}".format(rodada, total_de_tentivas))
    chute_string = input("Digite um numero entre 1 e 100: ")
    chute = int(chute_string)
    print("Voce digitou o numero", chute_string)

    if(chute <= 0 or chute >= 100):
        print("Voce deve digitar um valor entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if(acertou):
        print("Voce acertou!")
        break
    else:
        if(chute_maior):
            print("Errou! O seu chute foi maior do que número secreto.")
        elif(chute_menor):
            print("Errou! O seu chute foi menor do que número secreto.")

print("Fim do jogo")