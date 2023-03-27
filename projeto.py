# Equipe: Matheus, Caio, Julianny, Karen

# Variáveis Globais
nome = ""
cpf = ""
email = ""
fone_numero = ""
placa_veiculo = ""
alteracao_veiculo = ""
imagem_veiculo = ""

# Menu


def menu():
    print("Bem vindo ao app Porto Seguro! \n")
    while True:
        print("a) Registre seus dados")
        print("b) Novo atendimento")
        print("c) Acompanhar atendimento")
        print("d) Cancelar atendimento")

        opcao = input("Digite a opção desejada (a, b, or c): \n")
        if opcao.lower() == "a":
            register_information()
        elif opcao.lower() == "b":
            run_assistant()
        elif opcao.lower() == "c":
            run_open_service()
        elif opcao.lower() == "d":
            print("Cancelando atendimento em aberto...")

        else:
            print("Por favor, responda com uma das opções possíveis. \n")

# Registro de informações


def register_information():
    global nome, cpf, email, fone_numero, placa_veiculo, alteracao_veiculo, imagem_veiculo

    nome = input("Qual o seu nome? ")
    cpf = input("Qual o seu cpf? ")
    email = input("Qual o seu email? ")
    fone_numero = input("Qual o seu número de contato/whatsapp? ")
    placa_veiculo = input("Qual o número da sua placa? ")
    alteracao_veiculo = input("Descreva alterações recentes no veículo: ")
    imagem_veiculo = input("Envie uma imagem recente do veículo (url): \n")

    print("Agradecemos por manter seus dados atualizados!")
    print("Isso agiliza um possível atendimento.\n")
    menu()

# Quiz game function


def run_open_service():
    print("Segue os dados do seu pedido em aberto:")
    print(f"Nome: {nome}")
    print(f"cpf: {cpf}")
    print(f"Email: {email}")
    print(f"Número de contato/whatsapp: {fone_numero}")
    print(f"Placa do veículo: {placa_veiculo}")
    print(f"Alterações no veículo: {alteracao_veiculo}")
    print(f"Imagem do veículo: {imagem_veiculo} \n")


def run_assistant():
    global nome

    print("Bem vindo ao nosso asistente virtual!")
    print("Por favor, preencha as perguntas conforme solicitado: \n")

    if nome == "":
        nome = input("Qual o seu nome? ")
    print(f"Olá, {nome}! Vamos começar o atendimento. \n")

    # Primeira Pergunta
    while True:
        print("1: Qual tipo de atendimento você precisa? ")
        print("a) Troca de pneu")
        print("b) Manutenção")
        print("c) Chaveiro para veículo")
        print("d) Relatar furto ou roubo")
        print("e) Guincho \n")
        resposta1 = input("Escolha uma opção: ")

        if resposta1.lower() == "a" or resposta1.lower() == "troca de pneu":
            print("Sua escolha foi registrada. \n")
            break

        elif resposta1.lower() == "b" or resposta1.lower() == "manutenção":
            print("Sua escolha foi registrada. \n")
            break

        elif resposta1.lower() == "c" or resposta1.lower() == "chaveiro para veículo":
            print("Sua escolha foi registrada. \n")
            break

        elif resposta1.lower() == "d" or resposta1.lower() == "relatar furto ou roubo":
            print("Sua escolha foi registrada. \n")
            break

        elif resposta1.lower() == "e" or resposta1.lower() == "guincho":
            print("Sua escolha foi registrada. \n")
            break

        else:
            print("Por favor, responda com uma das opções possíveis. \n")

    # Segunda Pergunta
    while True:
        print("2: Escolha uma das opções que melhor atenda a sua necessidade. ")
        print("a) Preciso remover meu veículo de um local")
        print("b) Preciso de um técnico par meu veículo")
        print("c) Me envolvi em uma situação de acidente")
        resposta2 = input("Escolha uma opção: ")

        if resposta2.lower() == "a" or resposta2.lower() == "remover meu veículo de um local":
            print("Sua escolha foi registrada. \n")
            break

        elif resposta2.lower() == "b" or resposta2.lower() == "tecnico par meu veículo":
            print("Sua escolha foi registrada. \n")
            break

        elif resposta2.lower() == "c" or resposta2.lower() == "situação de acidente":
            print("Sua escolha foi registrada. \n")
            break

        else:
            print("Por favor, responda com uma das opções possíveis.")

    # Terceira Pergunta
    while True:
        print("3: Descrição simples do ocorrido e envio de imagem (opcional). ")
        print("a) Faça uma breve descrição da situação. ")
        print("b) Envie uma imagem da situação atual do veículo (se possível).")
        print("c) Pular essa opção/seguir com o atendimento. ")
        resposta3 = input("Escolha uma opção: ")

        if resposta3.lower() == "a" or resposta3.lower() == "descrição da situação":
            input("Sua resposta: ")
            print(
                "Recebemos sua descrição. Você pode também enviar/alterar a imagem da situação. \n")

        elif resposta3.lower() == "b" or resposta3.lower() == "imagem":
            # ainda não conseguimos dar a opção de upar um arquivo
            input("link da imagem: ")
            print(
                "Recebemos sua imagem. Você pode também enviar/alterar a descrição da situação. \n")

        elif resposta3.lower() == "c" or resposta3.lower() == "pular":
            # ainda não conseguimos dar a opção de upar um arquivo
            print("Você escolheu não preencher ou pular esta etapa. \n")
            break

        else:
            print("Por favor, responda com uma das opções possíveis.")

    # Quarta Pergunta
    while True:
        print("4: Qual tipo de atendimento você deseja? ")
        print("a) Atendimento imediato. ")
        print("b) Atendimento agendado. ")
        resposta4 = input("Your resposta: ")
        if resposta4.lower() == "a" or resposta4.lower() == "imediato":
            input("Entre com o endereço em que o veículo se encontra no momento: ")
            print("Enviaremos nosso modal imediatamente!")
            break

        elif resposta4.lower() == "b" or resposta4.lower() == "agendado":
            input("Digite o endereço em que o veículo se encontra: ")
            input("Digite uma data e horario que melhor atenda a sua necessidade: ")
            break

        else:
            print("Por favor, responda com uma das opções possíveis.")

    # Quinta Pergunta
    while True:
        print("5: Informe o endereço de atendimento. ")
        print("a) Selecione a para entrar com o endereço: ")
        resposta5 = input("Endereço: ")
        if resposta5.lower() == "a":
            print("O local do ocorrido foi registrado! \n")
            break
        else:
            print("Por favor, digite corretamente. ")

    # Perguntar se deseja refazer o atendimento
    refazer_atendimento = input("Deseja refazer o atendimento? (sim/não) ")
    if refazer_atendimento.lower() == "sim" or refazer_atendimento.lower() == "s":
        run_assistant()
    else:
        print("Agradecemos o contato. Tenha um ótimo dia!")

    # Print informações do usuário
    print("\n Segue suas informações:")
    print(f"Nome: {nome}")
    print(f"cpf: {cpf}")
    print(f"Email: {email}")
    print(f"Número de telefone/whatsapp: {fone_numero}")
    print(f"Placa do veículo: {placa_veiculo}")
    print(f"Alterações no veículo: {alteracao_veiculo}")
    print(f"Imagem do veículo: {imagem_veiculo}")


# Chama a fução menu para iniciar o programa
menu()

# fim do programa
