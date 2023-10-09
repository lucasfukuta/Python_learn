saldo_atual = float(input("Informe o saldo atual da conta bancária: "))
valor_deposito = float(input("Informe o valor a ser depositado na conta: "))
valor_retirada = float(input("Informe o valor a ser retirado da conta: "))

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
def calculo_das_transações(saldo_atual, valor_deposito, valor_retirada):
    saldo_final = saldo_atual + valor_deposito - valor_retirada
    return saldo_final

#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
saldo_final = calculo_das_transações(saldo_atual, valor_deposito, valor_retirada)    
print("Saldo atualizado na conta bancária: {:.2f}".format(saldo_final))
