# Camada de Armazenamento de dados



## Links



## PARTE 1 - Teórica

### Conceito de Data Lake com Armazenamento de dados

Você pode se perguntar: Mas tudo que está no curso não se trata de armazenamento de dados, que é o termo 'engenharia de dados'. **NÃO**

O data lake é um conceito que engloba todo o workflow dos dados, e uma das etapas é o armazenamento.

Observe a figura a seguir:

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-01.png)

Perceba que DataLake não é sou um repositório, dele dá pra fazer diversas coisas 

Neste capítulo vamos estudar mais essa parte de armazenamento e ver as ferramentas Hbase (DW para HDFS) e Hive (NoSQL para HDFS)

**Temos que tomar uma decisão na hora de armazenar**
+ limpar ou não os dados, deixar ou não em raw, isso depende do seu objetivo final. 
+ Data Lake é uma ferramenta de negócio, não é apenas um repositório gigante pra depois vê se dá pra tirar alguma coisa disso.
+ Você tem que criar o data lake com algum objetivo de negócio.



### Contexto da camada de storage do Data Lake

Vamos focar agora na Data Storage Layer

Há 2 BD para usar: hive e Hbase

Data Ingestion Layer vamos ver em IA em Sistemas Distribuídos

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-02.png)



### Objetivo dessa camada

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-03.png)

Verifique o seu objetivo: pode ser que você não precise armazenar os dados, talvez apenas processar.

Ex: Análise de sentimentos em tempo real. Se tenho que salvar os dados ou não depende do objetivo, e por quanto tempo vou fazer isso.

Outros tecnologias para persistência

HDFS: Armazena Arquivos
+ Ele não é um Data Lake, é na verdade responsável pela persistência dos dados na camada de persistência

NoSQL
+ Ex: Cassandra

Banco Relacional
+ Ex: depois de estruturado



### O que é o apache Hadoop

O apache hadoop não foi feito para apenas uma única máquina. Se uma máquina da conta do recado, não precisa disso tudo, você pode usar um banco de dados NoSQL

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-04.png)



### Por Que usar HDFS para armazenamento

Vantagens
+ Ele foi feito para rodar em máquinas ruins e apenas uma boa que vai ser a master. Assim tem custo menor

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-05.png)





### Outras ferramentas

Podemos usar o HDFS como o sistema de armazenamento para o data lake. Além dele podemos até por outros.

**OS DADOS ESTÃO ARMAZENADOS NO HDFS**

NÃO HÁ FORMA DE FAZER CONSULTAR OU EDITAR OS DADOS NO HDFS, pois ele é o sistema de arquivo, como o sistema de pastas do windows/linux, NÃO DE FORMA SIMPLES, pois eu teria de fazer por MapReduce.

**Podemos usar o Hive e HBase para manipular os dados do HDFS**

HBase: Não estruturados

Hive: Estruturados e não estruturados

Ele vai ser como camada complementar.

Ao invés de entregar ao cientista de dados arquivo rcu do HDFS, eu posso entregar a interface do Hive que usa o SQL.

**O HDFS é bom para jogar as coisas lá. Agora para consultar manipular os dados do HDFS, eu uso Hive e Hbase**



## PARTE 2 - Usando HDFS



### Acessando e Brincando com o Cluster Hadoop HDFS

**SOMENTE AGORA VAMOS VER FORMALMENTE O HDFS HADOOP**

**Ativar cluster**

```
$HADDOP_HOME/sbin/start-hdfs.sh
$HADDOP_HOME/sbin/start-yarn.sh
```

**Acessar esse cluster da minha máquina local (fora do cluster)**

+ Faz o binário da versão 3.1.0 na sua máquina local
+ descompacta
+ Editar 'alguns arquivos de configurações na sua máquina local


AULA DE 15MIN

Aula de 15 min: escrita da minha máquina local

Multi Home Network: Podemos ter um ambiente hadoop conversando com outras redes



## PARTE 3 - Hive - DW em HDFS



### Apache Hive

Ele tem o comportamento como um DW mas com características diferentes.

Foi desenvolvido pela equipe do facebook, para fazer consultas SQL em um Cluster HDFS.

O HDFS é apenas um sistema de pastas, e com o Hive poderemos fazer o SQL.

