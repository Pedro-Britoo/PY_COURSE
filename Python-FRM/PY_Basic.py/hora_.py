horas = input()

bomdia = '0,1,2,3,4,5,6,7,8,9,10,11'
boatarde = '12,13,14,15,16,17'
boanoite = '18,19,20,21,22,23'

lista_numeros = [int(number) for number in bomdia.split(',')]



if horas in bomdia :
    print('bomdia')
    

if horas in boatarde:
    print('boatarde')
    
    
if horas in boanoite:
    print('boanoite')
