valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxa_juros = float(input("Digita a taxa de juros anual da modalidade escolhida(exemplo:0.01): "))
periodo = int(input("Digite o período de tempo em anos para o resgate: "))

valor_final = valor_inicial

#TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.
# n indica o número de vezes que o juros é contabilizado
n = 1
valor_final = valor_inicial * (1 + taxa_juros / n) ** (n * periodo)
valor_final = round(valor_final, 2)
print("Valor final do investimento: R$", valor_final)
