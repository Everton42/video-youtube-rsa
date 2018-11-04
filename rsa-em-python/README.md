# Sistema simples de criptografia do Algoritmo RSA

Desenvolvido para fins de aprendizado e compreensão do conceito do algoritmo.

## O sistema gera números primos grandes, chaves públicas e privada, encripta e decripta com as chaves.

### Funcionamento

O RSA está fortemente ligado à Teoria dos Números, sendo baseado em pilares como as operações de resto e fatoração por números primos. O algoritmo pode ser resumido nos passos descritos abaixo:

*	Obter dois números primos p e q; (Utilizei o teste Miller-Rabin. É um teste probabilístico para saber se  um número n é primo de maneira eficiente).

*	Calcular n = p*q;

*	Calcular phi(n) = (p-1)(q-1); (Função totiente de Euler)

*	Escolher mdc(phi(n), E) == 1, ou seja, E e phi(n) são coprimos (primos relativos);

*	 Calcular D sendo d*e = 1 mod(phi(n)), ou seja, d seja o inverso multiplicativo de E em (mod phi(n)); (Algoritmo de Euclides estendido)

*	Chave pública: (e, n); chave privada: (d, n);

*	Função para cifrar uma mensagem m: m^e = c mod(n);

*	Função para decifrar uma mensagem c: c^d = m mod(n);

O RSA se mantém devido à dificuldade em fatorar um grande número (n) em números primos (p e q). Se b é o número de bits de n, então existem v(2b-1) possibilidades a serem testadas em um eventual pior caso, o que resulta em complexidade de tempo. A título de curiosidade, considerando b = 2048, v(2b) resulta em um número um pouco maior que 1,79.10308. Considerando uma supermáquina que consegue processar 1 bilhão (109) de tentativas por segundo, seriam necessários mais de 5.10291 anos.

## Mais  informações:

[The RSA Encryption Algorithm 1 of 2: Computing an Example](https://www.youtube.com/watch?v=4zahvcJ9glg)

[Criptografia RSA(canal Toda a Matemática)](https://www.youtube.com/watch?v=3jR62Mew8X4&t=534s)

[ RSA Criptografia Assimétrica e Assinatura Digital ](http://braghetto.eti.br/files/Trabalho%20Oficial%20Final%20RSA.pdf)

https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb

https://en.wikipedia.org/wiki/RSA_(cryptosystem)

https://seer.imed.edu.br/index.php/revistasi/article/view/1639/1296

https://www.lambda3.com.br/2012/12/entendendo-de-verdade-a-criptografia-rsa/
