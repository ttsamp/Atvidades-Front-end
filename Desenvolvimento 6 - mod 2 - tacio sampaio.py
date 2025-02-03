while True:
    nome_completo = input("Digite o nome completo: ")

    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                break
            else:
                print("Ano de nascimento inválido. Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro para o ano de nascimento.")

    idade = 2022 - ano_nascimento

    print(f"Nome: {nome_completo}")
    print(f"Idade em 2022: {idade} anos")

    # Pergunta se o usuário deseja inserir outra pessoa
    continuar = input("Deseja inserir outra pessoa? (s/n): ")
    if continuar.lower() != 's':
        break