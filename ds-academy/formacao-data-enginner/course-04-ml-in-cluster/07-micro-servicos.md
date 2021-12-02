# micro services

## Resumo

## PARTE 1 - O que é Micro-serviços

### O Que São Microsserviços?

clone-pdf


	Microservices é um padrão de arquitetura orientada a serviços em que os aplicativos
são criados como uma coleção de várias unidades de serviço independentes menores. É uma
abordagem de engenharia de software que se concentra em decompor um aplicativo em
módulos de função única com interfaces bem definidas. Esses módulos podem ser implantados
e operados independentemente por pequenas equipes que possuem todo o ciclo de vida do
serviço.

	O termo "micro" refere-se ao dimensionamento de um microsserviço que deve ser
gerenciável por uma única equipe de desenvolvimento (5 a 10 desenvolvedores). Nesta
metodologia, grandes aplicações são divididas em unidades independentes menores.

### Intro a Micro-Serviços

Envolve arqtuitetura e genhenhrai de software.

img-c4-07-01

img-c4-07-02

Lembrese: Na parte do deploy voce deve aplicar as mesmas etapas de limpeza e tranforçamoa dos dados de quanto fez na parte de develoment

### Arquitetura monolítica

img-c4-07-03

### Diferenaç entre SOA e Micro Serviços

img-c4-07-04

Os dois tarablham de forma bem parecidas, mas na iamgem a seguir tem a difenreça mais explícita

img-c4-07-05

SOA e MicroSeviços dividem a aplicaçâo monolitica em menores, mas micro-serviços divde em apps bem menores do que SOA.

Na pártica, no dia a dia, SOA é usada em grandes empresas. Já apps web e que usam IA/ML usam micro-serviços

É claro que SOA/Microserviços dao um problema para por tudo para funcionar

img-c4-07-06

img-c4-07-07

A ideia do micro-serviços é que cada componetne seja indenepndete

**middleware e api**

EM geral, usamos  mideleware na SOA para gerencia as mensagens/requisiçoes de um potnoto ao outro. Agora, no micro-serviços, usamos somente chaadas diferetas de API.

EM suma: na SOA há midrelware que éum sistema de mensagens que uasa coisa socmo AMPQP, MSMQ e SOAP para acesos remoto. Já microSrviçõs baseia em REST e mensagem simples

img-c4-07-08


img-c4-07-09


### Funcionalidade de micro-serviçoes


img-c4-07-10

duas razoes
+ simplifica o tsete e permite que o deplooys seja indenpende e asim, ser desenvlviod por equipes diferente  elinaugesn diferentes. Na partaica é como se cada serviço fosse uma pequena aplicaçâo e assim trabalhar de formas independentes

Resumindo: tudo fica menos acompladao, menos dependente um do out
ro e faiclita tudo 

img-c4-07-11

**OU SEJA, APRA FAZER ISOS, EU TENHO QUE PLANEJAR EM DIVIDIR O PORLBMEA/FUNCIONALDIADE EM PARTES/SERVIÇOS E CADA UMA DELAS FIQUE SERPARADSA**

img-c4-07-12

O idela é que cada serviço seja independente.

### Banco de dados no Micro Serivços

Em suma: micro-serviços é difidirum sitesma e mini-sistemas mais simples e independnetes entre si.

**COMO VAI FICAR O BANCO DE DADOS**

Para manter independete, entao **CADA SERVIÇO DEVE OFERECER UMA API PARA SEUS PRPIROS DADOS**

NO exmeplo abaixo,entao order Service API tem que consultar Customer Service APi emsmo que seestejam no mesmo banco dedados (desde que ambos sejam micro-serviçpos distaintso)

Dessa forma, as duas tabelas se tornam idepndees.

**NA VERDADE AS DUAS TABELAS PODEM ESTA'EM BANCO DE DADOS DIFERNETES**

### RPI  (R

img-c4-07-14

Imagine que tenha uma app com 15 micro-serviços, cada um com sua lingaugem/banc ded daso.

Mas como os serviçoes vao comunicar netre si?

Precismaos de um protocolod e comunicaçao

Para implementar usamos
+ REST
+ gRPC
  -Vamos usar esse na proximo capitulo
+ Apache Thrift

É necesśario entao estabelecer qual protoculo apra a troca de informaço entre os micro serviços? rest, gRPC, ApacehTRfit

### BUild e DEploys

img-c4-07-15

Vamos estudar DOcker/Kubernetes

### Desvantanges do micro-serviços

img-c4-07-16













