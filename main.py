# bibliotecas
import re

# variáveis globais
lista_atendimentos = []
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
        print("d) Excluir um chamado em aberto")
        print("e) Encerrar atendimento")

        opcao = input("Digite a opção desejada (a, b, c ou d): \n")
        if opcao.lower() == "a":
            registro_usuario()
        elif opcao.lower() == "b":
            run_assistant()
        elif opcao.lower() == "c":
            if not lista_atendimentos:
                print("Não existem atendimentos registrados. \n")
            else:
                acompanhar_atendimento()
        elif opcao.lower() == "d":
            excluir_atendimento()
        elif opcao.lower() == "e":
            print("O App da Porto Seguro está sendo encerrado...")
            exit()
        else:
            print("Por favor, responda com uma das opções possíveis. \n")

# Registro de informações do usuário
# Dados do cliente que independem do seu pedido


def registro_usuario():
    global nome, cpf, email, fone_numero
    nome = input("Qual o seu nome? ")
    print("Nome informado! Próxima questão.\n")

    # vericicação cpf
    def validar_cpf(cpf):
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            return False

        if cpf == cpf[0] * 11:
            return False

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        digito1 = 11 - (soma % 11)
        if digito1 > 9:
            digito1 = 0

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        digito2 = 11 - (soma % 11)
        if digito2 > 9:
            digito2 = 0

        if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
            return False

        return True

    while True:
        cpf = input("Digite o CPF (somente números): ")

        if validar_cpf(cpf):
            print("CPF cadastrado! Vamos para a próxima pergunta.\n")
            break
        else:
            print("CPF inválido. Tente novamente.\n")

    # verificação email
    def verificar_email(email):
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # fornecido pela biblioteca re
        return re.match(padrao, email) is not None

    while True:
        email = input("Qual o seu e-mail? ")

        if verificar_email(email):
            print(
                "Agradecemos por informar seu e-mail. Vamos para a próxima pergunta.\n")
            break
        else:
            print("O e-mail não está no formato correto. Tente novamente.\n")

    # verificação telefone/whatsapp
    def verificar_telefone(telefone):
        # Removendo caracteres não numéricos
        telefone = ''.join(filter(str.isdigit, telefone))

        # Verificando se o telefone possui 11 dígitos (DDD + nono dígito + 8 números)
        if len(telefone) != 11:
            return False

        # Verificando se os três primeiros dígitos são um DDD válido (considerando DDDs brasileiros)
        ddd_validos = ['11', '12', '13', '14', '15', '16', '17', '18', '19',
                       '21', '22', '24', '27', '28',
                       '31', '32', '33', '34', '35', '37', '38',
                       '41', '42', '43', '44', '45', '46', '47', '48', '49',
                       '51', '53', '54', '55',
                       '61', '62', '63', '64', '65', '66', '67', '68', '69',
                       '71', '73', '74', '75', '77', '79',
                       '81', '82', '83', '84', '85', '86', '87', '88', '89',
                       '91', '92', '93', '94', '95', '96', '97', '98', '99']
        if telefone[:2] not in ddd_validos:
            return False

        return True

    while True:
        # Solicitar número de telefone ao usuário
        fone_numero = input(
            "Digite o número de telefone (com DDD e nono dígito): ")

        # Verificar telefone
        if verificar_telefone(fone_numero):
            print("Agradecemos por informar seu número de contato!\n")
            break
        else:
            print("Número de telefone inválido! Tente novamente.\n")

    print("Agradecemos por manter seus dados atualizados!")
    print("Isso agiliza um possível atendimento.\n")
    menu()

# Print informações do pedido do usuário


def acompanhar_atendimento():
    if len(lista_atendimentos) == 0:
        print("Nenhum atendimento registrado.\n")
    else:
        print("Atendimentos registrados:\n")
        for i, atendimento in enumerate(lista_atendimentos):
            print(f"Registro atendimento #{i+1}")
            exibir_informacoes_atendimento(atendimento)
            print()


def excluir_atendimento():
    if len(lista_atendimentos) == 0:
        print("Nenhum atendimento registrado.\n")
    else:
        while True:
            num_atendimento = input(
                "Digite o número do atendimento que deseja excluir (ou 'cancelar' para voltar ao menu): ")
            if num_atendimento.lower() == "cancelar":
                break

            try:
                num_atendimento = int(num_atendimento)
                if num_atendimento > 0 and num_atendimento <= len(lista_atendimentos):
                    atendimento_excluido = lista_atendimentos.pop(
                        num_atendimento - 1)
                    print("Atendimento excluído com sucesso!\n")
                    exibir_informacoes_atendimento(atendimento_excluido)
                    print()
                    break
                else:
                    print(
                        "Número de atendimento inválido. Por favor, digite um número válido.\n")
            except ValueError:
                print(
                    "Entrada inválida. Por favor, digite um número válido ou 'cancelar' para voltar ao menu.\n")


