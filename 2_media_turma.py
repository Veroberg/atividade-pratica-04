# Atividade Prática 04 - Questão 2
#
# Crie um programa que permita a um professor registrar as notas de uma turma.
# Ele deve calcular a média da turma, ignorando notas inválidas.
#
# -----------------------------------------------------------------

notas = []
print("Digite as notas da turma (ou 'fim' para terminar):")

while True:
    entrada = input("> ")

    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)
        # Valida se a nota está entre 0 e 10
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Por favor, digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")

# Calcula e exibe a média das notas válidas
if notas:
    media = sum(notas) / len(notas)
    print(f"\nNotas inseridas: {notas}")
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")
