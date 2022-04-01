import os

class Arquivo():
    def __init__(self):
        pass
    def abrirArquivo(self):
        os.chdir(r'C:/Users/lucas/Documents/PYTHON/projects/jokenpo-CLS/res')
        caminho=os.getcwd()+"/infos.txt"
        
        arq = open(caminho, 'r',encoding="utf8")
        info=arq.readlines()
        arq.close()

        return info
    
    def event(self):
        user = input("Digite o seu nome de usuário: ")
        return user
    def gravar(self,texto,pontuacao):
        self.score = texto[0]
        self.user = texto[1]
        pontos=pontuacao
        if self.user == 'User':
            valUsr = self.event()
            self.user=valUsr
            if int(self.score)<pontos:

                self.score = str(pontos)
                os.chdir(r'C:/Users/lucas/Documents/PYTHON/projects/jokenpo-CLS/res')
                cc = os.getcwd()+"/infos.txt"
                arq = open(cc,'w')
                texto=arq.writelines(self.score+"\n"+self.user+"\n")
                arq.close()
        else:
            if int(self.score)<pontos:

                self.score = str(pontos)
                os.chdir(r'C:/Users/lucas/Documents/PYTHON/projects/jokenpo-CLS/res')
                cc = os.getcwd()+"/infos.txt"
                arq = open(cc,'w')
                texto=arq.writelines(self.score+"\n"+self.user+"\n")
                arq.close()
        return