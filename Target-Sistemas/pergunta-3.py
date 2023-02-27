import json
# abrindo o json 
with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)
# capturando os dados do json  para uma lista
faturamento = list()
for c in dados:
    while True:
        try:
            v = c['valor']
            break
        except:
            print('Valor Valido')

    faturamento.append(v)

    #  ultilizando o metódo List Comprehension para eliminar os dias em que o faturamento foi igual a 0
    faturamento_maior_zero = [faturamento for faturamento in faturamento if faturamento != 0.0]
    # media do faturamento mensal 
    media = sum(faturamento_maior_zero) / len(faturamento_maior_zero)
    # função pra trazer quantos dias, o faturamento foi maior do que a média mensal
    def quantidade_dias_maior_media(faturamento_maior_zero):
        return len([faturamento_maior_zero for faturamento_maior_zero in faturamento_maior_zero if faturamento_maior_zero > media])
    # buscar o  maior valor de faturamento ocorrido em um dia do mês  
    def buscarMaior(lst):
        i = float("-inf")
        for nr in lst:
            if nr > i:
                i = nr
        return i
    # buscar o menor valor de faturamento ocorrido em um dia do mês
    def buscarMenor(lst):
        i = float("inf")
        for nr in lst:
            if nr < i:
                i = nr
        return i


print(f'A média do faturamento mensal é: {media:.4f}')
print(
    f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi: {quantidade_dias_maior_media(faturamento_maior_zero)} ')
print(
    f'O maior valor de faturamento ocorrido em um dia do mês: {buscarMaior(faturamento_maior_zero)}')
print(
    f'O menor valor de faturamento ocorrido em um dia do mês foi: {buscarMenor(faturamento_maior_zero)}')
