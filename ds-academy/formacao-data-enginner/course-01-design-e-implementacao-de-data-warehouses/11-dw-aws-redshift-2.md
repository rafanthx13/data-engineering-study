# Criando DW usando AWS RedShift - parte 2

## O que veremos

+ CRUD an AWS
+ Diversas configurações para fazer isso

## Objetivo desse projeto

	Neste segundo projeto de implementação de um Data Warehouse,
trabalharemos com o ambiente em nuvem da Amazon e com o serviço Amazon
Redshift.
	
	Vamos implementar um cluster com 3 nós, sendo um líder e dois compute
nodes. Nosso cluster terá apenas um banco de dados.

	Criaremos as tabelas FATO e DIMENSÃO e iremos carregar apenas algumas
tabelas, dando ênfase às configurações do Amazon Redshift.

	Os scripts usados no projeto estão em anexo no canto superior direito do
seu vídeo e serão usados nas próximas aulas.

## O BD na RedShift

Bancos de Dados no Cluster Amazon Redshift


	O Amazon Redshift cria um banco de dados quando você provisiona um
cluster. Este é o banco de dados que você usa para carregar dados e executar
consultas em seus dados. Você pode criar bancos de dados adicionais executando
um comando SQL, conforme necessário. O limite é de até 60 bancos de dados por
cluster.

	Quando você provisiona um cluster, especifica um usuário principal que tem
acesso a todos os bancos de dados criados no cluster. Este usuário principal é um
superusuário que é, inicialmente, o único usuário com acesso ao banco de dados,
embora esse usuário possa criar outros superusuários e usuários.

	O Amazon Redshift usa parameter groups para definir o comportamento de
todos os bancos de dados em um cluster, tais como estilo de apresentação de
data e a precisão de ponto flutuante. Se você não especificar um parameter group
ao provisionar seu cluster, o Amazon Redshift associará um parameter group
padrão ao cluster.

Usa o seguinte SQL:
https://docs.aws.amazon.com/pt_br/redshift/latest/dg/cm_chap_SQLCommandRef.html

## Diferença entre tipos de RedShift

Dense Compute x Storage Compute


	Um cluster do Amazon Redshift consiste em nós. Cada cluster tem um nó
de liderança e um ou mais nós de computação. O nó de liderança recebe
consultas de aplicativos cliente, analisa as consultas e desenvolve planos de
execução de consulta. Em seguida, o nó principal coordena a execução paralela
desses planos com os nós de computação e agrega os resultados intermediários
desses nós. Então, ele retorna os resultados de volta para os aplicativos cliente.

	Nós de computação executam planos de execução de consultas e
transmitem dados entre si para atender essas consultas. Os resultados
intermediários são enviados ao nó de liderança para agregação antes de serem
enviados novamente para os aplicativos clientes.

	Quando você executa um cluster, uma opção que você especifica é o tipo
de nó. O tipo de nó determina a CPU, RAM, capacidade de armazenamento e o
tipo de unidade de armazenamento de cada nó. Os nós do tipo armazenamento
denso (DS) são otimizados para armazenamento. Os nós do tipo computação
densa (DC) são otimizados para computação.

	Você pode criar um cluster usando tipos de nós de armazenamento denso
(DS) ou computação densa (DC). Os tipos de nós de armazenamento denso
permitem criar data warehouses muito grandes usando discos rígidos (HDDs) por
um preço bastante reduzido. Os tipos de nós de computação densa permitem
criar data warehouses de altíssimo desempenho usando CPUs rápidas, grandes
quantidades de RAM e discos de estado sólido (SSDs).

	Os nós do tipo DS2 são otimizados para grandes cargas de trabalho de
dados e usam armazenamento com base em unidade de disco rígido (HDD).

	Os nós DC1 e DC2 são otimizados para cargas de trabalho de desempenho
intensivo. Como eles usam armazenamento de disco de estado sólido (SSD), os
tipos de nó DC1 e DC2 fornecem uma E/S muito mais rápida em comparação aos
nós do tipo DS, mas fornecem menos espaço de armazenamento.

	Você executa clusters que usam os tipos de nó DC2 em uma nuvem privada
virtual (VPC). Você não pode executar clusters DC2 no modo EC2 clássico.

	O tipo de nó escolhido depende intensamente de três informações:

	• A quantidade de dados que você importa para o Amazon Redshift
	• A complexidade das consultas e operações que você executa no banco de
	  dados
	• As necessidades de sistemas downstream que dependem dos resultados
	  dessas consultas e operações

	Os tipos de nó estão disponíveis em diferentes tamanhos. Os nós DS2 estão
disponíveis nos tamanhos xlarge e 8xlarge. Os nós DC2 estão disponíveis nos
tamanhos large e 8xlarge. O tamanho do nó e o número de nós determinam o
armazenamento total de um cluster.

	Alguns tipos de nó permitem um nó (single-node) ou dois ou mais nós (multinode).
A quantidade mínima para clusters 8xlarge são dois nós. Em um cluster de
single-node, o nó é compartilhado para a funcionalidade principal e de
computação. Em um cluster de multi-node, o nó de liderança é separado dos nós
de computação.

	O Amazon Redshift aplica cotas aos recursos para cada conta da AWS em cada
região. Uma cota restringe o número de recursos que sua conta pode criar para
determinados tipos de recursos, como nós ou Snapshots, em uma região.

