# Global variables
name = ""
cpf = ""
email = ""
phone_number = ""
placa_veiculo = ""
alteracao_veiculo = ""
imagem_veiculo = ""

# Menu function


def menu():
    print("Bem vindo ao app Porto Seguro! \n")
    print("a) Registre seus dados")
    print("b) Novo atendimento")
    print("c) Acompanhar atendimento")
    print("d) Cancelar atendimento")

    option = input("Digite a opção desejada (a, b, or c): ")
    if option.lower() == "a":
        register_information()
    elif option.lower() == "b":
        run_assistant()
    elif option.lower() == "c":
        run_open_service()
    elif option.lower() == "d":
        print("Cancelando atendimento em aberto...")

    else:
        print("Por favor, responda com uma das opções possíveis. ")

# Function to register information


def register_information():
    global name, cpf, email, phone_number, placa_veiculo, alteracao_veiculo, imagem_veiculo

    name = input("Qual o seu nome? ")
    cpf = input("Qual o seu cpf? ")
    email = input("Qual o seu email? ")
    phone_number = input("Qual o seu número de contato/whatsapp? ")
    placa_veiculo = input("Qual o número da sua placa? ")
    alteracao_veiculo = input("Descreva alterações recentes no veículo: ")
    imagem_veiculo = input("Envie uma imagem recente do veículo (url): ")

    print("Thank you for registering your information!")
    menu()

# Quiz game function


def run_open_service():
    print("\n Segue os dados do seu pedido em aberto:")
    print(f"Name: {name}")
    print(f"cpf: {cpf}")
    print(f"Email: {email}")
    print(f"Phone number: {phone_number}")
    print(f"Placa do veículo: {placa_veiculo}")
    print(f"Alterações no veículo: {alteracao_veiculo}")
    print(f"Imagem do veículo: {imagem_veiculo}")


def run_assistant():
    global name

    print("Welcome to our quiz game! Please answer the following questions:")

    if name == "":
        name = input("What's your name? ")
    print(f"Hello, {name}! Let's get started.")

    # First question
    while True:
        print("1: Qual tipo de atendimento você precisa? ")
        print("a) Troca de pneu")
        print("b) Manutenção")
        print("c) Chaveiro para veículo")
        print("d) Relatar furto ou roubo")
        print("e) Guincho")
        answer1 = input("Escolha uma opção: ")

        if answer1.lower() == "a" or answer1.lower() == "troca de pneu":
            print("Sua escolha foi registrada. \n")
            break

        elif answer1.lower() == "b" or answer1.lower() == "manutenção":
            print("Sua escolha foi registrada. \n")
            break

        elif answer1.lower() == "c" or answer1.lower() == "chaveiro para veículo":
            print("Sua escolha foi registrada. \n")
            break

        elif answer1.lower() == "d" or answer1.lower() == "relatar furto ou roubo":
            print("Sua escolha foi registrada. \n")
            break

        elif answer1.lower() == "e" or answer1.lower() == "guincho":
            print("Sua escolha foi registrada. \n")
            break

        else:
            print("Por favor, responda com uma das opções possíveis.")

    # Second question
    while True:
        print("2: Escolha uma das opções que melhor atenda a sua necessidade. ")
        print("a) Preciso remover meu veículo de um local")
        print("b) Preciso de um técnico par meu veículo")
        print("c) Me envolvi em uma situação de acidente")
        answer2 = input("Escolha uma opção: ")

        if answer2.lower() == "a" or answer2.lower() == "remover meu veículo de um local":
            print("Sua escolha foi registrada. \n")
            break

        elif answer2.lower() == "b" or answer2.lower() == "tecnico par meu veículo":
            print("Sua escolha foi registrada. \n")
            break

        elif answer2.lower() == "c" or answer2.lower() == "situação de acidente":
            print("Sua escolha foi registrada. \n")
            break

        else:
            print("Por favor, responda com uma das opções possíveis.")

    # Third question
    while True:
        print("3: Descrição simples do ocorrido e envio de imagem (opcional). ")
        print("a) Faça uma breve descrição da situação. ")
        print("b) Envie uma imagem da situação atual do veículo (se possível).")
        print("c) Pular essa opção/seguir com o atendimento. ")
        answer3 = input("Escolha uma opção: ")

        if answer3.lower() == "a" or answer3.lower() == "descrição da situação":
            input("Sua resposta: ")
            print(
                "Recebemos sua descrição. Você pode também enviar/alterar a imagem da situação. \n")

        elif answer3.lower() == "b" or answer3.lower() == "imagem":
            # ainda não conseguimos dar a opção de upar um arquivo
            input("link da imagem: ")
            print(
                "Recebemos sua imagem. Você pode também enviar/alterar a descrição da situação. \n")

        elif answer3.lower() == "c" or answer3.lower() == "pular":
            # ainda não conseguimos dar a opção de upar um arquivo
            print("Você escolheu não preencher ou pular esta etapa. \n")
            break

        else:
            print("Por favor, responda com uma das opções possíveis.")

    # Fourth question
    while True:
        print("4: Qual tipo de atendimento você deseja? ")
        print("a) Atendimento imediato. ")
        print("b) Atendimento agendado. ")
        answer4 = input("Your answer: ")
        if answer4.lower() == "a" or answer4.lower() == "imediato":
            print("Enviaremos nosso modal imediatamente!")
            break

        elif answer4.lower() == "b" or answer4.lower() == "agendado":
            input("Digite uma data e horario que melhor atenda a sua necessidade: ")
            break

        else:
            print("Por favor, responda com uma das opções possíveis.")

    # Fifth question
    while True:
        print("5: Informe o endereço de atendimento. ")
        print("a) Selecione a para entrar com o endereço: ")
        answer5 = input("Endereço: ")
        if answer5.lower() == "a":
            print("O local do ocorrido foi registrado! \n")
            break
        else:
            print("Por favor, digite corretamente. ")

    # Ask if user wants to play again
    play_again = input("Deseja refazer o atendimento? (sim/não) ")
    if play_again.lower() == "sim" or play_again.lower() == "s":
        run_assistant()
    else:
        print("Agradecemos o contato. Tenha um ótimo dia!")

    # Print user information
    print("\n Segue suas informações:")
    print(f"Name: {name}")
    print(f"cpf: {cpf}")
    print(f"Email: {email}")
    print(f"Phone number: {phone_number}")
    print(f"Placa do veículo: {placa_veiculo}")
    print(f"Alterações no veículo: {alteracao_veiculo}")
    print(f"Imagem do veículo: {imagem_veiculo}")


# Call the menu function to start the program
menu()

# End of program
