import random
import time

OK = '\033[92m' #GREEN
WARNING = '\033[93m' #YELLOW
FAIL = '\033[91m' #RED
RESET = '\033[0m' #RESET COLOR
venceu=False
empate = False
class Game():
    def __init__(self) :
        pass
    
    def VerificarObjetoAdversario(self):
        object=['r','p','s']
        return random.choice(object)
    
    def TratarEscolha(self,object1,object2):
        
        if object1 == 'r':
            print("Você escolheu Pedra\n")
        if object1 == 's':
            print("Você escolheu Tesoura\n")
        if object1 == 'p':
            print("Você escolheu Papel\n")
        
        if object2 == 'r':
            print("O adversário escolheu Pedra\n")
        if object2 == 's':
            print("O adversário escolheu Tesoura\n")
        if object2 == 'p':
            print("O adversário escolheu Papel\n")
        
        time.sleep(2)
          
    def verificar(self,escolhaplayer,escolhadversario,rodada,pontos):
        rodadatual=rodada
        score=pontos
        global venceu
        venceu = False
        global empate
        empate = False
        if escolhaplayer == 'r' and escolhadversario == 'p':
            print(FAIL+"Você perdeu"+RESET)
        if escolhaplayer == 'r' and escolhadversario == 's':
            print(OK+"Você ganhou"+RESET)
            venceu = True
        if escolhaplayer == 'p' and escolhadversario == 's':
            print(FAIL+"Você perdeu"+RESET)
        if escolhaplayer == 'p' and escolhadversario == 'r':
            print(OK+"Você ganhou"+RESET)
            venceu = True
        if escolhaplayer == 's' and escolhadversario == 'r':
            print(FAIL+"Você perdeu"+RESET)
        if escolhaplayer == 's' and escolhadversario == 'p':
            print(OK+"Você ganhou"+RESET)
            venceu = True
        if escolhaplayer ==  escolhadversario:
            print(WARNING+"Foi um empate"+RESET)
            empate = True
        
        if venceu == True:
            score=score + rodadatual*5
            time.sleep(2)
            return score
        elif empate == True:
            score=score + rodadatual*2
            time.sleep(2)
            return score
        elif venceu == False and empate == False:
            time.sleep(2)
            return score
        time.sleep(2)        
        