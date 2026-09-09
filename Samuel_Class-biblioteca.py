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