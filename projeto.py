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
    name = input("What's your name? ")
    cpf = input("What's your cpf? ")
    placa_veiculo = input("What's your vehicle number? ")
    alteracao_veiculo = input("What's your vehicle alterations? ")
    numero_contato_wpp = input("Insira seu numero de contato: ")
    email = ("Insira seu email: ")
    imagem_veiculo = ("Insira uma imagem do seu veículo, com possíveis alterações feitas: ")
    
    


# A quiz game with repeated questions and the option to play again
def run_assistant():
    print("Welcome to our quiz game! Please answer the following questions:")

    global name
    if not name:
        name = input("What's your name? ")
    print(f"Hello, {name}! Let's get started.")

    # First question
    while True:
        print("Question 1: What is the capital of Canada?")
        print("a) Toronto")
        print("b) Ottawa")
        print("c) Vancouver")
        answer1 = input("Your answer: ")
        if answer1.lower() == "b" or answer1.lower() == "ottawa":
            print("Correct!")
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
