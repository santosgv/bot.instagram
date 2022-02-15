import pickle
from threading import *
class Usuario:
    def ler(self):
        try:

            with open("Contas.txt", 'r', encoding='utf-8') as arq:
                users = arq.readlines()
                users = list(map(lambda x: x.replace('\n', ''), users))
                users = list(map(lambda x: x.split(','), users))
                i= 0
                while (i < len(users)):
                    print(users[i][0]+'login')
                    print(users[i][1] + 'senha')
                    i = i+1
                    return  users[i][1]




        except:
            print("Problemas ler o arquivo.")

    def threading(self):
        t1 = Thread(target=self.logar)
        t1.start()



