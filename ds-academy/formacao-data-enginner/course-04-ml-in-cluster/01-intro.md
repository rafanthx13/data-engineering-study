# Introdução

## Processamento Paralelo em Cluster

img-c4-01-01

Há duas coisa distintas:
+ Processamento paralelo: da pra fazer eaté em uma unica maquia, é a tecnoca de divir para conquistar

Sistema distribuidos
+ Várias maquinas que se ligam como uma só. DIvidindo a carga de trabalha entre as máquinas, entre varias CPU/GPu entre varias maquinas

img-c4-01-02

img-c4-01-03

Haddop e o ambite haddop permite trabalhar assim: varias maquinas, varias cpu/gpu/ram juntas

O que é um sistema distribuido

img-c4-01-04

## DIferença entre GPU e CPU

pq ia ts em alta agora

big dat e ao hadrware (capaciaded computacional)

**O que é CPU**

cpu: processador, unidade central de procdessamento.
cpu, estao restrita por core, e de forma 

**O que é GPU**

gpu:

COmo surgiu: COm jogos, quando começaram a surgir, perceberam que o hardware não era bom para games. Aí veio a NVIDIA, que fundou as placas de vídeo.

POr volta do meio dos anos 2000, começou a surgiur os modelo de IA, e percebram que envolvida operaçâo de matrizes, que são capazes de ser paralelizadas, só que a CPU nao oferece harware para esse paralelismo.

Hoje quem usa GPU: games e IA.

**DIfenreça**
+ A GPU tem muito mais cores e asism muito mais veloses para processar em paralelo


VOce usa cpu e gpu em conjunto

###  O que é programaço paralaela e otruos conceitos

progmraçao paralela: é voce por parte de seu codigo apra ser rodada em paralelo, como por exmeplo, a multiplaicaço de matrizes ARRAY.

Procesasmento paralelo: executar um certo código de forma paralaelo, pode ser pela cpu (tem numeros de core slimitados),g pu (tem muito mais cores) ou num sistema distribuido, tambem chamado de cluster (varias maquinas)

O que é concorrencia e paralelismo

img-c4-01-05

img-c4-01-06

Sempre que dois processamento forem independentos, por definiçao se pode usar paralelização.

### Medida de desempenho - tera flops

O que é FLOPS

img-c4-01-07

Medida é usada para expremir o desemepnho de poder computacional.

Quantidade de operaçoes sobre float por segundo

img-c4-01-08

### O que sâo Micro Services

MicroService é uma arqutitetura de engenharia de Software.

O seu objetivo como Engenhro/cientisda de dados é: usar big data e entregar um resultado final. EM geral agente entrega na forma de softwares ou uma API, que será chamada e asism retorna um resultado.

### App Monolitica: usada por default hoje
+ Usamos o modelo Fornt-End e Back-End

img-c4-01-12

É possivel dividir em 3 camads: apresentaçao, regra de negoicio e acesso ao BD

Vantagesn

img-c4-01-11

Des

img-c4-01-12

img-c4-01-09

img-c4-01-10


### Pra que serve MIcro Services



img-c4-01-16

img-c4-01-17

Ou seja: é dividir em pequenas coisas, e no final, acopla tudo

img-c4-01-18

img-c4-01-19

Ou seja, se na app monolitica, par amudar um botao eu tenho que compilar tudo, na de micro-serviços, eu so mudo o micro-serviço que está chaamdno

**É SIMPLIKSMNTE BIXO ACOPLAMENTO**

VANTAGESN

img-c4-01-20


DESVANTANGES

img-c4-01-21

img-c4-01-22

**E como tudo isos tem haver com IA/Cluster**

O modeo de ML treinado será subido em um DOcker, e asism, acoplar na orquestração de meu sistemas

## API REST

Imagine que vote tem um crm

img-c4-01-23

Como o CRM é muito usado. Imagine que ao invez de digitar, crie um sistema para reocnhecer a voa para inserir os dados.

Isos já exsite: speech-to-text do IBM Watson.

Agora, como eu integro esse sistema de voz ao meu sistema proprio do CRM. É ai que entra uma REST API

**O que é uma REST API**


img-c4-01-24

img-c4-01-25

img-c4-01-26

## COmo fazer deploys de Ml

Deploy é entregar/resolver o problema, e deixar o modelo pronto pra ser usado

Exempl de worflow de ML com deploy

img-c4-01-27

As varias possibildiades

img-c4-01-28

**IREMOS APANAES FAZER O DEPLY DE MODELOS, NAO VAMOS CRIALOS**



