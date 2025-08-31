# Atividade Prática 04 - Questão 3
#
# Crie um programa que verifique se uma senha é forte.
# A senha deve ter pelo menos 8 caracteres e conter um número.
#
# -----------------------------------------------------------------

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    # Verifica o comprimento da senha
    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        continue

    # Verifica se a senha contém pelo menos um número
    tem_numero = False
    for char in senha:
        if char.isdigit():
            tem_numero = True
            break
    
    if not tem_numero:
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    # Se a senha passou em todas as verificações, ela é considerada forte
    print("Senha forte inserida! Acesso concedido.")
    break
