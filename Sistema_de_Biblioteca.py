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

Leitor1 = ("Manuel Silva de Oliveira", "48", "55 77 99106-9024", "manuelsilvadeoliveira169@gmail.com")

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

        print("------------------------------")

livro1 = ("Star Wars: A Vingança dos Sith (Episódio III) – Edição de luxo", "MATTHEW STOVER", 2025, 400, "Universo Geek","Ficção científica")
livro2 = ("Star Wars: The Mandalorian – Como deve ser", "Christopher Nicholas",2026 ,32,"Uni Jr","Literatura infantil e Infantojuvenil")
livro3 = ("A Metamorfose","Franz Kafka",1915,96,"Editora Principis","Novela, Ficção fantástica e Ficção do absurdo")
livro4 = ("O Senhor dos Anéis: A Sociedade do Anel","J. R. R. Tolkien",1954 ,434,"HarperCollins Brasil,""Fantasia épica e Romance de Aventura")
class Administrador(Pessoa):
    def __init__(
        self,
        nome,
        idade,
        telefone,
        email,
        matricula
    ):
        super().__init__(
            nome,
            idade,
            telefone,
            email
        )
        self.matricula = matricula

# Cadastro do administrador
administrador = Administrador("Alan Silva De Oliveira",30,"(77) 99999-0000","alansilvadeoliveira169@gmail.com","ADM123")
