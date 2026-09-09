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
        print("\n================================")
        print("              Acervo              ")
        print("==================================")       

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

        print("Emprestimo realizado com sucesso")
        leitor.historico.append({"Título": livro.titulo, "autor": livro.autor, "status": "Emprestado" })

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

        def alterar_livro (self,titulo):
            livro=self.buscar_livro(titulo)
            if livro is None:
                print("Livro não encontrado")
                return
            if not livro.disponivel:
                print("Não é possivel alterar um livro emprestado.") 
                return

            print("\n================================")
            print("        ALTERAÇÃO DO LIVRO        ") 
            print("==================================")  

            print("Deixe vazio para manter a informção atual. ")  
            novo_titulo= input(f"Informe o novo titulo: {livro.titulo}")
            novo_autor= input(f"Informe o novo autor: {livro.autor}")
            novo_ano= input(f"Informe o novo ano de publicação: {livro.ano_publicacao}") 
            nova_paginas= input(f"Informe o novo numero de páginas: {livro.numero_paginas}") 
            nova_editora= input(f"Informe uma nova editora: {livro.editora}")
            novo_genero= input(f"Informe o novo genero literario:  {livro.genero}")

            if novo_titulo != "": 
                livro.titulo=novo_titulo
            if novo_autor !=  "":
                livro.autor= novo_autor
            if  novo_ano != "":
                livro.ano_publicacao= int(novo_ano)
            if nova_paginas != "": 
                livro.numero_paginas= int(nova_paginas)
            if nova_editora != "":
                livro.editora= nova_editora
            if novo_genero != "":
                livro.genero=novo_genero

            print("Livro alterado com sucesso! ")

        def mostrar_dados (self):
            total_livros = len(self.livros)
            total_leitores=len(self.leitores)   
            livros_disponiveis=0
            livros_emprestados=0

            for livro in self.livros: 
                if livro.disponivel:
                    livros_disponiveis +=1
                else:
                    livros_emprestados +=1

            print("DADOS DA BIBLIOTECA")     
            print(f"Total de livros: {total_livros}")   
            print(f"Livros disponiveis: {livros_disponiveis}")
            print(f"Livros emprestados: {livros_emprestados}")
            print(f"Total de leitores: {total_leitores}")

        
