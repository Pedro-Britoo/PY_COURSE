precos = (100, 200, 300, 400)
descontos = (0.10,)  

def calcular_Desconto(preco, taxa) :
    res_taxa = preco * taxa 
    def exibir():
        return f"{preco} x {taxa} = {res_taxa}"
    return exibir

for num in precos:
    for taxa in descontos:
        func =calcular_Desconto(num, taxa)
        print(func())
