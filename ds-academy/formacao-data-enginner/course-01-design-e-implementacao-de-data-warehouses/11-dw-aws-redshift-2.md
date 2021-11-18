# aula 2

jdbc:redshift://rhavel-redshift-cluster-1.cpyuyvrzuwic.us-east-1.redshift.amazonaws.com:5439/dev
rhavel
royal-Thunder_-_re8
## Criando estrutura do gw

Arquivo create_awsdw.sql

### tipo key

CREATE TABLE DimProduct
    (
      ProductKey INT NOT NULL sortkey distkey,

### Tipo all

CREATE TABLE DimDate
    (
      datekey INT NOT NULL ,
      alternatedatekey DATE NOT NULL sortkey,
      dayofweek INT NOT NULL ,
      dayofmonth INT NOT NULL ,
      weekofyear INT NOT NULL ,
      monthofyear INT NOT NULL ,
      quarter INT NOT NULL ,
      CONSTRAINT PK_DimDate_DateKey PRIMARY KEY ( DateKey )
    ) DISTSTYLE ALL;

estilo de distribuiçao carregado para todos os nodes. 

Faemzo isso com data porque ela nao vai mudar durante o tempo,

Isso da vantagem pois a data, que sâo poucas e nao vai mudar estarâo já distribuidos em todos os computes nodes, isso significa que nao vai precisa redistribuir os dados relacionadoa a data.

Usamos o ALL DISTRIBUTION pois os dados muda com pouquissima frequencia.

Tanti Fato como as Dimenoes esatao quase tudo como tipo key.

LEMBRES: VOCE TEM QUE FAZER COMMIT tanto em DDL quno no SQL de consulta, clique no commit no topo do SQLWorkBenchJ


## Fazer a carga diretamente do S3 AWS

S3 (Simple Storage Service)

criei bucket red-shift-bucket, com acesos privadpo

## Fazer a crarga do S3

Usamos uma sintaxe do postgre para fazer esse copy de dados

``````
copy dimproduct
from '' 
iam_role '' 
region ''
delimiter ','
``````

Onde:
copy: especifica qual tabela vai receber os dados
from '' 
iam_role '' 
region ''
delimiter ','

### Configuraando IAM ROLE

O role em portugues é funçâo .

**como criar**
+ Busque por IAM no console AWS
+ Buscque criar uma role/função
+ Busqeu criar para o produto S3 e selecione o READoNLEY
+ Aṕos criado, busque o ARN da role, no meu caso foi
arn:aws:iam::459886294046:role/aws-dw-redshift-read-s3

Agora terei o comando completo

copy dimproduct
from 's3://red-shift-bucket-rhavel/dimproduct.csv' 
iam_role 'arn:aws:iam::459886294046:role/aws-dw-redshift-read-s3' 
region 'us-east-1'
delimiter ','

nao vai dar certo como sempre. Vá no clsuter e configura essas coisa de IAm no cluster

infeisemten esse IAM role nao consegui colcoar l, entao, vou fazer por uotro que se conecta ao s3


copy dimproduct
from 's3://red-shift-bucket-rhavel/dimproduct.csv' 
iam_role 'arn:aws:iam::459886294046:role/service-role/AmazonRedshift-CommandsAccessRole-20211118T032058' 
region 'us-east-1'
delimiter ','

## Processar de forma palarela a carga

1. Subo 4 arquivos zip
2. Subo o manifest que especifica esse 4 arquvios zip
3. EXECUTO O COMANDO ABAIXO PARA EPEGAR E PROCESSAR ESSES 4

copy factsales
from  's3://red-shift-bucket-rhavel/manifest.txt'
iam_role 'arn:aws:iam::459886294046:role/service-role/AmazonRedshift-CommandsAccessRole-20211118T032058' 
region 'us-east-1'
delimiter '|'
GZIP
manifest

OBS: TEM QUE MUDAR O MANIFEST.TXT PARA O 'S3' APONTAR par ao nosos s3

## Carregar arquivo JSIN de data

copy dimdate
from 's3://red-shift-bucket-rhavel/dimdate.json'
iam_role 'arn:aws:iam::459886294046:role/service-role/AmazonRedshift-CommandsAccessRole-20211118T032058' 
region 'us-east-1'
json as 'auto'

## Conectar pelo PowerBI

Server: endpoint

Busque por redshfit

Vai pedri server: o server é o endpoins sem o '/dev' final, que especiificia o banco de dados, .

Ou seja, o que voce poe no server é a a string cujo final é o umero da paorta soemtne

escolhga as tabelas e clique load/carregar.

Ele vai elaborar e chamar a query com eses dados

## Leia a aula de ETL

O ETL É FEITO POR LNGUAGEM DE PROGRAMAÇA. É ASIM QUE MUITAS EMPRESAS ESTAO CRIANDO SOLUÕES PARA AWS CRAIANDO PROGRAMSA. ENTAO, VOCE MESMO PODE CRIAR A SOLUÇAO DE FAZER ETL para AWS usando linagunes de programaçao
