numeros = (0, 1, -3, -2, -7, 10, 20, 50, -40)

def classificacao(*args):
    positivo = []
    negativo = []
    nulo = []
    for num in args:
        if num == 0:
            nulo.append(num)
        if num > 0:
            positivo.append(num)
        if num < 0:
            negativo.append(num)
    
    print("Positivos:", positivo)
    print("Negativos:", negativo)
    print("Nulos:", nulo)

classificacao(*numeros)

            

            
    
    


            
            
        