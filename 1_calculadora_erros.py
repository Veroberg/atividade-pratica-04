# Atividade Prática 04 - Questão 1
#
# Desenvolva uma calculadora em Python que realize as quatro operações básicas.
# Ela deve lidar com erros de entrada, divisão por zero e operações inválidas.
#
# -----------------------------------------------------------------

while True:
    try:
        # Solicita os números e a operação ao usuário
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        # Realiza a operação com base na escolha do usuário
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            # Trata o erro de divisão por zero
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                continue  # Volta para o início do loop
            resultado = num1 / num2
        else:
            # Trata a operação inválida
            print("Erro: Operação inválida. Por favor, use +, -, * ou /.")
            continue  # Volta para o início do loop

        # Exibe o resultado e encerra o programa
        print(f"O resultado é: {resultado}")
        break  # Sai do loop após uma operação bem-sucedida

    except ValueError:
        # Trata o erro de entrada não numérica
        print("Erro: Entrada inválida. Por favor, digite apenas números.")
    except Exception as e:
        # Trata qualquer outro erro inesperado
        print(f"Ocorreu um erro inesperado: {e}")
