class Biblioteca: 
    def __init__(self):
        self.leitores= []
        self.livros=[]

    def cadastrar_leitor(self,leitor):
        self.leitores.append(leitor)

    def cadastrar_livro(self,livro):
        self.livros.append(livro)

    def buscar_leitor(self,nome):
        for leitor in self.leitores: 
            if leitor.nome.lower()== nome.lower():
                return leitor
            
    def buscar_livro(self,titulo):
        for livro in self.livros:
            if livro.titulo.lower()== titulo.lower():
                return livro
            return None

    def consultar_acervo (self):
        print("          Acervo   ")       

        if len(self.livros)==0:
            print(" Nenhum livro cadastrado. ")
            return
        if livro in self.livros:
            livro.mostrar_informacoes()

    def pesquisar_livro(self,titulo):
        encontrados=[]
        for livro in self.livros:
            if titulo.lower()in livro.titulo.lower():
                encontrados.append(livro)
        return encontrados 

    def remover_livro (self):
        livro= self.buscar_livro(titulo)
        if livro is None:
            print("Livro não encontrado.")
            return
        if not livro.disponivel:
            print("Não é possivrl remover o livro emprestado.")
            return
        livro.disponivel=False

        leitor.historico.append({"Título": livro.titulo "autor: " livro.autor, "status: " "Emprestado" })
        print("Emprestimo realizado com sucesso")

    def devolver_livro(self,titulo):
        livro= self.buscar_livro(titulo)
        if livro is None: 
            print("Livro não encontrado")
            return
        if livro.disponivel:
            print("Esse livro já esta disponivel")
            return
        livro.disponivel=True 

        for leitor in self.leitores:
            for registro in leitor.historico:
                if (registro["Título"].lower()== livro.titulo.lower()and registro["status"]=="Emprestado"):
                    registro["status"] = "Devolvido"
        print("Livro devolvido com sucesso!")

        
        