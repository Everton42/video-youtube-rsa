#Sistema simples de criptografia do Algoritmo RSA

Desenvolvido para fins de aprendizado e compreens�o do conceito do algoritmo.

##O Reposit�rio cont�m o c�digo gerador de n�meros primos aleat�rios grandes e das chaves publicas e privada.

##Funcionamento

O RSA est� fortemente ligado � Teoria dos N�meros, sendo baseado em pilares como as opera��es de resto e fatora��o por n�meros primos. O algoritmo pode ser resumido nos passos descritos abaixo:
```
*	Obter dois n�meros primos p e q; (Utilizei o teste Miller-Rabin. � um teste probabil�stico para saber se  um n�mero n � primo de maneira eficiente).

*	Calcular n = pq;

*	Calcular F(n) = (p-1)(q-1); (Fun��o totiente de Euler)

*	Escolher mdc(F(n), E) == 1, ou seja, E e F(n) s�o coprimos (primos relativos);

*	 Calcular D sendo d*e = 1 mod(f(n)), ou seja, d seja o inverso multiplicativo de E em (mod f(n)); (Algoritmo de Euclides estendido)

*	Chave p�blica: (e, n); chave privada: (d, n);

*	Fun��o para cifrar uma mensagem m: C(m) = me mod n = c;

*	Fun��o para decifrar uma mensagem c: D(c) = cd mod n = m;
```
O RSA se mant�m devido � dificuldade em fatorar um grande n�mero (n) em n�meros primos (p e q). Se b � o n�mero de bits de n, ent�o existem v(2b-1) possibilidades a serem testadas em um eventual pior caso, o que resulta em complexidade de tempo. A t�tulo de curiosidade, considerando b = 2048, v(2b) resulta em um n�mero um pouco maior que 1,79.10308. Considerando uma superm�quina que consegue processar 1 bilh�o (109) de tentativas por segundo, seriam necess�rios mais de 5.10291 anos.

##Mais  informa��es:

[The RSA Encryption Algorithm (1 of 2: Computing an Example)]
(https://www.youtube.com/watch?v=4zahvcJ9glg)

[Criptografia RSA(canal Toda a Matem�tica)]
(https://www.youtube.com/watch?v=3jR62Mew8X4&t=534s)

[RSA Criptografia Assim�trica
e Assinatura Digital](http://braghetto.eti.br/files/Trabalho%20Oficial%20Final%20RSA.pdf)

https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb

https://en.wikipedia.org/wiki/RSA_(cryptosystem)

https://seer.imed.edu.br/index.php/revistasi/article/view/1639/1296

https://www.lambda3.com.br/2012/12/entendendo-de-verdade-a-criptografia-rsa/