def exibir_informacoes_atendimento(atendimento):
    for chave, valor in atendimento.items():
        if chave == "Resposta 4":
            print("Resposta 4:")
            for sub_chave, sub_valor in valor.items():
                print(f"{sub_chave}: {sub_valor}")
        else:
            print(f"{chave}: {valor}")


def run_assistant():
    global nome, resposta1, resposta2, resposta3, resposta4_a, resposta4_b, resposta4_c, resposta4_d, resposta4_e, resposta5, resposta6

    print("Bem vindo ao nosso asistente virtual!")
    print("Por favor, preencha as perguntas conforme solicitado: \n")
    if nome == "":
        nome = input("Qual o seu nome? ")
    print(f"Olá, {nome}! Vamos começar o atendimento. \n")

    # Primeira Pergunta
    print("1: Escolha uma das opções que melhor atenda a sua necessidade. \n")
    print("a) Meu veículo está em um local de difícil acesso.")
    print("b) Me envolvi em uma situação de acidente.")
    print("c) Meu veículo apresenta defeito.")
    print("d) Preciso remover meu veículo de um local. \n")
    resposta1 = input("Escolha uma opção: ")

    if resposta1.lower() == "a" or resposta1.lower() == "dificil acesso":
        print("Sua escolha foi registrada. \n")
        if resposta1.lower() == "a":
            resposta1 = "Local dificil"

    elif resposta1.lower() == "b" or resposta1.lower() == "acidente":
        print("Sua escolha foi registrada. \n")
        if resposta1.lower() == "b":
            resposta1 = "Acidente"

    elif resposta1.lower() == "c" or resposta1.lower() == "veiculo com defeito":
        print("Sua escolha foi registrada. \n")
        if resposta1.lower() == "c":
            resposta1 = "Veículo com defeito"

    elif resposta1.lower() == "d" or resposta1.lower() == "remoção":
        print("Sua escolha foi registrada. \n")
        if resposta1.lower() == "d":
            resposta1 = "Remoção veículo do local"

    else:
        print("Por favor, responda com uma das opções possíveis. \n")

    # Segunda Pergunta

    resposta2 = input("2: Faça um breve descrição do ocorrido: ")
    print()

    # Terceira Pergunta
    resposta3 = input(
        "3: Envie uma imagem da situação (com o veículo): ")
    print()

    # Quarta pergunta
    print("4: Precisamos de algumas informações sobre o veículo. \n")
    resposta4_a = input("a) Quantidade de eixos. ")
    resposta4_b = input("b) Altura do veículo (metros). ")
    resposta4_c = input("c) Modelo do veículo. ")
    resposta4_d = input("d) Peso do veículo (em tons, sem carga). ")
    resposta4_e = input("e) Placa do veículo. ")
    print()

    # Quinta Pergunta
    print("5: Escolha a opção que identifique o peso da carga. \n")
    print("a) Carga leve. ")
    print("b) Carga pesada. ")
    print("c) Sem carga. ")
    resposta5 = input("Escolha uma opção: ")

    if resposta5.lower() == "a" or resposta5.lower() == "carga leve":
        print("Sua escolha foi registrada. \n")
        if resposta5.lower() == "a":
            resposta5 = "Carga leve"

    elif resposta5.lower() == "b" or resposta5.lower() == "carga pesada":
        print("Sua escolha foi registrada. \n")
        if resposta5.lower() == "b":
            resposta5 = "Carga pesada"

    elif resposta5.lower() == "c" or resposta5.lower() == "sem carga":
        print("Sua escolha foi registrada. \n")
        if resposta5.lower() == "c":
            resposta5 = "Sem carga"

    else:
        print("Por favor, responda com uma das opções possíveis. \n")

    # Sexta Pergunta
    resposta6 = input("6: Insira o local do atendimento: ")
    print()

    # Registro do atendimento
    registro_atendimento = {
        "Nome": nome,
        "CPF": cpf,
        "Email": email,
        "Telefone": fone_numero,
        "Resposta 1": resposta1,
        "Resposta 2": resposta2,
        "Resposta 3": resposta3,
        "Resposta 4": {
            "a": resposta4_a,
            "b": resposta4_b,
            "c": resposta4_c,
            "d": resposta4_d,
            "e": resposta4_e
        },
        "Resposta 5": resposta5,
        "Resposta 6": resposta6
    }

    lista_atendimentos.append(registro_atendimento)
    print("Atendimento registrado com sucesso!\n")


    menu()


# Iniciar o programa
menu()