**O HIVE SÓ MOSTRA SEU VALOR QUANDO EXECUTADO SOBRE UM CLUSTER HADOOP**

O hive não é pra substituir o seu DW, você usa ele para consultar o HDFS para dados estruturados e semiestruturados. Se não for estruturado, usamos HBase

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-07.png)



### Arquitetura do Hive

Usamos a linguagem HQL, Hive Query Language: ele converte a consulta em um job Map-Reduce e consulta diretamente um HDFS

AO invés de mandar uma instrução MapReduce, você vai usar o SQL comum, que facilita tudo

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-08.png)

**Componentes**

DAG: Directed Acyclic Graph, grafo acíclico direcionado. O hive cria um grafo de instruções

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-09.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-10.png)

**MetaStore**

É um banco de dados relacional que vai armazenar os metadados do HDFS



### Shell do Hive

Shell: interpretador

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-11.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-12.png)

Significado Ad-hoc: EM TEMPO REAL



### Instalar o Hive

O hive pode ser usado mesmo depois de armazenado os dados, Ele não transforma o HDFS num MySQL da vida, ele apenas faz as consultas nesse HDFS como SQL

Se atente com a versão, para ligar a sua versão do hadoop

1. instalar mysql, pois vamos usá-lo para o meta-store use o arquivo 'hive-squema' e a versão do seu hive. Vamos criar um DB a para o hive no mysql executado o script já pronto

2. source /opt/....../hive-schema......sql

criamos hive-site.xml e aí , configuramos as propriedade

3. O hive só vai funcionar se o HDFS estiver sendo, inicializado



### Usando

```
$ hive
$ > create table datalke(id int, nome string);
```

Aí, os dados vão ser criados  no mysql no db meta-store

```
mysql > use metastore
mysql> select * FROM TBLS
```

O hive e permite fazer consultas, agora para fazer operações matemáticas MapReduce/Spark

**AGENTE CRIA UMA TABELA NO HIVE PARA LER OS DADOS QUE JÁ ESTÃO NO HDFS**

Vai criar uma forma de ler como SQL os dado do hdfs delimitados por ;

````
create external table tb_teste (
  id int,
  nome string
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ';'
location '/tmp/teste';
````




## PARTE 4 - HBASE - NoSQL em HDFS



### Apache HBase

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-20.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-21.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-22.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-23.png)

Ele permite leitura/gravação de coisas aleatórias que não é possível pelo hadoop. O HDFS não oferece uma interface para consultar os dados em TeraBytes 

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-25.png)

A leitura é sobre o Hbase (o Hbase serve como interface), mas às escrita pode ser sobre o Hbase ou diretamente no HDFS.

Há duas formas de gravar no hbase/hdfs, mas dependendo do seus dados, pode ser mais fácil gravar direto no hdfs do que no hbase

**Arquitetura**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-8-26.png)



### Instalando Hbase

O hdfs foi feito para por os dados, mas agora, para manipular e consultar, é necessário outras ferramentas.

De forma estruturada, usamos o Hive. E de forma não-estruturada usamos o Hbase.

**N O É TODO CASO QUE VAI CABER O HBASE PARA DADOS NÃO ESTRUTURADOS**

Lembrando que o Hbase é NoSQL

**Definição**Use Apache HBase™ when you need random, realtime read/write access to your Big Data. This project's goal is the hosting of very large tables -- billions of rows X millions of columns -- atop clusters of commodity hardware.

Instalação da mesma forma de sempre

Vamos colocar o Hbase para todos os nodes do nosso cluster



### Inicializando Hbase

Inicializando hadoop/yarn primeiros

Na aula 4, ele resolveu um troubleshooting bem difícil em 4 min. A equipe no hbase esqueceu um arquivo, : colocaram o arquivo numa pasta diferente da que deveria



### Shell Hbase e testando

Podemos usar em shell ou API Java

```
$ hbase shell

$ Criar tabela
$ crate 'cdr', 'index', 'customer', 'type', 'timing', 'usage', 'correspondent', 'network'
```

INSERIR

```
$ put 'crd', '010', 'index:customercount', '2'
```

VER DADOS

```
scan 'cdr'
```

**VAMOS VER MAIS DO HBASE NO CURSO DE ML in SD**

Há poucos comandos na base. Ele serve para No SQL e para consultar o big data, ano é um sql completo.




