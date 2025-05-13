numeros = (1,2,3,4,5,6,7,8)
vezes = (2,3,4)

def duplicar(numero, vezesduplicar):
    resultado = numero * vezesduplicar
    def mostrar():
        return f"{numero} x {vezesduplicar} = {resultado}"
    return mostrar




for n in numeros:
    for v in vezes:
        func = duplicar(n,v)
        print(func())


    
    
    
    




