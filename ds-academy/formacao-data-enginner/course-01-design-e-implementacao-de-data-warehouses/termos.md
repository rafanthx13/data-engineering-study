

Data WareHouse - DW: Reuniao de varios dados de diversos bancos de dados transacionais e agerga tudo o que é improtante em um unico só lugar. É uma centralizçao consolidada de informaççoes extrememente relatiavas a ativdade da empresa.


Data Mart:
+ Uma especie de mini DW, masi especifico para organizar

Big Data: Um enorme volume de dados. E isso é possivel por meio da internt

BI (Business Inteliggence): O DW é a matéria prima  principal para o BI. Está muito relacionado ao SW

OLTP (Online Transactional Processing): 
+ Suma: É o modelo de banco de dados entidade-relacionametno. É o oposto ao OLAP que usa dimensao-fato
+ Bancos de dados que registram várias informações que armazena diversas transaçôes durante o dia. Entâo, é apenas registrar cada transaçâo, criando assim dados.
+ É um bnaco para operaçôes do dia a dia

OLAP (Online Analytics Processing):
+ SUma: DImensao-fato
_ Usado spara plcaiaçoes analticias, é o modelo de um DW, que é difenrete dos bancos de dados comuns que agente aprende

ETL (Extract, Tranformation, Load):
+ É um conceito, basiamcnete é pegar os dados e mandar par aoutro lguar fazendo ou nao alguma alteraçao
+ pOde se usar desde Bash até coisas complexasa para fazer isso

Surrogate Key: A Surrogate Key é uma chave artificial e auto incremental.
+ A palavra artificial vem do tipo, porque ela não existe em lugar nenhum, não está lá no transacional como a Natural Key, ela é criada no Data Warehouse.
+ E é auto incremental porque toda vez que é chamada, troca de número, então ela começa com 1 e vai indo para 2, 3, 4, e assim por diante.
+ Resumindo: ela é a famosa sequence do banco de dados ou a sequência no Excel.
+ Uma Surrogate Key nada mais é que um campo com as características de uma Primary Key, e é gerada automaticamente na hora da carga, quando você carrega a dimensão no ETL.
+  Surrogate Key : é utilizada para referenciar a dimensão na fato; é auto incremental; é uma chave artificial; é criada no Data Warehouse; não pode se repetir
