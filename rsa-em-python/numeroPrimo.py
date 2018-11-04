# Algoritmo para encontrar números primos grandes : 
#   https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb

from random import randrange, getrandbits

class GeradorNumeroPrimo:
    def __init__(self):
        self.numero_primo = self.gerar_numero_primo()

    def teste_miller_rabin(self,n, k=128):
        """ Testa se o número é primo
            Param:
                n - número testado
                k - número de testes
            return True if n is prime
        """
        if n < 6:  # válida alguns casos
            return [False, False, True, True, False, True][n]
        # Testa se n é par
        if n <= 1 or n % 2 == 0:
            return False
        # encontra r e s
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2
        # executa k testes
        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True
    def tentativa_de_numero(self,length):
        """ Gera um número primo inteiro aleatório.
                retorna o número
        """
        # gera bits aleatórios
        self.numero_primo = getrandbits(length)
        # aplica uma mascara para determinar valor 1 para MSB e LSB
        self.numero_primo |= (1 << length - 1) | 1
        return self.numero_primo
    def gerar_numero_primo(self,length=5):
        ''' Cria um número primo testado
            parâmetros: 
                length - tamanho em bits
        '''
        self.numero_primo  = 4
        # Continua enquanto o teste falha
        while not self.teste_miller_rabin(self.numero_primo, 128):
            self.numero_primo  = self.tentativa_de_numero(length)
        return self.numero_primo 

