# Equipe:
# Caio César Arruda = RM 99456
# Julianny Araújo Pereira = RM 99554
# Karen Vitória Jesus da Silva = RM 99468
# Matheus Matos Pereira = RM 99792
# Rodrigo Machado Cardoso = RM 94301


# variáveis globais
global lista_atendimentos, lista_final, nome

# Lista com as escolhas
lista_atendimentos = []

# Variáveis Globais
nome = ''
cpf = ''
email = ''
fone_numero = ''
placa_veiculo = ''
alteracao_veiculo = ''
imagem_veiculo = ''
resposta1 = ''
resposta2 = ''
resposta3 = ''
resposta4_a = ''
resposta4_b = ''
resposta4_c = ''
resposta4_d = ''
resposta4_e = ''
resposta5 = ''
resposta6 = ''


# Menu Principal


def menu():

    print("Bem vindo ao app Porto Seguro! \n")
    while True:
        print("a) Registre seus dados")
        print("b) Novo atendimento")
        print("c) Acompanhar atendimento")
        print("d) Encerrar atendimento")

        opcao = input("Digite a opção desejada (a, b, c ou d): \n")
        if opcao.lower() == "a":
            registro_usuario()
        elif opcao.lower() == "b":
            run_assistant()
        elif opcao.lower() == "c":
            if resposta1 == '' and resposta2 == '' and resposta3 == '' and resposta4_a == '' and resposta4_b == '' and resposta4_c == '' and resposta4_d == '' and resposta4_e == '' and resposta5 == '' and resposta6 == '':
                print("Não existem atendimentos registrados. \n")
            else:
                run_open_service()
        elif opcao.lower() == "d":
            print("O App da Porto Seguro está sendo encerrado...")
            exit()
        else:
            print("Por favor, responda com uma das opções possíveis. \n")

# Registro de informações do usuário
# Dados do cliente que independem do seu pedido


def registro_usuario():
    global nome, cpf, email, fone_numero
    nome = input("Qual o seu nome? ")
    cpf = input("Qual o seu cpf? ")
    email = input("Qual o seu email? ")
    fone_numero = input("Qual o seu número de contato/whatsapp? ")
    print("Agradecemos por manter seus dados atualizados!")
    print("Isso agiliza um possível atendimento.\n")
    menu()

# Print informações do pedido do usuário


def run_open_service():
    print("Segue os dados dos atendimentos em aberto: \n")
    lista_final = [nome, cpf, email, fone_numero, resposta1,
                   resposta2, resposta3, resposta4_a, resposta4_b, resposta4_c, resposta4_d, resposta4_e, resposta5,
                   resposta6]
    lista_atendimentos.append(lista_final)
    for i, lst in enumerate(lista_atendimentos):
        print("Registro atendimento #{}: {}".format(i+1, lst))


def run_assistant():
    global nome, resposta1, resposta2, resposta3, resposta4_a, resposta4_b, resposta4_c, resposta4_d, resposta4_e, resposta5, resposta6

    print("Bem vindo ao nosso asistente virtual!")
    print("Por favor, preencha as perguntas conforme solicitado: \n")
    if nome == "":
        nome = input("Qual o seu nome? ")
    print(f"Olá, {nome}! Vamos começar o atendimento. \n")

    # Primeira Pergunta
    while True:
        print("1: Escolha uma das opções que melhor atenda a sua necessidade. \n")
        print("a) Meu veículo está em um local de dificil acesso.")
        print("b) Me envolvi em uma situação de acidente.")
        print("c) Meu veículo apresenta defeito.")
        print("d) Preciso remover meu veículo de um local. \n")
        resposta1 = input("Escolha uma opção: ")

        if resposta1.lower() == "a" or resposta1.lower() == "dificil acesso":
            print("Sua escolha foi registrada. \n")
            if resposta1.lower() == "a":
                resposta1 = "Local dificil"
            break

        elif resposta1.lower() == "b" or resposta1.lower() == "acidente":
            print("Sua escolha foi registrada. \n")
            if resposta1.lower() == "b":
                resposta1 = "Acidente"
            break

        elif resposta1.lower() == "c" or resposta1.lower() == "veiculo com defeito":
            print("Sua escolha foi registrada. \n")
            if resposta1.lower() == "c":
                resposta1 = "Veículo com defeito"
            break

        elif resposta1.lower() == "d" or resposta1.lower() == "remoção":
            print("Sua escolha foi registrada. \n")
            if resposta1.lower() == "d":
                resposta1 = "Remoção veículo do local"
            break

        else:
            print("Por favor, responda com uma das opções possíveis. \n")

    # Segunda Pergunta
    while True:
        resposta2 = input("2: Faça um breve descrição do ocorrido: ")
        print()
        break

    # Terceira Pergunta
    while True:
        resposta3 = input(
            "3: Envie uma imagem da situação (com o veículo): ")
        print()
        break

    # Quarta pergunta
    while True:
        print("4: Precisamos de algumas informações sobre o veículo. \n")
        resposta4_a = input("a) Quantidade de eixos. ")
        resposta4_b = input("b) Altura do veículo (metros). ")
        resposta4_c = input("c) Modelo do veículo. ")
        resposta4_d = input("d) Peso do veículo (em tons, sem carga). ")
        resposta4_e = input("e) Placa do veículo. ")
        print()
        break

    # Quinta Pergunta
    while True:
        print("5: Escolha a opção que identifique o peso da carga. \n")
        print("a) Carga leve. ")
        print("b) Carga pesada. ")
        print("c) Sem carga. ")
        resposta5 = input("Escolha uma opção: ")

        if resposta5.lower() == "a" or resposta5.lower() == "carga leve":
            print("Sua escolha foi registrada. \n")
            if resposta5.lower() == "a":
                resposta5 = "Carga leve"
            break

        elif resposta5.lower() == "b" or resposta2.lower() == "carga pesada":
            print("Sua escolha foi registrada. \n")
            if resposta5.lower() == "b":
                resposta5 = "Carga pesada"
            break

        elif resposta5.lower() == "c" or resposta5.lower() == "sem carga":
            print("Sua escolha foi registrada. \n")
            if resposta5.lower() == "c":
                resposta5 = "Sem carga. "
            break

        else:
            print("Por favor, responda com uma das opções possíveis. \n")

    # Sexta Pergunta
    while True:
        resposta6 = input("6: Insira o local do atendimento: ")
        print()
        break

    # Perguntar se deseja refazer o atendimento atual (substitui as respostas)
    # Selecionar "não" retorna ao menu principal, assim é possível fazer outro atendimento(que não substitui respostas)
    refazer_atendimento = input("Deseja refazer esse atendimento? (sim/não) ")
    if refazer_atendimento.lower() == "sim" or refazer_atendimento.lower() == "s":
        run_assistant()
    else:
        print("Agradecemos o contato. Tenha um ótimo dia! \n")

    # Resumo atendimento
        lista_final = [nome, cpf, email, fone_numero, resposta1,
                       resposta2, resposta3, resposta4_a, resposta4_b, resposta4_c, resposta4_d, resposta4_e, resposta5, resposta6]
        print("Segue o resumo do seu atendimento: \n")
        print(lista_final)
        print()
        print("Caso deseje, poderá realizar outro atendimento. \n")


# Chama a fução menu para iniciar o programa
menu()

# fim do programa