## Sigilo

jdbc:redshift://rhavel-redshift-cluster-1.cpyuyvrzuwic.us-east-1.redshift.amazonaws.com:5439/dev
rhavel
royal-Thunder_-_re8

## Criando estrutura do DW

Arquivo create_awsdw.sql

Há 3 estilos de DW para cada tabela: EVEN, KEY, ALL.

Eles são especificados na chamada do "CREATE" DELAS

### Tipo even

Bsata não especificar , é o tipo default

### Tipo key

````
CREATE TABLE DimProduct
    (
      ProductKey INT NOT NULL sortkey distkey,
````
### Tipo all

````
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
````
estilo de distribuiçao onde os dados da tabela são carregado para todos os nodes (slaves). 

Faemzo isso com a dimensão data porque ela nao vai mudar durante o tempo,

Esse estilo para dimensâo data tem a seguinte vantagem : os dados estarao em todos os alves, assim, as consultas a data ficaraâo mais rápidas

vantagem pois a data, que sâo poucas e nao vai mudar estarâo já distribuidos em todos os computes nodes, isso significa que nao vai precisa redistribuir os dados relacionadoa a data.

Usamos o estilo ALL DISTRIBUTION pois os dados muda com pouquissima frequencia.

**OBSERVAÇÕES DO TUTOR**
Tanto Fato como as Dimenoes esatao quase tudo como tipo key, ou seja, com `distkey`

LEMBRES: VOCE TEM QUE FAZER COMMIT tanto em DDL quno no SQL de consulta, clique no commit no topo do SQLWorkBenchJ

## Fazer a carga diretamente do S3 AWS

S3 (Simple Storage Service)

criei bucket red-shift-bucket, com acesos privado

O S3 é praticamente um google drive, onde pode-se até mesmo por site/coisas estáticas

## Fazer a carga do DW-Redshift buscando a Carga do S3

Usamos uma sintaxe do postgre para fazer esse copy de dados

``````
copy dimproduct
from '' 
iam_role '' 
region ''
delimiter ','
``````

Onde:
+ copy:  especifica qual tabela vai receber os dados
+ from: vai especificar o loca, no caso, o s3
+ iam_role: tem que configurar uma role no clsuter para esse serviço AWS poder ler o S3
+ region: cada regiao tem um codigo, no caso é us-east-1
+ delimiter: separador do arquivo, no caos, vai ser ','

### Configuraando IAM ROLE

O role em portugues é funçâo .

**como criar**
+ Busque por IAM no console AWS
+ Busque criar uma role/função (role foi traduzido para 'funçâo' em portugues)
+ Busqeu criar para o produto S3 e selecione o READoNLEY
+ Aṕos criado, busque o ARN da role, no meu caso foi
arn:aws:iam::459886294046:role/aws-dw-redshift-read-s3

Agora terei o comando completo
``````
copy dimproduct
from 's3://red-shift-bucket-rhavel/dimproduct.csv' 
iam_role 'arn:aws:iam::459886294046:role/aws-dw-redshift-read-s3' 
region 'us-east-1'
delimiter ','
``````
nao vai dar certo como sempre. Vá no clsuter e configura essas coisa de IAm no cluster

infeisemten esse IAM role nao consegui colcoar l, entao, vou fazer por uotro que se conecta ao s3

``````
copy dimproduct
from 's3://red-shift-bucket-rhavel/dimproduct.csv' 
iam_role 'arn:aws:iam::459886294046:role/service-role/AmazonRedshift-CommandsAccessRole-20211118T032058' 
region 'us-east-1'
delimiter ','
``````
## Processar de forma palarela a carga

1. Subo 4 arquivos zip
2. Subo o manifest que especifica esse 4 arquvios zip
3. EXECUTO O COMANDO ABAIXO PARA EPEGAR E PROCESSAR ESSES 4
``````
copy factsales
from  's3://red-shift-bucket-rhavel/manifest.txt'
iam_role 'arn:aws:iam::459886294046:role/service-role/AmazonRedshift-CommandsAccessRole-20211118T032058' 
region 'us-east-1'
delimiter '|'
GZIP
manifest
``````
OBS: TEM QUE MUDAR O MANIFEST.TXT PARA O 'S3' APONTAR par ao nosos s3

## Carregar arquivo JSIN de data
``````
copy dimdate
from 's3://red-shift-bucket-rhavel/dimdate.json'
iam_role 'arn:aws:iam::459886294046:role/service-role/AmazonRedshift-CommandsAccessRole-20211118T032058' 
region 'us-east-1'
json as 'auto'
``````
## Conectar pelo PowerBI

Server: endpoint

Busque por redshfit

Vai pedir server: o server é o endpoins sem o '/dev' final, que especificia o banco de dados, .

Ou seja, o que voce colocar no server é a a string cujo final é o numero da paorta soemtne

escolhga as tabelas e clique load/carregar.

Ele vai elaborar e chamar a query com eses dados

## Como fazer ETL para AWS

O ETL É FEITO POR LINGUAGEM DE PROGRAMAÇA. É ASIM QUE MUITAS EMPRESAS ESTAO CRIANDO SOLUÕES PARA AWS CRAIANDO PROGRAMSA. ENTAO, VOCE MESMO PODE CRIAR A SOLUÇAO DE FAZER ETL para AWS usando linagunes de programaçao

OBS: Faltou as últimas aulas
