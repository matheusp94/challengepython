# Equipe: Matheus, Caio, Julianny, Karen

# variáveis globais
global lista_atendimentos, lista_final, nome

# Lista com as escolhas
lista_atendimentos = []

# Variáveis Globais
nome = ""
cpf = ""
email = ""
fone_numero = ""
placa_veiculo = ""
alteracao_veiculo = ""
imagem_veiculo = ""

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
            run_open_service()
        elif opcao.lower() == "d":
            print("O App da Porto Seguro está sendo encerrado...")
            exit()
        else:
            print("Por favor, responda com uma das opções possíveis. \n")

#### Registro de informações. O usuário tem a possibilidade de##
# fazer um registro prévio de algumas informações para agilizar#
# futuros atendimentos #########################################

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
                   resposta2, resposta3, resposta4, resposta5,
                   resposta6]
    lista_atendimentos.append(lista_final)
    for i, lst in enumerate(lista_atendimentos):
        print("Registro atendimento #{}: {}".format(i+1, lst))


def run_assistant():
    global nome, resposta1, resposta2, resposta3, resposta4, resposta5, resposta6

    print("Bem vindo ao nosso asistente virtual!")
    print("Por favor, preencha as perguntas conforme solicitado: \n")
    if nome == "":
        nome = input("Qual o seu nome? ")
    print(f"Olá, {nome}! Vamos começar o atendimento. \n")

    # Primeira Pergunta
    while True:
        print("1: Qual tipo de atendimento você precisa? \n")
        print("a) Troca de pneu")
        print("b) Manutenção")
        print("c) Chaveiro para veículo")
        print("d) Relatar furto ou roubo")
        print("e) Guincho \n")
        resposta1 = input("Escolha uma opção: ")

        if resposta1.lower() == "a" or resposta1.lower() == "troca de pneu":
            print("Sua escolha foi registrada. \n")
            if resposta1.lower() == "a":
                resposta1 = "Troca pneu"
            break

        elif resposta1.lower() == "b" or resposta1.lower() == "manutenção":
            print("Sua escolha foi registrada. \n")
            if resposta1.lower() == "b":
                resposta1 = "Manutenção"
            break

        elif resposta1.lower() == "c" or resposta1.lower() == "chaveiro para veículo":
            print("Sua escolha foi registrada. \n")
            if resposta1.lower() == "c":
                resposta1 = "Chaveiro para veículo"
            break

        elif resposta1.lower() == "d" or resposta1.lower() == "relatar furto ou roubo":
            print("Sua escolha foi registrada. \n")
            if resposta1.lower() == "d":
                resposta1 = "Furto ou roubo"
            break

        elif resposta1.lower() == "e" or resposta1.lower() == "guincho":
            print("Sua escolha foi registrada. \n")
            if resposta1.lower() == "e":
                resposta1 = "Guincho"
            break

        else:
            print("Por favor, responda com uma das opções possíveis. \n")

    # Segunda Pergunta
    while True:
        print("2: Escolha uma das opções que melhor atenda a sua necessidade. \n")
        print("a) Preciso remover meu veículo de um local")
        print("b) Preciso de um técnico para meu veículo")
        print("c) Me envolvi em uma situação de acidente")
        resposta2 = input("Escolha uma opção: ")

        if resposta2.lower() == "a" or resposta2.lower() == "remover meu veículo de um local":
            print("Sua escolha foi registrada. \n")
            if resposta2.lower() == "a":
                resposta2 = "Remoção veículo"
            break

        elif resposta2.lower() == "b" or resposta2.lower() == "tecnico para meu veículo":
            print("Sua escolha foi registrada. \n")
            if resposta2.lower() == "b":
                resposta2 = "Envio de técnico"
            break

        elif resposta2.lower() == "c" or resposta2.lower() == "situação de acidente":
            print("Sua escolha foi registrada. \n")
            if resposta2.lower() == "c":
                resposta2 = "Acidente"
            break

        else:
            print("Por favor, responda com uma das opções possíveis. \n")

    # Terceira Pergunta
    while True:
        print("3: Descrição simples do ocorrido e envio de imagem (opcional). \n")
        print("a) Faça uma breve descrição da situação. ")
        print("b) Envie uma imagem da situação atual do veículo (se possível). ")
        print("c) Pular essa opção/seguir com o atendimento. ")
        resposta3 = input("Escolha uma opção: ")

        if resposta3.lower() == "a" or resposta3.lower() == "descrição da situação":
            input("Sua resposta: ")
            print(
                "Recebemos a descrição. Você pode também enviar/alterar a imagem da situação.")
            print(
                "Caso não queira, você pode selecionar a opção C e pular para a próxima etapa. \n")
            if resposta3.lower() == "a":
                resposta3 = "Situação descrita"

        elif resposta3.lower() == "b" or resposta3.lower() == "imagem":
            # ainda não conseguimos dar a opção de upar um arquivo
            input("link da imagem: ")
            print(
                "Recebemos sua imagem. Você pode também enviar/alterar a descrição da situação. \n")
            print(
                "Caso não queira, você pode selecionar a opção C e pular para a próxima etapa. \n")
            if resposta3.lower() == "b":
                resposta3 = "Imagem registrada"

        elif resposta3.lower() == "c" or resposta3.lower() == "pular":
            # ainda não conseguimos dar a opção de upar um arquivo
            print("Você escolheu não preencher ou pular esta etapa. \n")
            if resposta3.lower() == "c":
                resposta3 = "Pulou pergunta"
            break

        else:
            print("Por favor, responda com uma das opções possíveis. \n")

    # Quarta Pergunta
    while True:
        print("4: Qual tipo de atendimento você deseja? \n")
        print("a) Atendimento imediato. ")
        print("b) Atendimento agendado. ")
        resposta4 = input("Sua resposta: ")
        if resposta4.lower() == "a" or resposta4.lower() == "imediato":
            endereco = input(
                "Entre com o endereço em que o veículo se encontra no momento: ")
            print("Enviaremos nosso modal imediatamente! \n")
            if resposta4.lower() == "a":
                resposta4 = f"Endereço: {endereco}"
            break

        elif resposta4.lower() == "b" or resposta4.lower() == "agendado":
            endereco_agendado = input(
                "Digite o endereço em que o veículo se encontra: ")
            horario_agendado = input(
                "Digite uma data e horario que melhor atenda a sua necessidade: ")
            if resposta4.lower() == "b":
                resposta4 = f"Endereço: {endereco_agendado} as {horario_agendado}"
            break

        else:
            print("Por favor, responda com uma das opções possíveis. \n")

    # Quinta Pergunta REFAZER OU REMOVER
    while True:
        resposta5 = input("5: Por favor, nos informe a placa do seu veículo: ")
        print()
        break

    # Quinta Pergunta REFAZER OU REMOVER
    while True:
        resposta6 = input("6: Envie uma imagem do seu veículo: ")
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
                       resposta2, resposta3, resposta4, resposta5, resposta6]
        print("Segue o resumo do seu atendimento: \n")
        print(lista_final)
        print()
        print("Caso deseje, poderá realizar outro atendimento. \n")


# Chama a fução menu para iniciar o programa
menu()

# fim do programa
