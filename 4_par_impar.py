# Atividade Prática 04 - Questão 4
#
# Crie um programa que solicite números inteiros e verifique se são pares ou ímpares.
# O programa deve continuar até o usuário digitar 'fim'.
#
# -----------------------------------------------------------------

pares = 0
impares = 0

print("Digite números inteiros (ou 'fim' para terminar):")

while True:
    entrada = input("> ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
            pares += 1
        else:
            print(f"O número {numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

print(f"\nNúmeros pares inseridos: {pares}")
print(f"Números ímpares inseridos: {impares}")
