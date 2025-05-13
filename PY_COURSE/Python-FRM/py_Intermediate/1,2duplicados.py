lista1 = [3, 7, 12, 5, 8, 10, 15]
lista2 = [4, 10, 7, 18, 5, 21, 9]

def funcao(listaBoa : set, listaRuim : list):
    for i in listaRuim:
        listaBoa.add(i)

def func_duplicatas() :
    s1 = set()
    s2 = set()
    funcao(s1, lista1)
    funcao(s2, lista2)
    comum = s1.intersection(s2)
    print(f'o comum e {comum}')
    



func_duplicatas()


