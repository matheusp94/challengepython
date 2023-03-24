# Menu principal de navegação. Contem:
# 1- preechimento dos dados do cliente
# 2- Novo atendimento
# 3- acompanhar atendimento
# 4- cancelamento de um atendimento

# A quiz game with a menu to register name, play the game, or end the program

def menu():
    while True:
        print("Please select an option:")
        print("a) Register your name")
        print("b) Play the game")
        print("c) End the program")
        choice = input("Your choice: ")
        if choice.lower() == "a":
            register_data()
        elif choice.lower() == "b":
            run_assistant()
        elif choice.lower() == "c":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def register_data():
    global name
    name = input("Qual o seu nome? ")
    cpf = input("Qual o seu cpf? ")
    placa_veiculo = input("Insira a placa do seu veículo: ")
    # Talvez dar opções nessa opção em versões futuras
    alteracao_veiculo = input(
        "Foram feitas alterações recentes no veículo? Descreva-as: ")
    numero_contato_wpp = input("Insira seu numero de contato/whatsapp: ")
    email = ("Insira seu email: ")
    imagem_veiculo = (
        "Insira uma ou mais imagens do seu veículo, com possíveis alterações feitas: ")


# A quiz game with repeated questions and the option to play again
def run_assistant():
    print("Bem vindo! Sou o Cirilo, seu assitente virtual! Escolha a seguir as opções que melhor responda a cada pergunta: ")

    global name  # importante para usar a variável dentro de def
    if not name:
        name = input("Qual o seu nome? ")
    print(f"Olá, {name}! vamos começar.")

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
        print("a) K2")
        print("b) Mount Everest")
        print("c) Kilimanjaro")
        answer5 = input("Your answer: ")
        if answer5.lower() == "b" or answer5.lower() == "mount everest":
            print("Correct!")
            break
        else:
            print("Incorrect. Please try again.")

    # Ask if user wants to play again
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() == "yes":
        run_assistant()
    else:
        print("Thank you for playing! Goodbye!")


# Initialize the name variable
name = None

# Call the menu function to start the program
menu()

# End of program
