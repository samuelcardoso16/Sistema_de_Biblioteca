def menu_cadastro(biblioteca):
    while True:
        print("\n================================")
        print(" CADASTRO")
        print("================================")

        print("1 - Cadastrar leitor")
        print("2 - Cadastrar livro")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_novo_leitor(biblioteca)

        elif opcao == "2":
            cadastrar_novo_livro(biblioteca)

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")


def menu_administrador(biblioteca):
    print("\n================================")
    print(" ACESSO ADMINISTRADOR")
    print("================================")

    matricula = input("Digite a matrícula: ")

    if matricula != "ADM123":
        print("\nMatrícula incorreta.")
        return

    print("\nAcesso autorizado!")

    while True:
        print("\n================================")
        print(" MENU DO ADMINISTRADOR")
        print("================================")

        print("1 - Cadastrar livro")
        print("2 - Remover livro")
        print("3 - Alterar livro")
        print("4 - Consultar acervo")
        print("5 - Cadastrar leitor")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_novo_livro(biblioteca)

        elif opcao == "2":
            titulo = input(
                "\nDigite o título do livro: "
            )
            biblioteca.remover_livro(titulo)

        elif opcao == "3":
            titulo = input(
                "\nDigite o título do livro: "
            )
            biblioteca.alterar_livro(titulo)

        elif opcao == "4":
            biblioteca.consultar_acervo()

        elif opcao == "5":
            cadastrar_novo_leitor(biblioteca)

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")


def consultar_leitor(biblioteca):
    print("\n================================")
    print(" CONSULTAR LEITOR")
    print("================================")

    nome = input("Digite o nome do leitor: ")

    leitor = biblioteca.buscar_leitor(nome)

    if leitor is None:
        print("\nLeitor não encontrado.")
        return

    leitor.mostrar_informacoes()

    print("\n1 - Ver histórico")
    print("0 - Voltar")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        leitor.mostrar_historico()


def menu_emprestimo(biblioteca):
    print("\n================================")
    print(" EMPRÉSTIMO DE LIVRO")
    print("================================")

    nome = input("Nome do leitor: ")
    titulo = input("Título do livro: ")

    biblioteca.emprestar_livro(
        nome,
        titulo
    )


def menu_devolucao(biblioteca):
    print("\n================================")
    print(" DEVOLUÇÃO DE LIVRO")
    print("================================")

    titulo = input("Título do livro: ")

    biblioteca.devolver_livro(titulo)


def pesquisar_livro(biblioteca):
    print("\n================================")
    print(" PESQUISAR LIVRO")
    print("================================")

    titulo = input(
        "Digite parte ou o título do livro: "
    )

    resultados = biblioteca.pesquisar_livro(titulo)

    if len(resultados) == 0:
        print("\nNenhum livro encontrado.")
        return

    print(
        f"\nForam encontrados {len(resultados)} livro(s):"
    )

    for livro in resultados:
        livro.mostrar_informacoes()


def menu_principal(biblioteca):
    while True:
        print("\n")
        print("============================================")
        print(" SISTEMA DE BIBLIOTECA")
        print("============================================")

        print("Bem-vindo ao Sistema de Biblioteca!")

        print("\n----------- MENU PRINCIPAL -----------")

        print("1 - Consultar dados da biblioteca")
        print("2 - Consultar acervo")
        print("3 - Realizar cadastro")
        print("4 - Área do administrador")
        print("5 - Consultar dados do leitor")
        print("6 - Realizar empréstimo")
        print("7 - Realizar devolução")
        print("8 - Pesquisar livro")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            biblioteca.mostrar_dados()

        elif opcao == "2":
            biblioteca.consultar_acervo()

        elif opcao == "3":
            menu_cadastro(biblioteca)

        elif opcao == "4":
            menu_administrador(biblioteca)

        elif opcao == "5":
            consultar_leitor(biblioteca)

        elif opcao == "6":
            menu_emprestimo(biblioteca)

        elif opcao == "7":
            menu_devolucao(biblioteca)

        elif opcao == "8":
            pesquisar_livro(biblioteca)

        elif opcao == "0":
            print("\nObrigado por utilizar o sistema!")
            print("Programa encerrado.")
            break

        else:
            print("\nOpção inválida!")

        input("\nPressione ENTER para continuar...")


# ==========================================
# INÍCIO DO PROGRAMA
# ==========================================

biblioteca = Biblioteca()


# Cadastro dos leitores iniciais
leitor1 = Leitor(
    "Samuel",
    17,
    "(77) 99999-1111",
    "samuel@gmail.com"
)

leitor2 = Leitor(
    "Maria",
    18,
    "(77) 99999-2222",
    "maria@gmail.com"
)

biblioteca.cadastrar_leitor(leitor1)
biblioteca.cadastrar_leitor(leitor2)


# Cadastro dos livros iniciais
livro1 = Livro(
    "Orgulho e Preconceito",
    "Jane Austen",
    1813,
    432,
    "Penguin",
    "Romance"
)

livro2 = Livro(
    "Dom Casmurro",
    "Machado de Assis",
    1899,
    256,
    "Garnier",
    "Romance"
)

livro3 = Livro(
    "1984",
    "George Orwell",
    1949,
    328,
    "Companhia das Letras",
    "Ficção Distópica"
)

biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)
biblioteca.cadastrar_livro(livro3)


# Cadastro do administrador
administrador = Administrador(
    "Administrador",
    30,
    "(77) 99999-0000",
    "admin@biblioteca.com",
    "ADM123"
)


# Inicia o sistema
menu_principal(biblioteca)