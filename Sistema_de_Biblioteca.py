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

