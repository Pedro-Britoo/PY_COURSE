def imprimir (a, b, c) :
    print(a, b, c)
    
imprimir(1, 2, 3)
imprimir(4, 5, 6)


def saudacao(nome):
    print(f'ola, {nome}!')
    
    saudacao('luiz otaivo')
    saudacao('Maria')
    saudacao('Helene')
    saudacao()
    




def soma(*args) :
    print(args, type (args))
    
    
    soma(1,2,3,4,5,6)