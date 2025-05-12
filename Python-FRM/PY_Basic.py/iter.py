texto = iter('luiz')
iterador = iter(texto)
#print(texto.__next__())
#(texto.__next__())
#print(texto.__next__())
#print(texto.__next__())

while True :
    try:
        print(next(iterador))
    except StopIteration:
        break
    