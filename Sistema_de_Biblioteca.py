class Pessoa:
    def __init__(self, nome, idade, telefone, email):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")

class Leitor(Pessoa):
    def __init__(self, nome, idade, telefone, email):
        super().__init__(nome, idade, telefone, email)
        self.historico = []

    def mostrar_informacoes(self):
        print("\n----- DADOS DO LEITOR -----")
        super().mostrar_informacoes()
        print(f"Quantidade de empréstimos: {len(self.historico)}")

    def mostrar_historico(self):
        print("\n---- HISTÓRICO DE LIVROS ----")

        if len(self.historico) == 0:
            print("O leitor ainda não possui histórico.")
            return

        for i, livro in enumerate(self.historico, 1):
            print(f"\n{i} - {livro['titulo']}")
            print(f" Autor: {livro['autor']}")
            print(f" Status: {livro['status']}")


class Livro:
    def __init__(self,titulo,autor,ano_publicacao,numero_paginas,editora,genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.editora = editora
        self.genero = genero
        self.disponivel = True

    def mostrar_informacoes(self):
        print("\n------------------------------")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de publicação: {self.ano_publicacao}")
        print(f"Número de páginas: {self.numero_paginas}")
        print(f"Editora: {self.editora}")
        print(f"Gênero: {self.genero}")

        if self.disponivel:
            print("Status: Disponível")
        else:
            print("Status: Emprestado")


class Administrador(Pessoa):
    def __init__(self,nome,idade,telefone, email,matricula):
        super().__init__( nome,idade,telefone, email)
        self.matricula = matricula


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

        if len(self.livros) == 0:
            print(" Nenhum livro cadastrado. ")
            return
        for livro in self.livros:
            livro.mostrar_informacoes()

    def pesquisar_livro(self,titulo):
        encontrados=[]
        for livro in self.livros:
            if titulo.lower()in livro.titulo.lower():
                encontrados.append(livro)
        return encontrados 

    def remover_livro (self,titulo):
        livro= self.buscar_livro(titulo)
        if livro is None:
            print("Livro não encontrado.")
            return
        if not livro.disponivel:
            print("Não é possivel remover o livro emprestado.")
            return
        livro.disponivel=False

        print("Emprestimo realizado com sucesso")

    def emprestar_livro(self,nome_leitor,titulo):

        leitor=self.buscar_leitor(nome_leitor)

        if leitor is None:
            print("Leitor não encontrado")
            return
        livro=self.buscar_livro(titulo)
        if livro is None:
            print("Livro não encontrado")
            return
        if not livro.disponivel:
            print("Esse livro já está emprestado")
            return

        livro.disponivel=False
        leitor.historico.append({"Titulo": livro.titulo, "Autor": livro.autor, "Status": "Emprestado"})
        print("\nEmprestima realizado com sucesso!")


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

def  ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas numeros.")

def cadastrar_novo_leitor(Biblioteca):
    print("\n================================")
    print("        CADASTRO DE LEITOR        ") 
    print("==================================")

    nome=input("Nome: ")

    if biblioteca.buscar_leitor(nome) is not None:
        print("\n Esse leitor já está cadastrado. ")
        return

    idade= ler_inteiro("idade: ")
    telefone=  input("Telefone: ")
    email= input("E-mail: ")

    leitor=Leitor(nome,idade,telefone,email)

    biblioteca.cadastrar_leitor(leitor)
    print("\nLeitor cadastrado com sucesso!")


def cadastrar_novo_livro(biblioteca):
    print("\n================================")
    print("        CADASTRO DE LIVRO         ") 
    print("==================================")

    titulo=input("Título: ")
    if biblioteca.buscar_livro(titulo) is not None:
        print("\nEsse livro já está cadastrado.")
        return

    autor=input("Autor; ")
    ano=ler_inteiro("Ano de pulblicação: ")
    paginas= ler_inteiro("Numero de páginas: ")
    editora=input("Editora: ")
    genero=input("Genero literário: ")

    livro=Livro(titulo, autor, ano, paginas, editora, genero)

    biblioteca.cadastrar_livro(livro)
    print("\nLivro cadastrado com sucesso!")


Leitor1 = Leitor("Manuel Silva de Oliveira", "48", "55 77 99106-9024", "manuelsilvadeoliveira169@gmail.com")
administrador = Administrador("Alan Silva De Oliveira",30,"(77) 99999-0000","alansilvadeoliveira169@gmail.com","ADM123")

livro1 = ("Star Wars: A Vingança dos Sith (Episódio III) – Edição de luxo", "MATTHEW STOVER", 2025, 400, "Universo Geek","Ficção científica")
livro2 = ("Star Wars: The Mandalorian – Como deve ser", "Christopher Nicholas",2026 ,32,"Uni Jr","Literatura infantil e Infantojuvenil")
livro3 = ("A Metamorfose","Franz Kafka",1915,96,"Editora Principis","Novela, Ficção fantástica e Ficção do absurdo")
livro4 = ("O Senhor dos Anéis: A Sociedade do Anel","J. R. R. Tolkien",1954 ,434,"HarperCollins Brasil,""Fantasia épica e Romance de Aventura")