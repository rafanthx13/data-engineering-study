# Data Lake - Camada de Mensagens - Kafka, ZooKeeper, StreamSets

ESTA SEÇÃO SERVE COMO UM CURSO DE APACHE KAFKA, POIS NÃO HÁ NADA EM PORTUGUES

## Objetivo de data lake

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-01.png)

Ele é muito mais que um repositório para armazenar dados. É uma plataforma para tratar dados estruturados ou não, em batch ou streaming.

Não temos que obrigatoriamente armazenar. Podemos pegar com flume, processar com spark e armazenar só o resultado.

**Você pode tratar, criar diferente pipeline, em tempo real ou não e fazendo tudo isso sem armazenar fisicamente os dados**

**ESTAMOS MIGRANDO DE BIG DATA PARA FASTA DATA. É TANTO DADO QUE ESTAMOS PROCESSANDO ELES EM REAL-TIME E ARMAZENANDO SÓ O QUE IMPORTA, O RESULTADO**

**OBJETIVO**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-02.png)

Ao invés de armazenar, vamos processar em tempo real.

Usaremos a principal ferramenta: APACHE KAFKA.

Ele é mais complexo e de altíssimo nível. Ele age como um middleware

O Kafka é para o processamento de dados em tempo real. Se você não tem isso, da pra reduzir a complexidade do Data Lake pela metade

**Divisão do curso**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-03.png)

## PARTE 1 - Camada de mensagem

Arquitetura do nosso data lake

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-04.png)

Pode ter uma ou mais funções. As 10 funções principais da camada de mensagem são a seguir (não é obrigatório para todo projeto).

A camada de mensagem serve como middleware, ela liga o subscribe do consumer com o listen dos dados em tempo-real

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-05.png)

a camada de mensagem é o 'colletor tier'

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-06.png)

**Serve para juntar a coleta de dados para um único ponto, e de um único ponto disponibilizar para n consumer**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-08.png)

**Ele é o homem do meio entre a coleta de dados e consumir os dados, para mandar para n destinos**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-09.png)

Ele funciona como um broker, no modelo listen/subscribe e há controle de fila. 

**Ela vai centralizar N fontes e disponibilizar para M consumidores**

O Kafka não é a ferramenta para todos os problema,s só porque ele é fodão

### Funções da camada de mensagem

** F1**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-f01.png)

Você dissocia fonte do destino. Isso serve como uma espécie de interface em Java. Onde um lado não precisa se preocupar com quem será do outro lado, pois cabe ao objeto do meio fazer essa integração. 

Assim, se um das partes mudar, a mudança pode ser feito somente neste middleware

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-f02.png)

Garante que seja entregue em ordem

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-f03.png)

### O que é Apache Kafka

Linkedin, Uber, airbnb, netflix, todas elas usam Kfka para BIg data

Definição do que é o kafka

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-10.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-11.png)

Ele é um centralizador e um dispensador, além de ser capaz de fazer ETL.

**Lembre, quase qualquer coisa pode executar ETL, mas nem todos da mesma forma que o Pentaho**

**Origem do Apache Kafka**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-15.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-12.png)

### Arquitetura de Mensagem / Kafka

A definição mais simples: serviço de mensagem que manda dados de uma lado ao outro.

Ele trabalha com a arquitetura de producers (publica info) e consumers (assinar serviço).

É criado o conceito de tópico, que é nele que o consumer assinar e é nele que o producer envia. É como uma caixa de email

Isso é feito a partir do broker, que é uma uma caixa de correio

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-20.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-21.png)
### Cluster Kafka

Vamos colocar várias kafka como se fosse uma.

Não vamos criar um Cluster Kafka pois precisa realmente disso para processar terabytes por segundo

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-22.png)
Podemos por brokers em máquinas diferentes, um cluster de kafka.

**O KAFKA NÃO TEM UM SISTEMA DE GERENCIAMENTO DE CLUSTER, QUEM VAI FAZER ISSO É O ZOO-KEEPER**

**Informação de utilização do kafka**

### APache Zookeeper

