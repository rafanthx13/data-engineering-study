# Termos de Engenharia de Dados

## DB/BI Termos

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

## Bussines Terms

RollOut:
+ Quando você cria um ambiente e depois passa o ambiente para a equipe de suporte

=============================================

## Ambiente Hadoop

### HDFS

É como o sistem de arquivos/pasta do linux/window, mas para sistemas distribuidos.

Exemplo: Se voce joga um arquivo no HDFS, ele vai duplica para outros nós aquele arquivo. Se um dele flha, há outro. O HDFS cuida de tudo isso, de cria rum cluster dde arquivos. Ou seja, voce vai usar várias maquina apra armazenar os arquivos e para vocÊ, vai parecer que é tudo uma máquina só.

### MapReduce

Módulo do Haddop para processar dados. Ele usa Storage, entao é ideal para processar muitíssimo dados

### ZooKeeper

App que gerencia aplicaçôes apache entre os vários nós do haddop

### Apache Spark

Ferramentas de procesasmetno de dados em ambinete distribuidos para dados em streaming.

É melhor que o MapReduce em alguns casos, pois usa memória, e por isso mais rápido.

Ferramenta ideal para fazer cálculos e ML sobre streming.s

### Apache Sqoop

Buscar dados estrutudaso, de batch

### Apache FLume

Buscar dados de Streaming. Tipo ETL

### StreamSets

Serve como uma UI do pentahoo para lidar com as aplicaçêos Haddop. Um Dragp and Drop que facilitar usar o kafka, por exemplo.

Nâo tem o selo apache, mas é muito poderosa e facilita tud, como o pentaho.

### Apache NiFi

Apache NiagraFalls. Faz ETL de treminag de dados como Apache Flume, mas, faz via interface (parecido com pentaho, mas via web, ou seja, abre uma porta 8080 e lá vocÊ faz drag and drop)

### Apache Kafka

É a camada de mensagem. É ums erviço complexo. Ideal para usar em conjunto com dados Stremaing.

Serve como uma caamda intermediária entre a aquisiçâo dos dados e sua persistencia/prcessamento. Usa o sistema Producer => Broker => Consumer para trabalhar com mensagesn.
+ O producer envia dados para o kafka, no formato de mensagem
+ No kafka, cada mensagem fica num broker
+ No broker fica aas mensagem por umcerto tempo, e lá as maensagens são mantidas e ordenadas
+ Um consumer faz a asisnatura de um broker
+ se há algo nesse broker, o consumer recebe em ordem.
+ No broker, a mensagem não é deletada, pois pode ser que outro consumer prceise daquilo.

Objetivo principal: ligar N produtores com N consumidores que podem ser tanto para processar os dados quanto para persistilos

### Apache Ambari

Ferramenta de Hadoop Management. Permite vocÊ monitorar todo o cluster haddop, cada um dos nós e as aplicaçôes rodando dele.

**O que faz**
+ Permite fazer deploy de n nós haddop ao mesmo tempo via interface (evita usar linha de comando) tendo que conigurar apenas ssh sem senha
+ Permite monitorar não só o haddop, mas tudo que está rodando nele (hbase, hive, sqccop, kafka e etcc)

**Quando uso**
+ Monitorar sistema hadop
+ fazer deply mais rápido sem usar linha de comando

### Apache Hbase

Banco de dados NoSQL que roda sobre o HDFS. Semelhante ao Hive, mas par anao-estruturados.

### Apache Hive

Banco de dados Estrutural do HDFS. Ele roda sobre o HDFS.

O HSFS é um sistema de arquivo, mas nâo é bom para consultar as coisas. Fazer consulta e algumas manipulaçôes ´e algo que o SQL faz bem.

O que o Hive faz. Com ele voce pode criar tabelas que abstraem os arquivo estrutudaos do HDFS e asism fazer consultas SQL (NO caso chamads de HiveQL)


=============================================

## AWS EcoSystem

### AWS EC2

EC2 é uma máquina que fica ligada 24horas, sem ui/interface GUI

### AWS S3

Simple Storage Service (S3): É um repositório tipo o git, que dá pra por qualquer coisa nele

### AWS RedShift

Banco de Dados para DW. Não é apenas um banco Postgre, ele foi otimizado para consultas de DataWarehouse

### AWS RDS

É o banco de dados relacional do AWS. Émontar lá um MySQL, ou Postgre da vida.

