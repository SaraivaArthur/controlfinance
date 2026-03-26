itens = [] 

while True:
    aifinance = input(
        "Escolha uma opção: [I]NSERIR [A]PAGAR [L]ISTAR [S]AIR [+]SOMAR: "
    ).upper()

    # INSERIR
    if aifinance == "I":
        nome = input("Digite o nome do item: ")
        valor = float(input("Digite o valor do item: "))

        itens.append((nome, valor))  # salva na lista!!
        print(f"Item {nome} com valor R${valor:.2f} inserido!")

    # APAGAR
    elif aifinance == "A":
        nome = input("Digite o nome do item a ser apagado: ")

        for item in itens:
            if item[0] == nome:
                itens.remove(item)
                print(f"Item {nome} apagado!")
                break
        else:
            print("Item não encontrado.")

    # LISTAR
    elif aifinance == "L":
        print("\n--- GASTOS -----------")

        if not itens:
            print("Nenhum item cadastrado.")
        else:
            for nome, valor in itens:
                print(f"{nome} - R${valor:.2f}")

        print("----------------------\n")

    # SAIR
    elif aifinance == "S":
        print("Programa encerrado.")
        break

    #SOMAR OS VALORES

    elif aifinance == "+":
        total = sum(valor for _, valor in itens)
        print(f"Total dos gastos: R${total:.2f}")

    else:
        print("Opção inválida.")