O que são sistema distribuídos/cluster

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-24.png)
Exemplos de sistema distribuídos

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-25.png)
**Pra que serve o zookeeper**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-26.png)
O zookeeper vai gerenciar os brokers e os casos em que ele forem compartilhados entre os nodes do cluster

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-23.png)
### Instalar apache Kafka

mesmo processo, wget, move e descompacta,  em seguida, configurar variáveis de ambiente

**O KAFKA JÁ VEM COM ZOOKEEPER** 

Há 3 arquivos de configurações do kafka

consumer.proprietis, zookeeper.proprietis, producers.proprietis

## PARTE 2 - Componentes do Kafka

Esse conhecimento é importante para montar uma arquitetura de micro-service

### Apache Kafka - TOPICS

O kafka é como uma caixa de correio: alguém deposita mensagem lá e outra pessoa em outra hora vai lá e consome.

O 'tópico' é a abstração central do Kafka.

**O TÓPICO É COMO UMA CATEGORIA DE MENSAGE**

É uma entidade lógica, representada por um arquivo de log

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-30.png)
Podemos ter um mesmo tópico entre vários brokers, um cluster kafka

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-31.png)
A concessão é feita a um tópico e não a uma máquina, assim, cabe num Sistema Distribuído

**O que tem no tópico**

O tópico fica organizado sequencialmente no tópico.. O tópico tem um conjunto de mensagens recebidas de um producer

### Apache Kafka - MESSAGE

O que tem dentro de cada mensagem do kafka

+ timeStamp : controle de tempo
+ id : identificador
+ Payload : dados sem si

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-32.png)

**Como o kafka sabe que uma mensagem já foi consumida pelo consumer**

Através do **Offset**: um espaço reservado, placeholder, guarda a posição da última mensagem lida. É mantida pelo Kafka COnsumer

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-33.png)
O consumidor consome aquela mensagem, e marca aquela mensagem nesse offset. Assim ele tem o controle ao voltar e ler a mensagem: ele pode ler de várias maneiras (ler todas a partir do offset, ler as anteriores também ao offset e outros, tudo isso é configurado)

### Apache Kafka - Políticas

**Por quanto tempo ficam as mensagens no Kafkf**

O produtor gera mensagens, mas o consumer não precisa ocorrer ao mesmo tempo.

**O PROCESSO É ASSÍNCRONO**

Como não preciso ter os dois acessando ao mesmo tempo, eu preciso de uma política de retenção. POis nao posso guardar eternamente

**Política de retenção**
+ O kafka retém todas as mensagens publicadas independente do consumo por um tempo que é 168 horas, ou seja, 7 dias. Isso é o suficiente para processar dados em tempo real.
+ Cada tópico pode ter uma retenção diferente
+ Lembre-se de considerar o espaço em disco ao definir a política de retenção. Depois do período, as mensagens são excluídas


## PARTE 3  - Usando Kafka e ZooKeeper na Prática

### Kafka cluster

Vamos criar uma kafka cluster independente de data lake
1. Configurar Kafka Cluster
2. Inicializar Broker
3. Produzir e consumir mensagens de um tópico
4. Por fim, ver essa mensagem no kafka

*Lembres, agente nao vai criar um cluster kafka, então porque tem esse nome no título*

Porque a ideia do kafka sempre foi trabalhar com Sistema Distribuído, então ele foi feito para cluster, para haver vários brokers. Mas vamos só usar um único cluster que ainda assim recebe a terminologia de cluster kafka (pois estamos testando/laboratoria)

Vamos usar SOMENTE O MasterNode

Abra 4 terminais na máquina local que usam putty na ec2 MASTER

Zookeeper fica na porta 2181

Usamos telnet para ver se o zookeeper está online

### Cluster com Zookeeper : a forma de operar o kafka

O kafka funciona no zookeeper. ponto.

o zookeeper gerencia cluster (n máquinas trabalhando juntas). ponto

Mesmo que você tenha uma única máquina, você ainda assim referência ao zookeeper, então comandos de listar/criar/deletar tópicos consiste em mandar esses comandos ao zookeeper e ele fazer as coisa no cluster kafka de 1 ou n máquinas.

### O que soa commit logs

