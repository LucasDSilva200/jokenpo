import os
import getpass

class Arquivo():
    def __init__(self):
        pass
    def abrirArquivoScore(self):
        user = getpass.getuser()
        if not os.path.exists('C:/Users/'+user+'/Documents/jokenpo/res/score/scores.txt'):
            try:
                os.makedirs('C:/Users/'+user+'/Documents/jokenpo/res/score')
                with open('C:/Users/'+user+'/Documents/jokenpo/res/score/scores.txt','a') as arquivo:
                    add=list()
                    for x in range(10):
                        add.append("0\n")
                        arquivo.writelines(add[x])
            except FileExistsError:
                pass
        user = getpass.getuser()
        os.chdir(r'C:/Users/'+user+r'/Documents/jokenpo/res/score')
        caminho=os.getcwd()+"/scores.txt"
        
        arq = open(caminho, 'r',encoding="utf8")
        info=arq.readlines()
        arq.close()

        return info
    def abrirArquivoUsers(self):
        user = getpass.getuser()
        if not os.path.exists('C:/Users/'+user+'/Documents/jokenpo/res/user/users.txt'):
            try:
                os.makedirs('C:/Users/'+user+'/Documents/jokenpo/res/user')
                with open('C:/Users/'+user+'/Documents/jokenpo/res/user/users.txt','a') as arquivoUser:
                    add=list()
                    for x in range(10):
                        add.append("User\n")
                        arquivoUser.writelines(add[x])
            except FileExistsError:
                pass
        
        user = getpass.getuser()
        os.chdir(r'C:/Users/'+user+r'/Documents/jokenpo/res/user')
        caminho=os.getcwd()+"/users.txt"
        
        arq = open(caminho, 'r',encoding="utf8")
        info=arq.readlines()
        arq.close()

        return info
    
    def event(self):
        user = input("Digite o seu nome de usuário: ")
        return user
    def gravar(self,score,users,pontuacao):
        getuser = getpass.getuser()
        pontos=pontuacao
        for i in range(10):
            self.score = score[i]
            self.user = users[i]
            if int(self.score)<pontos:
                print(self.user) 
                if self.user != ' ':
                    print("if2")
                    valUsr = self.event()
                    self.user=valUsr  
                    self.score = str(pontos)
                    
                    
                    os.chdir(r'C:/Users/'+getuser+'/Documents/jokenpo/res/score')
                    cc = os.getcwd()+"/scores.txt"
                    arqScore = open(cc,'r')
                    linesScore = arqScore.readlines()
                    arqScore.close()
                    
                    
                    os.chdir(r'C:/Users/'+getuser+'/Documents/jokenpo/res/score')
                    cc = os.getcwd()+"/scores.txt"
                    arqScore = open(cc,'w')
                    linesScore.insert(i, self.score + "\n")
                    arqScore.writelines(linesScore)
                    arqScore.close()
                    
                    
                    
                    os.chdir(r'C:/Users/'+getuser+'/Documents/jokenpo/res/user')
                    cc = os.getcwd()+"/users.txt"
                    arqUsers = open(cc,'r')
                    linesUsers = arqUsers.readlines()
                    arqUsers.close()

                    os.chdir(r'C:/Users/'+getuser+'/Documents/jokenpo/res/user')
                    cc = os.getcwd()+"/users.txt"
                    arqUsers = open(cc,'w')
                    linesUsers.insert(i, self.user +"\n")
                    arqUsers.writelines(linesUsers)
                    arqUsers.close()
                    break
        return