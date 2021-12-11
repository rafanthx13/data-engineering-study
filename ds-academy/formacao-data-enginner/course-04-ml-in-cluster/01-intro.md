# Introdução

## Processamento Paralelo em Cluster

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-01.png)

Há duas coisa distintas:
+ Processamento paralelo: da pra fazer e até em uma única máquina, é a técnica de dividir para conquistar

Sistema distribuídos
+ Várias máquinas que se ligam como uma só. DIvidindo a carga de trabalha entre as máquinas, entre várias CPU/GPu entre várias máquinas

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-02.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-03.png)

Hadoop e o ambiente hadoop permite trabalhar assim: várias máquinas, varias cpu/gpu/ram juntas

O que é um sistema distribuído

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-04.png)

## Diferença entre GPU e CPU

**O que é CPU**

cpu: processador, unidade central de processamento.
cpu, estão restrita por core, e de forma 

**O que é GPU**

gpu:

Como surgiu: Com jogos, quando começaram a surgir, perceberam que o hardware não era bom para games. Aí veio a NVIDIA, que fundou as placas de vídeo.

Por volta do meio dos anos 2000, começaram a surgir os modelo de IA, e perceberam que envolvida operação de matrizes, que são capazes de ser paralelizadas, só que a CPU não oferece hardware para esse paralelismo.

Hoje quem usa GPU: games e IA.

**DIferença**
+ A GPU tem muito mais cores e assim muito mais velozes para processar em paralelo


Você usa cpu e gpu em conjunto

###  O que é programação paralela e outros conceitos

programação paralela: é você por parte de seu código para ser rodada em paralelo, como por exemplo, a multiplicação de matrizes ARRAY.

Processamento paralelo: executar um certo código de forma paralelo, pode ser pela cpu (tem números de core limitados), gpu (tem muito mais cores) ou num sistema distribuído, também chamado de cluster (varias maquinas)

O que é concorrência e paralelismo

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-05.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-06.png)

Sempre que dois processamento forem independentes, por definição se pode usar paralelização.

### Medida de desempenho - tera flops

O que é FLOPS

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-07.png)

A medida é usada para exprimir o desempenho de poder computacional.

Quantidade de operações sobre float por segundo

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-08.png)

### O que são Micro Services

MicroService é uma arquitetura de engenharia de Software.

O seu objetivo como Engenheiro/cientista de dados é: usar big data e entregar um resultado final. Em geral a gente entrega na forma de softwares ou uma API, que será chamada e assim retorna um resultado.

### App Monolítica: usada por default hoje
+ Usamos o modelo Front-End e Back-End

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-12.png)

É possivel dividir em 3 camadas: apresentação, regra de negócio e acesso ao BD

Vantagens

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-11.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-12.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-09.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-10.png)

### Pra que serve MIcroServices

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-16.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-17.png)

Ou seja: é dividir em pequenas coisas, e no final, acopla tudo

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-18.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-19.png)

Ou seja, se na app monolítica, para mudar um botão eu tenho que compilar tudo, na de micro-serviços, eu so mudo o micro-serviço que está chamando

**É SIMPLESMENTE BAIXO ACOPLAMENTO**

VANTAGENS

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-20.png)

DESVANTAGENS

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-21.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-22.png)

**E como tudo isso tem haver com IA/Cluster**

O modelo de ML treinado será subido em um Docker, e assim, acoplar na orquestração de meu sistemas

## API REST

Imagine que você tem um CRM

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-23.png)

Como o CRM é muito usado, imagine que ao invés de digitar, crie um sistema para reconhecer a voz para inserir os dados.

Isso já existe: speech-to-text do IBM Watson.

Agora, como eu integro esse sistema de voz ao meu sistema próprio do CRM. É aí que entra uma REST API

**O que é uma REST API**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-24.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-25.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-26.png)

## Como fazer deploys de Ml

Deploy é entregar/resolver o problema, e deixar o modelo pronto para ser usado

Exemplo de workflow de ML com deploy

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-27.png)

As várias possibilidades

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-01-28.png)

**IREMOS APENAS FAZER O DEPLOY DE MODELOS, NÃO VAMOS CRIÁ LOS**