São uma fonte confiante de dados, como se fosse transações bem registradas, não só de insert mas também de alter do SQL

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-37.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-38.png)
O Kafka é como se fosse um commit log salvo, e acessado pelos consumers

### Concluindo Lab 4
(5 min da ultima aula do lab 4)

Analogia que eu fiz do kafka:
uma thread manda dados,
outra thread mantém os dados
outra thread retira os dados
Os dados são ordenados pela 2 thread.

É o middleware, o nome do meio. N produtores produzem mensagens para M tópicos e 1 ou mais tópicos podem ser consumidos por Q consumidores

## PARTE 4 - Lab - Desenvolver um Kafka producer em Java

A Partir da IDE INTELLIJ usando Maven, cria uma classe Java que vai conectar a EC2 que está rodando o kafka e assim produz 1000 mensagem de forma randômica

## PARTE 5 - Lab - Configurando Multi-Cluster Kafka Cluster

ANtes tínhamos 1 único broker, agora vamos fazer mais de um broker

abrir 7 terminais na mesma  máquina
1 - zookeeper
3- 3 broker
1- produce
1- consumer
1 -teste random

O que faço
+ 3 brokers em portas diferente (faço isso modificando arquivos fisicamente) criava vários server-0.proprieties

Houve um erro ao subir multi-broker, e isso aconteceu porque cada broker tem que ter um diretório de logs diferentes

## PARTE 6 - StreamSets

### Introdução

até aqui estudamos o Apache Kafka, agora vamos integrar o Kafka ao nosso data lake.

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-40.png)
**Porque vamos usar o Kafka**

**IMPORTANTE**: Tanto Flume quanto NiFi precisavam do zookeeper? **NÃO**

Eles são ferramentas não-distribuidoras, cada um é feito em uma única máquina.

Então, como vamos salvar os dados sem salvá-los no Data Lake? Através do kafka.

Lambe-re, o Kafka não é o HDFS mas ele vai manter os dados seguros antes de chegar lá. Isso por que **ESTAMOS NUM AMBIENTE EM QUE É DISTRIBUÍDO E ASSÍNCRONO, VAMOS MANTER OS DADOS ATÉ QUE ALGUÉM VÁ LÁ, CONSUMA O BROKER E ASSIM SALVE NO HDFS**

A ideia é: manter os dados como mensagem por 7 dias, e depois, aí sim, processar e talvez guardar no HDFS

Propósito das ferramentas
+ Flume: Coleta de Streaming
+ Kafka: Manter uma camada de mensagens, de persistência dos dados, de modo que, se algum node falhar eu consigo garantir a entrega dos dados
+ Nifi: Ferramenta de ETL

### STREAM-SETS

Uma nova ferramenta. com 100%de certeza, vai incluir o Stream Set nas suas ferramentas preferidas

Criado em 2014 por um engenheiro da cloudera. **GRATUITO**. Foi criado para operadores de DataOps entre sistemas heterogêneos

**DRAG-AND-DROP VIA BROWSER**

HÁ DASHBOARD TOTALMENTE PRONTOS COM ESTATÍSTICAS DE DADOS, UTILIZAÇÃO DE MEMÓRIA E TUDO O MAIS. 

### Dois Pipeline usando StreamSets

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-42.png)
Vamos fazer 2 pipeline
1. De IOT , Streaming
2. de RDMS, cada  nova row vai gerar um stream

No curso de ML e SD vamos reproduzir isso e no final vamos aplicar ML

### Instalando e usando Stream Sets

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-44.png)
### Criando os pipeline no Stream Sets

Criamos 2 pipelines, um para mandar do producer ao kafka (producer)

E outro para consumir, do consumier para o Hadoop HDFS

Não colocamos tudo junto porque se dar erro para tudo, e tanto o processo do consumer quanto que o producer SÃO E DEVEM SER INDEPENDENTES

DÁ PRA FAZER ALGUMAS COISA COMO O PENTAHO no Stream Sets

Da aula 23 em diante, é o pipeline 2 pegando do banco relacional

Agente instala o MysQL na máquina Master e a gente criar a tabela em conolse
s
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-7-47.png)


