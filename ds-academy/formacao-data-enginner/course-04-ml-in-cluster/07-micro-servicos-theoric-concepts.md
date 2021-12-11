# micro services

## Resumo

## PARTE 1 - O que é Micro-serviços

### O Que São Microsserviços?

	Microservices é um padrão de arquitetura orientada a serviços em que os aplicativos
são criados como uma coleção de várias unidades de serviço independentes menores. É uma
abordagem de engenharia de software que se concentra em decompor um aplicativo em
módulos de função única com interfaces bem definidas. Esses módulos podem ser implantados
e operados independentemente por pequenas equipes que possuem todo o ciclo de vida do
serviço.

	O termo "micro" refere-se ao dimensionamento de um microsserviço que deve ser
gerenciável por uma única equipe de desenvolvimento (5 a 10 desenvolvedores). Nesta
métodologia, grandes aplicações são divididas em unidades independentes menores.

### Intro a Micro-Serviços

Envolve arqtuitetura e genhenhrai de software.

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-01.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-02.png)
Lembrese: Na parte do deploy você deve aplicar as mesmas etapas de limpeza e tranforçamoa dos dados de quanto fez na parte de develoment

### Arquitetura monolítica

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-03.png)
### Diferenaç entre SOA e Micro Serviços

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-04.png)
Os dois tarablham de forma bem parecidas, mas na iamgem a seguir tem a difenreça mais explícita

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-05.png)
SOA e MicroSeviços dividem a aplicação monolitica em menores, mas micro-serviços divde em apps bem menores do que SOA.

Na pártica, no dia a dia, SOA é usada em grandes empresas. Já apps web e que usam IA/ML usam micro-serviços

É claro que SOA/Microserviços dao um problema para por tudo para funcionar

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-06.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-07.png)
A ideia do micro-serviços é que cada componetne seja indenepndete

**middleware e api**

EM geral, usamos  mideleware na SOA para gerencia as mensagens/requisiçoes de um potnoto ao outro. Agora, no micro-serviços, usamos somente chaadas diferetas de API.

EM suma: na SOA há midrelware que éum sistema de mensagens que uasa coisa socmo AMPQP, MSMQ e SOAP para acesos remoto. Já microSrviçõs baseia em REST e mensagem simples

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-08.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-09.png)

### Funcionalidade de micro-serviçoes


![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-10.png)
duas razoes
+ simplifica o tsete e permite que o deplooys seja indenpende e asim, ser desenvlviod por equipes diferente  elinaugesn diferentes. Na partaica é como se cada serviço fosse uma pequena aplicação e assim trabalhar de formas independentes

Resumindo: tudo fica menos acompladao, menos dependente um do out
ro e faiclita tudo 

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-11.png)
**OU SEJA, APRA FAZER ISOS, EU TENHO QUE PLANEJAR EM DIVIDIR O PORLBMEA/FUNCIONALDIADE EM PARTES/SERVIÇOS E CADA UMA DELAS FIQUE SERPARADSA**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-12.png)
O idela é que cada serviço seja independente.

### Banco de dados no Micro Serivços

Em suma: micro-serviços é difidirum sitesma e mini-sistemas mais simples e independnetes entre si.

**COMO VAI FICAR O BANCO DE DADOS**

Para manter independete, então **CADA SERVIÇO DEVE OFERECER UMA API PARA SEUS PRPIROS DADOS**

NO exmeplo abaixo,então order Service API tem que consultar Customer Service APi emsmo que seestejam no mesmo banco dedados (desde que ambos sejam micro-serviçpos distaintso)

Dessa forma, as duas tabelas se tornam idepndees.

**NA VERDADE AS DUAS TABELAS PODEM ESTA'EM BANCO DE DADOS DIFERNETES**

### RPI  (R

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-14.png)
Imagine que tenha uma app com 15 micro-serviços, cada um com sua lingaugem/banc ded daso.

Mas como os serviçoes vão comunicar netre si?

Precismaos de um protocolod e comunicaçao

Para implementar usamos
+ REST
+ gRPC
  - Vamos usar esse na próximo capitulo
+ Apache Thrift

É necesśario então estabelecer qual protoculo para a troca de informaço entre os micro serviços? rest, gRPC, ApacehTRfit

### Build e Deploys

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-15.png)
Vamos estudar DOcker/Kubernetes

### Desvantanges do micro-serviços

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-07-16.png)












