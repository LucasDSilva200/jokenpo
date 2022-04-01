import util
from util import logica

l = logica.Game()
ss = util.Arquivo()
arq=ss.abrirArquivo()
rodada=0
score=0
def Menu():
    print("-"*35)
    print("Bem-vindo ao meu jokenpô")
    print("- j : Jogar -")
    print("- m : Maior Pontuação -")
    print("- s : Sair -")
    print("-"*35)

def EscolherObjeto():
    while True:
        print("\n"+"-"*35)
        print("- r : Pedra -")
        print("- s : Tesoura -")
        print("- p : Papel -")
        print("- e : sair -")
        print("\n" + "-"*35)
        eo = input("Escolha uma das opções: ")
        if eo not in['r','p','s','e']:
            print("Escolha inválida")
        if eo == 'e':
            break        
        else:
            global rodada 
            global score
            rodada +=1
            adv=l.VerificarObjetoAdversario()
            l.TratarEscolha(eo,adv)
            score=l.verificar(eo,adv,rodada,score)
            print("-"*35+"\n")
            print("Pontuação: ",score)
            print("Rodada: ",rodada)
            print("-"*35+"\n")
            if rodada == 10 :
                ss.gravar(arq,score)
                break
def mostrarMaiorScore():
    while True:
        print("-"*35)
        print("O maior Pontuador: ",arq[1])
        print("O maior score: ",arq[0])
        print("- v : Voltar -")
        print("-"*35)
        v = input("Voltar? ")
        if v !='v':
            print("Escolha inválida")
        else:
            break
while True:
    Menu()
    op = input("Escolha uma das opções: ")
    if op not in['j','s','m']:
        print("Opção Inválida")
        continue
    if op == 'j':
        print("Começando o jogo:")
        EscolherObjeto()
    if op == 'm':
        mostrarMaiorScore()
    if op == 's':
        print("fechando o jogo")
        break


'''
print("Olá mundo")
player = input("Digite a sua opção: ")
print(player)'''