ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input("Informe a quantidade de ativos: "))

# Entrada dos códigos dos ativos
for i in range(quantidadeAtivos):
    codigoAtivo = input("Informe o tipo do ativo {}: ".format(i + 1))
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()
# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
ativo = "\n".join(ativos)
print(ativo)
# Outra forma de exiber os ativos linha por linha:
#for ativo in ativos:
#    print(ativo)
