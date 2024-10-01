nome = input("Digite o seu nome:")
escola = "José Bonifácio"
print(f"Seja bem vindo ao colégio {escola}{nome}")


def menu():
    print("Em que posso ser útil hoje?")
    print("Digite uma das opções abaixo:")
    print("1 - Cursos")
    print("2 - Matricula")
    print("3 - Vagas")

    resp_aluno = int(input("Você: "))

    if resp_aluno == 1:
        print("Aqui vai ser o retorno quando a opção digitar 1")

    elif resp_aluno == 2:
        print("Aqui vai ser o retorno quando a opção digitar 2")

    elif resp_aluno == 3:
        print("Aqui vai ser o retorno quando a opção digitar 3")

    else:
        print("Essa mensagem vai aparecer quando a pessoa digitar uma opção que não está disponível")