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