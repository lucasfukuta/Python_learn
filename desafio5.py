valor = float(input("Digite o valor do deposito: "))

if valor > 0:
    #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
    print("Deposito realizado com sucesso!")
    print("Saldo atual: R$ {:.2f}".format(valor))
elif valor == 0:
    #TODO: Imprimir a mensagem de encerrar o programa.
    print("Encerrando o programa...")
else:
    #TODO: Imprimir a mensagem de valor inválido.
    print("Valor invalido! Digite um valor maior que zero.")
