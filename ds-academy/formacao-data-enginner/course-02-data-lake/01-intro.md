# Introdução

## Refs

Enterprise Big Data Lake
https://www.amazon.com.br/Practical-Enterprise-Data-Lake-Insights/dp/1484235215?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=data+lake&qid=1526000730&sr=8-8&ref=sr_1_8

The Enterprise Big Data Lake
https://www.amazon.com.br/Enterprise-Big-Data-Lake/dp/1491931558?keywords=big+data+lake&qid=1526000761&sr=8-1&ref=sr_1_1

Data Lake Architecture: Designing the Data Lake and Avoiding the Garbage Dump
https://www.amazon.com.br/Data-Lake-Architecture-Designing-Avoidingebook/dp/B01DPEGSO4?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=data+lake&qid=1526575032&sr=8-3&ref=sr_1_3

Data Lake
https://martinfowler.com/bliki/DataLake.html

Azure Data Lake
http://www.jamesserra.com/archive/2015/05/azure-data-lake/

Top 5 Differences Between Data Lakes and Data Warehouses
https://www.blue-granite.com/blog/bid/402596/top-five-differences-betweendata-lakes-and-data-warehouses

Design Fast Data Architecture for Big Data with Logical Data Warehouse & Lakes
https://www.youtube.com/watch?v=bTRNkouGO-Q

Big Data na Globo.com
https://www.slideshare.net/renangpa/big-data-na-globocom

Kylo
https://www.thinkbiganalytics.com/kylo/

Message Oriented Middleware (MOM)
https://docs.oracle.com/cd/E19316-01/820-6424/aeraq/index.html

## OBS

A DSA tem um curso de BIga Dta GRATUITO
+ Há um curso de Python e Haddop apra cientista de dados, mas essse curso é par aenisnar ao CInetista a pegar os dados de lá.

## Como surgiu o termo Data Lake

O grande avanço da IA ocorreu por 2 fatores:
+ 1. Paralelimso; Provido por GPU e algoritmos de processamento paralelo
+ 2. Big Data: Sermos capaz de gerar e guaradar uma enorma quantidade de dados, com alta variedade e alta velocidade.

O que é Big Data:
+ Um enorma volumes de daos, gerados a todo omeneto e das mais diversas forasm
+ Assim, nâo tem como fazer isso como um DW. O DW existe para dadso estruturados e para pdoer fazer análise

Data Lake:
+ Repositório dentro da empresa, para que todos os dados estejam disponíveis s aqualquer pessoa que precise afzer análise sobre eles

**Big Data x Data Lake: Data Lake é uma zona anárquica de dados, que sâo organizados asism que agente pega eles. Enquanto que DW é estruturado**

Entâo, tome cuisadao para que o DataLka enao vire um DataSwamp: **É necessário ter um estrutura e organizaçao para nao virar um DataSwamp**

Vamos criar 2 dataLakes
+ AWS e no Virtual Box

## Difernela entre Dlake e DW

img-c2-1-01

A grande diferença é a organizçao: no datalake aagente organiza apos pegar os dados do DataLake,

## DataLake vai substituir o DW

SIM E NAO

Nâo porque aiinda as pessao usam o DW.

Mas sim, porque o DataLake pode no futuro se tornar o unico repositorio da empresa

img-c2-1-02

## O que sâo dados corporativos

O tesouro das empresa sâo: dados e os colaboraladores.

Já há ipotese de comercializar dados na bolsa de valores.

Estima-se que 85% dos dados das empresa sâo descartardoas, uma grande perda de conheicmento que podem chegar em resultados.

Há um problema, consturir a infra certa é fundamental.

**Dados corporativos quando analisados, revelam grandes respostas**

Boa parte dos datalke hoje sao criadas por statapus, que podem criala d zero.

## Dados estruturados x NAO ESTRUTURADOS

estruturadas: sql, xml, csv
nao-erestrutudarso: pdf, txt, mp4, resddes/sociais

img-c2-1-03

## Infra em Nuvem e Local

Na pratica, só se usa cluster (master/slave)

É preferível na nuvem, porque voce paga o que usar, e nunca sabemos o quanto vamos conseguir de dados

## Logica do Data Lake

DataLake é um conceito:
+ A ideia é ter um hub central que concecta diversas fontes de dados
+ Uma emorpesa pode ter diversos tipso de BD

img-c2-1-04

Nao vamos criar esse tipo de 'logical data lake', com um hub central. 

Muitos empresas implementam um datalake como um mongoDB ou cassandra. Outros fazem isso ligando variso bancos distaitnso.
Nos faremso com o haddop que trabalha com clusers : fornce armazenmaneto e processamento distribuido

img-c2-1-05

## Apache Hadoop e Big Data Stack

**Haddop** 

+ Framework que permite trabalahra com armaeznamento e prcesasmento distribuid
+ Divido em 2: HDFS (sistema de arquviso distribuidos) e MapReduce
+ Nâo tem concorrente, é o melhor para processamento distribuido

HDFS
+ É a soluçâo, e uma das melhores para fazer DataLake

Map-Reduce
+ É o processamento dos nodos e vamos utilizar ele mais no capitulo 4 para fazer o processamento de todos esse daos


**Big data Stack**

Quais sâo os compoentne usadaoa para montar um bom e moderno big data. Vamos usar o segunte
img-c2-1-06 

Mas há outros

img-c2-1-07 e 8

## Dados em Batch e Streaming

Analogia com um lago
+ Barch: pegar agua do lago de baude
  - Traser os dados de tempo em tempos (cap4) apache scoop
+ Strminag: Mangueira/Torneira
  - Buscar os dados em tempo-real (cap5) apache flume

SAIBA QUE CARREGA REM BARCH É COMPLETMENTE DIFERENTE DE STREMING

##Custo de montar DataLake local

img-c2-1-09

Para ter um ROI, você tem que contar pelo menos 3 anos

## Custo para montar o datalek em cloud


