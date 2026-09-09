

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
# Cadastro do administrador


