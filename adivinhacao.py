import time
import random

print('***********************')
print("Welcome the game :D")
print('***********************')

def jogar():
  #continuar = input('Voce deseja recomeçar? ')
  #numero_secreto = 37
  numero_secreto = round(random.random()*100)
  total_tentativas = 5
  rodada = 1
  jogador = input("Bem vindo(a) insira seu nome (a):")


  print(f"Olá, {jogador}, o objetivo principal do game, é acertar o número secreto.")
  time.sleep (6)
  print('\n')
  print('Dica: Será mostrado a porcentagem que seu chute representa. Ou seja, seu objetivo é chegar ao 100%. Lembre-se, da simples regrinha :D')
  print('\n')
  time.sleep (6)
  #for value in range (1, 50): 
    #print(f" O número da sorte pode ser esse: {value}") #exibe a opção dos números de 1 à 49
  print('\n')
  print('Lembrando, você tem 5 tentativas.')

  #while rodada <= total_tentativas: #substituindo por for
  for rodada in range(1, total_tentativas + 1):
      #print(f"Tentativa {rodada} 'de' {total_tentativas}") #formatação antiga
      print ("Tentativa {} de {}". format(rodada, total_tentativas))
      chute = int((input("Digite o número sorteado: ")))
      acertou = chute == numero_secreto
      maior = chute > numero_secreto
      quase = chute == 36
      menor = chute < numero_secreto
      porcentagem_chute = (chute/numero_secreto) * 100 #dica para chegar ao resultado, com uma regra de 3 fica easy.

      if acertou :
          print("Parabéns, você acertou!")
          break
    
      else:
          if maior:
              print(f'{jogador},seu chute representa {porcentagem_chute:.0f}% do valor correto. Você errou, seu chute foi maior!')
          elif quase:
            print(f'{jogador}, seu chute representa {porcentagem_chute:.0f}% do valor correto. Você está perto!!')
          elif menor:
              print(f'{jogador}, seu chute representa {porcentagem_chute:.0f}% do valor correto. Você errou, seu chute foi menor.')
          # elif chute == total_tentativas - 1:
            # print(f'Seu chute representa {porcentagem_chute}. Agora ficou fácil')
        
if (__name__ =="__main__"):
  jogar() 

print("Fim do game!") 