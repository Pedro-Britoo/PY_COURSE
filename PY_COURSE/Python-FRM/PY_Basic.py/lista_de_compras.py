lista_de_compras = []
preco = 0
funcionando = True

while funcionando:
    acao = input('[i] Inserir | [a] Pagar | [l] Listar: ')

    if acao.startswith('i'):
        fruta = input('Escolha uma fruta: [p] Pera (R$2), [m] Maçã (R$3), [g] Goiaba (R$1): ')
        if fruta.startswith('p'):
            lista_de_compras.append('pera')
            preco += 2
        elif fruta.startswith('m'):
            lista_de_compras.append('maca')
            preco += 3
        elif fruta.startswith('g'):
            lista_de_compras.append('goiaba')
            preco += 1
        else:
            print('Fruta inválida.')

    elif acao.startswith('l'):
        print("Lista de compras:")
        for i, item in enumerate(lista_de_compras, 1):
            print(f"{i}. {item}")
        print(f"Total parcial: R${preco}")

    elif acao.startswith('a'):
        print("Pagamento efetuado.")
        print(f"Total: R${preco}")
        funcionando = False

    else:
        print("Opção inválida.")





    
        
        


        
        
        
    
    

    
        
    