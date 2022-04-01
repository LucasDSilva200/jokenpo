import os
import getpass

class Arquivo():
    def __init__(self):
        pass
    def abrirArquivo(self):
        user = getpass.getuser()
        if not os.path.exists('C:/Users/'+user+'/Documents/jokenpo/res/infos.txt'):
            try:
                os.makedirs('C:/Users/'+user+'/Documents/jokenpo/res')
                with open('C:/Users/'+user+'/Documents/jokenpo/res/infos.txt','a') as arquivo:
                    add=list()
                    add.append("0\n")
                    add.append("User")
                    arquivo.writelines(add)
            except FileExistsError:
                pass
        
        user = getpass.getuser()
        os.chdir(r'C:/Users/'+user+r'/Documents/jokenpo/res')
        caminho=os.getcwd()+"/infos.txt"
        
        arq = open(caminho, 'r',encoding="utf8")
        info=arq.readlines()
        arq.close()

        return info
    
    def event(self):
        user = input("Digite o seu nome de usuário: ")
        return user
    def gravar(self,texto,pontuacao):
        user = getpass.getuser()
        self.score = texto[0]
        self.user = texto[1]
        pontos=pontuacao
        if self.user == 'User':
            valUsr = self.event()
            self.user=valUsr
            if int(self.score)<pontos:

                self.score = str(pontos)
                os.chdir(r'C:/Users/'+user+'/Documents/jokenpo/res')
                cc = os.getcwd()+"/infos.txt"
                arq = open(cc,'w')
                texto=arq.writelines(self.score+"\n"+self.user+"\n")
                arq.close()
        else:
            if int(self.score)<pontos:

                self.score = str(pontos)
                os.chdir(r'C:/Users/'+user+'/Documents/jokenpo/res')
                cc = os.getcwd()+"/infos.txt"
                arq = open(cc,'w')
                texto=arq.writelines(self.score+"\n"+self.user+"\n")
                arq.close()
        return