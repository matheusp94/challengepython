# Menu principal de navegação. Contem:
#1- preechimento dos dados do cliente 
#2- Novo atendimento 
#3- acompanhar atendimento 
#4- cancelamento de um atendimento

def menu_navegacao():





    # Assistente virtual


    def executar_assistente():

        print("Bem vindo ao assistente da Porto Seguro! Por favor, responda as seguintes perguntas: ")

        nome = input("Qual o seu nome? ")
        print(f"Olá, {nome}! Meu nome é Cirilo, sou o assistente da Porto Seguro. Para o seu atendimento, preciso que me informe o seu cpf: ")

        cpf = input("Digite o seu cpf: ")
        print(f"Muito obrigado, {nome}, registramos o seu cpf {cpf}! Agora, preciso que preencha o campo com uma das opções que melhor descreve sua resposta para cada pergunta que virá a seguir. \n")

        # talvez por um timesleep aqui

        # First question
        while True:
            print("Pergunta 1) De que atendimento você precisa?")
            print("a) Novo atendimento")
            print("b) Acompanhar atendimento")
            print("c) Cancelar serviço agendado")
            # print("d) Outro")

            answer1 = input("Digite sua resposta: ")
            if answer1.lower() == "a" or answer1.lower() == "novo atendimento":
                print(
                    "Ok, vamos fazer algumas perguntas para dar sequencia ao seu novo atendimento.")

            elif answer1.lower() == "b" or answer1.lower() == "acompanhar atendimento":
                input("Digite o ocorrido: \n")

                break

            else:
                print("Incorrect. Please try again.")

        # Second question
        while True:
            print("Question 2: Which is the largest desert in the world?")
            print("a) Sahara")
            print("b) Gobi")
            print("c) Antarctica")
            answer2 = input("Your answer: ")
            if answer2.lower() == "a" or answer2.lower() == "sahara":
                print("Correct!")
                break
            else:
                print("Incorrect. Please try again.")

        # Third question
        while True:
            print("Question 3: What is the tallest mountain in the world?")
            print("a) K2")
            print("b) Mount Everest")
            print("c) Kilimanjaro")
            answer3 = input("Your answer: ")
            if answer3.lower() == "b" or answer3.lower() == "mount everest":
                print("Correct!")
                break
            else:
                print("Incorrect. Please try again.")

        # Ask if user wants to play again
        play_again = input("Deseja realizar um novo atendimento? (sim/não) ")
        if play_again.lower() == "sim" or "s":
            executar_assistente()
        else:
            print("Agradecemos o seu contato. Tenha um ótimo restante de dia!")


# Call the function to start the quiz game
    executar_assistente()

menu_navegacao()

# End of program
