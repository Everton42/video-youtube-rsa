
class Criptografia(object):

    def criptografia(self, m, e, n):
        c = (m**e) % n
        return c

    def descriptografia(self, c, d, n):
        m = c**d % n
        return m

    def encripta_mensagem(self):
        s = input("Digite a mensagem: \t")
        print('='*5 + ' Digite as chaves públicas: ' + '='*5)
        e = int(input("Chave e: \t"))
        n = int(input("Chave n: \t")) 
        enc = ''.join(chr(self.criptografia(ord(x), e, n)) for x in s)
        print('Texto Cifrado: ', enc, '\n')
        return enc
        
        
    def decripta_mensagem(self, s):
        self.s = s
        print('='*5 + ' Digite as chaves privadas: ' + '='*5)
        d = int(input("Chave d: \t"))
        n = int(input("Chave n: \t")) 
        dec = ''.join(chr(self.descriptografia(ord(x), d, n)) for x in s)
        return print('Texto Simples: ', dec, '\n')