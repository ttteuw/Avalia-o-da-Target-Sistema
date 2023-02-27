# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53


E = ['SP', 'RJ', 'MG', 'ES', 'OUTROS']

faturamento = list()
for c in E:
    # Capturando e tratando os valores digitados:
    while True:
        try:
            v = float(input(f'Digite o faturamento mensal de {c}: '))
            if v < 0:
                print('Valor INVÁLIDO! Digite apenas valores maiores ou iguais a "0":')
            break
        except:
            print('Valor INVÁLIDO! Digite apenas valores reais!')

    # Armazenando os valores digitados na lista faturamento
    faturamento.append(v)

# Calculando o faturamento total da distribuidora:
faturamento_total = sum(faturamento)
print(f'O faturamento total da Distribuidora foi: R$ {faturamento_total:.2f}'.replace('.', ','))

# Calculando e exibindo o percentual relativo de cada filial de cada estado:
cont = 0
for i in faturamento:
    cont += 1
    percentual = ((i / faturamento_total) * 100)
    print(f'O percentual de faturamento de {E[cont - 1]} é: {percentual:.2f} %')