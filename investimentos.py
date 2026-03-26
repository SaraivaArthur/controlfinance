investimentos = input("Você já investiu antes? [S]IM ou [N]ÃO: ").upper()

if investimentos == 'S':
    sim = input("Você sabe o que é renda variável e fixa? [S]IM ou [N]ÃO: ").upper()
    if sim == 'S':
        print('Aqui está as melhores recomendações de investimentos ...')
    
elif investimentos == 'N':
    nao = input("Você sabe o que é renda variável e fixa? [S]IM ou [N]ÃO: ").upper()
    if nao == 'S':
        print('Aqui está as melhores recomendações de investimentos ...')
    elif nao == 'N':
        print('Explicação ...')    