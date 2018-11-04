
from numeroPrimo import GeradorNumeroPrimo
from gerarChaves import Chaves
from criptografia import Criptografia

p = GeradorNumeroPrimo()
numero_p = p.numero_primo
print('\n P :',str(numero_p))

q = GeradorNumeroPrimo()
numero_q = q.numero_primo
print('\n Q :',str(numero_q))

chaves = Chaves(numero_p, numero_q)
chaves.gerar_chaves()

encripta = chaves.encripta_mensagem()
chaves.decripta_mensagem(encripta)