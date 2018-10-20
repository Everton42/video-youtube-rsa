cifra = 'Dozdbv Orrn RqWkh Euljkw Vlgh Ri Olih'
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'	

for chave in range(26): 
    descriptografia = ''

    for caractere in cifra: 

        if caractere in alfabeto: 

            num = alfabeto.find(caractere)
            num = num - chave
            if num < 0:
                num = num + 26
            descriptografia = descriptografia + alfabeto[num]
        else:
            descriptografia = descriptografia + caractere

    print('hackeando chave #%s: %s' % (chave, descriptografia))
