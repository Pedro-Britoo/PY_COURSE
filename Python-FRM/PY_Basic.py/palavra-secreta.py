palavra_secreta = 'lindo'
tentativa = input('digite uma letra para adivinha minha palavra secreta')
n_tentativas = 0

tentativa_nova = ''
    
    
    
    
    
for letras in palavra_secreta:
    if tentativa == letras:
        print (f"a tentativa foi um sucesso {tentativa}")
        break
    else: 
        while tentativa_nova != letras:
            tentativa_nova = input('tente novamente')
            if tentativa_nova == letras:
                 print (f"a tentativa foi um sucesso {tentativa_nova}") 
        break
                
                
                
        
               
            
        
        