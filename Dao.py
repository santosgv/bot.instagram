import pickle

class Usuario:
    def adiciona(self,user,password):
        try:
            arquivo = open("users.bin", "w+b")
            self.usuarios ={'user':user,'password':password}
            pickle.dump(self.usuarios, arquivo)
            arquivo.close()
            return print('Cadastrado')
        except:
            print('Erro no arquivo')

    def ler(self):
        try:
            arquivo = open("users.bin", "rb")
            users = pickle.load(arquivo)
            print(users)

        except:
            print("Problemas ler o arquivo.")



a=Usuario()
a.ler()