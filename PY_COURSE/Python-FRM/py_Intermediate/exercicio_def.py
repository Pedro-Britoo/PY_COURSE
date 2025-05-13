numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
total = 1  

def multiplica(*args):
    global total 
    for num in args:
        total *= num
        print(total)

multiplica(*numeros)

print(f"{total}")







