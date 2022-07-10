# 01 - Conceitos e Introdução



Tempo: 01h11m02s || Quantidade de Vídeos 11


## Boas Vindas, Objetivo do Curso e Conceitos Introdutórios - Aula 01 (04m55s)


Introduçâo bem básica

img-01


## Responsabilidades dos Analistas e Cientistas de Dados - Aula 02 (06m04s)

img-03

## Responsabilidades do Engenheiro de Dados na Construção do Data Pipeline - Aula 03 (06m43s)


img-02


## Data Pipelines para o Processo de ETL - Aula 04 (07m39s)


Extração, Trasnformaçâo e eCarga: BUcsar os dados de locais difenretes, modificalos e então  fazer o upload em algum lugar

Os dados sâo madnado para uma área chamada 'staging area' e é lá que é feita a tranformação. Depois carrega num DW  enta^podera ser feito toda analise..

O airflow faz isso: acessa diversa fontes e manda para outras bases, fazendo a tranformaçao nesse processo

## Data Pipelines para Machine Learning - Aula 05 (06m25s)

exemplo de pipeline de dados em Machine Learning

img-04

podemos desenvolver todo esse pipeline com o airflow

img-06

## Representação em Grafos de Pipelines - Aula 06 (06m20s)

exemplo de modlagem de pipeline semples para um mahcine learning

img-07

onde a tareda C depende da B, a B da A e a A é a primeira tarefa

DAG: É aciclcio, ou seja, não cai em um ciclo, nao em em um deadlock

img-08

As dags vai seguir sempre da esquerda pra dirieta e nao vai ter ciclo nem for para voltar

img-09

## Pipelines em Grafos vs Scripts Sequenciais - Aula 07 (07m19s)

**Porque ao invez de usar o airflow eu nô posso desenvolver um script py sequencial das tarefas?**

img-10

AO usar uma ferramenta de worflow, voce pode executar tarefas simultanemnete não havendo dependendicia entre elas. Ex: fazer a imagem acima em script tem que busca um dado e depois o otruo. Num worfklow, elas eriam tarefas distintas e executariam  na mesma forma, POIS NÂO HÁ DEPENDENCIA ENTRE ELAS. MAS SE FOSES EM SCRIPT HAVERIA DEEPNDENCIA POIS SERIA SEQUENCIAL.

É como no pentaho, ao clicar em EXECUTAR vai automaticamnete executar sem dependenicas essa duas tarefas, desde que você arquitete bem. Agora, se fosse n script, deveria ter um timeout ou alguma inteleigenica para deixar essa tarefas indepnendetes e nexecutar simultamentment (multi-threasd, o qu eé chato.

Pentaho e AIdflow já dá isos naturalmente

Visão usadno o airflow

img-11

**a grande vantagem do airflow ao script é manipular a dependencia e concorrencia das tarefas**


## Introdução e Porque Escolher o Apache Airflow - Aula 08 (05m32s)

img-12

img-13

**PYTHON TEM UMA QUANTIDADE GIGANTE E ULTRA-FLEXÍVEL PARA EDITAR E FAZR O QUE QUISER COM DADOS**


## Airflow vs Scripts Bash - Aula 09 (05m31s)

img-14

O airflow tem 'OPeradores' que já facilita fazer muitas coisa, é como uma lib já pronta para se concetar a diversas coisa, aaism, em airflow já tme muita coisa montada: Ex: já está montado o operador par amandar email, entâo voce nao precisa dessenvolver um script bash par amnadar um email desde importar uma lib especificamente para isso.


## Airflow vs outros Worloads Managers - Aula 10 (07m59s)

outras ferramentas parecida com airflow para ETL

img-15

A unica coisa ruim do airflow é que é umpouquinho pesado e nâo se dá muito bem no windows

Os principais concorrente
+ Luigi: Faz quase tudo que o airflow e é em python
+ Nifi: Tme interface gráfica

**quando nao usar aiflow**

img-16

## Componentes e Arquitetura do Airflow - Aula 11 (06m35s)

img-17

O que é Dag: grafico aciclo direcionado. Sera um arquivo escrito em python que vamos definis os nós arestas, dependencias e tarefsa

**COMpoennet do airflow**

img-18

+ User: a sua conta, pode haver varias contas
+ aiflow webserver: o servidor web subido, ou seja, a pagina web apra geranciar e monitorar tudo
+ aiflow metastores: Os dasdos de monitormaneto ficam num RDBS, que pode ser qualquer um (SQLITE, mysql e etcc)
+ AIflow Workeres: unidade que executam as tarefas. Há mais de uma entâo permite paralelismo
+ AIflorw Schedule: monitora e vigia alem de decidir a ordem do que vi executar as coisas
+ Diretorio de Dasg
  - VOce pode fazer uma DASG esperar por outro, como um seosr
