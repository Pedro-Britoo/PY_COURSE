numero = input("Digite um número inteiro: ")

par = []
impar = []

# Verifica se é um número inteiro válido
if not numero.isdigit():
    print('Isso não é um número inteiro.')
else:
    numero = int(numero)

    if numero % 2 == 0:
        par.append(numero)
        print('Esse número é par.')
    else:
        impar.append(numero)
        print('Esse número é ímpar.')

    print(f"Pares: {par}")
    print(f"Ímpares: {impar}")
