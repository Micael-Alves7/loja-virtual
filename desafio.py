estoque = 100
vendas = 0
repos = 0

def venda():
    global estoque
    global vendas
    while True:
        valor = input("digite um valor pra venda ")
        if valor != "sair":
            try :
                valor = int(valor)
                if valor <= estoque:
                    estoque -= valor
                    vendas += valor
                else:
                    print("estoque insuficiente")
            except ValueError:
                        print("valor insuficiente")
        else:
            break

def reposicao():
    global estoque
    global repos
    while True:
        valor = input("digite um valor para repor")
        if valor != "sair":
            try :
                valor = int(valor)
                repos += valor
                estoque += valor

            except ValueError:
                print("entrada invalidade")
        else:
            break

print("bem vindo a loja")

def menu():
    global estoque, vendas, repos
    while True:
        print("bem vindo\n 1- vender\n 2- repor\n 3- estoque atual\n 4- encerrar expediente")
        opcao = int(input())
        if opcao == 1:
            venda()
        elif opcao == 2:
            reposicao()
        elif opcao == 3 :
            print(estoque)
        elif opcao == 4 :
            print(vendas, repos)
            exit()
        else:
            print("encerrar expediente")
            print("total de vendas: {}".format(vendas))
            print("total de repos: {}".format(repos))
menu()














