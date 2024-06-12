print("Bem-vindo ao meu quiz!")

playing = input("Você deseja jogar? Escreva 'S' para sim e 'N' para não: ")

answer = playing.upper()

if answer == "S":
    print("\nVamos jogar!")

elif answer == "N":
    print("\nQue pena, nos vemos na proxima.")
    quit()
else:
    print("\nDigite o valor correto.")
    quit()

score = 0
max_score = 5

while answer == 's' or 'S':

    print("\nVocê vai responder 5 questões.")

    print("\nVamos começar com primeira questão!")
    resposta1 = input("Quantos metros possui um quilometro? ")

    print("\nVamos com a segunda questão!")
    resposta2 = input("Quando terminou a segunda guerra mundial? ")

    print("\nVamos com a terceira questão!")
    resposta3 = input("Em que ano o Brasil foi descoberto pelos navegantes portugueses? ")

    print("\nVamos com a quarta questão!")
    resposta4 = input("Qual o valor da raiz quadrada de 25? ")

    print("\nVamos com a quinta questão!")
    resposta5 = input("Quanto é 8x8? ")

    break

if resposta1 == "1000":
    score += 1

if resposta2 == "1945":
    score += 1

if resposta3 == "1500":
    score += 1

if resposta4 == "5":
    score += 1

if resposta5 == "64":
    score += 1

print("\nO jogo acabou. Confira seus acertos ")

if score == max_score:
    print("\nVocê acertou todas as questões, parabéns!")
    print("Seu score é: " + str(score))

else:
    print("\nPodemos melhorar!")
    print("Seu score é: " + str(score))
