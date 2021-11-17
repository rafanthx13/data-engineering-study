# Design e Implementação de Data Warehouses

## Introduçâo

### O que é engenharia de Dados

Pode-se entender como: Engenharia dedicada a criar sistsemas,este para processar e tratar dados que formam o Big Data.
+ Hoje é uma funçâo, para lidar com Big Data.
+ E big data é repsonsaǘel pela grande tranformaçao na IA, pois é apartir delees que se faz ML e asism soluçôes incriveis

**O que faz** Cria sistema e resolve problemas de processamento de dados, de dados em tempo real e de manipular toda essa enorme quantidade de dados juntas

**proposito**: forncecer soluesço e plataformas de big data modulares e escalaveis para que cientistas de dados possam fazer o seu trabalho de analise

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-1-01.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-1-02.png)

### Data Warehouse é importante para Big Data

Implementar uma infra de Big Data é algo extremamente trabalhoso e custa dinheiro. Pa rauma empresa que vai tomar susas decisoes para Big Data é algo que leva tempo, pode levar uma decada.

E muitas empresas ainda estâo finalizando o seu BI Business Inteligence

DW é apenas um pequeno pedaço do Big Data.

Entâo, por conta disso, o DW ainda tem muitos anos de vida.

Ouse aj, o BIg Data nâo está matatnado o DW, mas o DW está se adaptando ao Big Data.

ENtâo, DW ainda é revelante na era do Big Data

## BI, DW, Data Mart e OLTP

OLTP: Bancos de dados que armazenam transçoes, dados transacionais

DW: É a centralizaçao desses varios bancos de OLTP, em geral, é feito um processo de ELT entre OLTP e DW

Dsta Mart: AO invez de um único DW ponde-se ter vários DtaMarts. Seria por exmeplo um mini DW, uma opporçao do DW

BI: É tomar as deciseos de acordo com os dadosdo DW. É extrari dados e motrar os gráficos para a tomada de decisao

## Quando usar um DW

O objetivo do DW: Extrair informaçoes de sistesmas transacionais para os tomadores de decisao.

Antes do DW, voce tinha que extrai os dados das mais variadas fontes a medida que precisava dele. Entao surgia o seguinte problema
+ Esforço duplicadao (setores difernetes podem quere omesmo dado e fazer o mesmo esforço)
+ Difenretes regras de extraçao
+ Diferentes meta-dados de diversos lugares
+ Diversos níveis de granularidade
+ Tratamenteos diferente para diversas situaçôes
+ Pode-se sobrecarregar esses sistesma se fizer várias queries

É aí que surge o DW. Entao quando vou usar
+ Quando tiver muitos, mas muitos Bancos de dados, e voce  nao qure fazer consultas a esses siestma de origem a toda hora
+ Evitar de acessar os sistsemas origianis
+ Informaçâo consoldiadada: Voce pode simplificar mais os dados
+ Buscar somente informaçoes relevantes (voce pdoe diminuir os dados que nao vao ser tao imporantes?)
+ Dados dispersos em 

Em suma:
+ Um repositorio central
+ A informaçao limpa e consoldiadaad
+ COncnetrar nas informçaçoes soesmnte releavantes
+ Centralizar diversos dados de diversos banco de dadaos
+ **PARA consolidad os dados para geraçao de relatorios de bI E Tomada de decisao**

DateWarehouse é para dadods esturutados. Datalake é para nao estrututradas

## Vantagens e limitaçoes do DW

O dw serve como um centralizador de todos os dados da empresa, fornecendo os dados para o BI

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-1-03.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-1-04.png)

## Caracteristicas do DW

1. Orientado ao negócio da empresa
+ As questoes técnicas sao as mesmas, mas a forma vária umpouco pela forma da empresa
2. Nã Volátil
+ Ou seja, eu vou manter o histórico dos daods. Enfim, eu mantenho dados por um certo tempo delimitado
3. Variante no Tempo
+ Eu tenho que permitir que as concsultas sejam feita nnos diversos e em qualquer intervlao de tempo


## BI x DS

Não são as mesma coisa.

Os dosi fazem ese processo
Dado - informaçao - conhecimento => decisao

DEFINÇAO DA GARTNER GROUP DE BI

BI: Processo de transformar dados em informaçao, e atraves das descobertas, tranformar informaçao em conhceimento que suporte a tomada de decisao.
+ Perceba que paraece com DS

**Diferença**
BI: Responde perguntas Descritivas e Diagnosticas
+ Oque aconteceu e porque isso aocntece

DS: Alem do que o BI faz Preditiva e PREsctivia (ML)
+ O que acontecerá e o que deve ser feito


![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-1-06.png)


## OLAP e OLTP

Sao formas de criar um banco de dados:
OLAP (ONline ANalytics Processing); OLTP (Online Transaction Processing)

É mais normal usamros OLAP para DW, em opsosiçao ao OLTP que é para os bancos operacionais da emrpesa.

O DW sao dados de froma analitica, por isos, apra ele, usamos OLAP

Exemplo de OLTP; REgistrar transçoes de um banco


MODELO OLTP (ENTIDADE-RELACIONMENTO, SQL COMUN)
+ MOdelo entidade relacionametno
+ Traballahmso com normalizaçâo
+ É o noss uso comun, 

MODELO OLAP (DW, DIMENSAO-FATO)
+ Modelo dimensional
+ Fazemos uma desnormalizaçôa
+ Para aplicaçeoes ANLITICAS, DW

## OLAP e o modelo DImensional

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-1-08.png)

Há metodos especificos de OLAP

Tem ferramentas classificadas em 5 tipos:
ROLAP, MOLAP, HOLAP, DOLPA, WOLAP, XOLAP

Sâo usadas para crciar banco de dados para fazer ANÁLISE

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-1-09.png)

**Modelo DImensional**

+ É star-schema ou Snow-Flake
+ Há tabelas Fatos (a tabela central) e Dimensôes (Cada pedacinho)

## ETL

ETL: Extract, Tranformation, Load
+ Conceito: Passar os dados de um BD a outro lugar, fazendo alguma modificaçâo se precisar.
+ Será mais estudado no capitulo 6

EM geral como é o prcesso:
+ Eu extraio os dados da fonte e coloco no 'staging area' (rea intermediaria) é nela que os dados sao treinados, limpados 

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-1-10.png)



![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-1-11.png)












