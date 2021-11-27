#

ESTA SEÇaÔ SERVE COMO UM CURSO DE APACHE KFKA, POIS NAO HÁ NADA EM PORTUGUES

## Objetivo de datalkae

img-c2-7-01

ELe é muito mais que um repositório para armazenar dados. É uma plataforma para tratar dadaos estruturados ou nao, em batch ou stremiang.

Nao temos que obrigatoriamente armzanear. Podemos pegar com flume, processar com spark e aramzenar só o resultado.

**VOce pode tratar, criar diferente paiplein, em tempo rela ou nao e fazendo udo isos sem aramaenzar fisicamente os dados**

**ESTAMOS MIGRANDO DE BIG DATA PARA FASTA DATA. É TANTO DADO QUE ESTMAOS PROCESSANDO ELES EM REAL-TIME E ARMAZENANDO SÓ OQUE IMPORTA, O RESULTADO

**OBJETIVO**

img-c2-7-02

Ao invez de armaenar, vamos processar em tempo real.

Usaremso com a principal ferramenta: APACHE KAFKA.

Ele é mais complexo e de altíssimo nível. Ele age como um middleware

O Kafka é para o processamento de dados me tempo real. Se voce nao tem isos, da pra redzuir a complexidade do DataLake pela metade

**Divisao do curso**

img-c2-7-03

## Camada de mensagem

Arquitetura do nosos data lake

img-c2-7-04

Pode ter uma ou mais funçôes. As 10 funçôes princiapis da camada de mensagem sao a seguir (nao é obrigatorio para todo projeto).

A camada de mensagem serve como middleware, ela liga o subscribe do consumer com o lsiten dos dados em temp-real

img-c2-7-05

a camadad de messangem é o 'colletor tier'

img-c2-7-06

**Serve para juntar a coleta de dados par aum unico ponto, e de um unicoponto disponibilizar para n consumer**

img-c2-7-08

**Ele é o homem do meio entre a colet de dados e sonsumir os dados, para mandar para n destinos**

img-c2-7-09

ELe funciona como um broker, no modelo lsiten/subscribe e há controle de fila. 

**Ela vai centralizar N fontes e disponibilizar para M consumidores**

O Kafka nao é a ferremante pra todos os problema,s só proque ele é fodâo

### FUnçôes da camada de mensagem

** F1**

img-c2-7-f01

Voce dissocia fonte do destino. Isso serve como uma espécie de interfcace em Java. Onde um lado nao precisa se preocupar com quem será do ouro lado, posi cabe ao objeto do meio fazer essa integraçAô. 

Assim, se um das partes mudar, a mudnça pode ser feito somente nese midleware

img-c2-7-f02

Garante que seja entregue em ordem

img-c2-7-f03

### O que é Apache Kafka

Linkedin, Uber, airbnb, netflix, todas elas usam Kfka para BIg data

Definiçao do que é o kafka

img-c2-7-10.png

img-c2-7-11

Ele é um centralizador e um dispensador, além de ser capaz de fazer ETL.

**LEMbrre, quase qualuer coisa pode executar ETL, ams nem todos da mesma forma qu eo Pentaho**

**Origem do Apache Kafka**

img-c2-7-15

img-c2-7-12

### Arquitetura de Mensagem / Kafka

A definiçaomais simples: serviçod e mensagem que amnda dados de uma lado ao outro.

ELe trabalha com a arquitetura de producers (publica info) e consumers (assinar serviço).

É criado o conceito de topoico, que é nele que o consumer assinar e é nele que o producer envia. É como uma caixa de email

Isso é feito a partir do broker, que é uma uma caixa de correio

img-c2-7-20

img-c2-7-21

### Cluster Kafka

Vmaos colocar várias kafka como se fosse uma.

Nao vamos criar um CLsute rkafka pois precisa relamente disos para processar petabys por segundo

img-c2-7-22

Podemos por brokers em máquinas diferes, um clustetr de kafka.

**O KAFKA NAO TEM UM SISTEMA DE GERENCIMANETO DE CLUSTER, QUEM VAI FAZER ISSO É O ZOO-KEEPER**

**Informaçao de utilizaçao do kafka**

### APache Zoookper

O que sao sisstema distibuidos/cluster

img-c2-7-24

Exemplos de sistema distribuidos

img-c2-7-25

**Pra que serve o zookeeper**

img-c2-7-26

O zzokeerpe vai gerenciar os broketesr e os casos em que ele forem compartilhados entre os nodes do cluster

img-c2-7-23

### Instalar apache Kafka

mesmo procesos, wget, move e desxompopatar,  em seguida, consfigura veariaveis d eambiente

**O KAFKA JÁ VEM COM ZOOKEEPER** 

Há 3 arquivos de configuraçoes do kakfa

consumer.proprietis, zookeeper.proprietis, producers.proprietis

## PARTE 2 - COMPONENTES DO KAFKA

Esse conehcmeicmento é importante para montar uma arquitetura de micro-service

### Apache Kafka - TOPICS

O kfka é como uma caixa de correio: alguqme deposita mensagem la e outra pesosa em outra hora via la e consome.

O 'tópico' é a abstraçao central do Kafkaa.

**O TOÍCO É COMO UMA CATEGORIA DE MENSAGE**

É uma entidade llógia, representada por um arquivo de log

img-c2-7-30

Podemos ter um memso topico entre varios brokers, um cluster kafka

img-c2-7-31

A conceao é feita a um topio e nao a uma maquina, assim, cabe num SistemDistribuido

**O wu tem no topico**

O topico fica organizado sequenciamente no tópico.. O topico tem um conjeutno de mensagens recebidas de um rpdocuer

### Apaceh Kafka - MESSAGE

O que tem dentro de caamda mensagem do kafka

+ timeStamp : controle de tempo
+ id : identificador
+ Payload : dadod sem si

img-c2-7-32


**Como o kafka sabe que uma mensagem ja foi consumida pelo consumer**

Atraves do **Offeset**: um espaço reservado, placeholder, guarda a posiçao da ultima mensagem lida. É mantida pelo Kafka COnsumer

img-c2-7-33

O consumie consome aquela mensagem, e marca aquela mensagem nesse offeset. Assim ele tem o controle ao voltar e ler a mensage: ele pode ler de varias maneiras (ler todas apartir do offest, ler as anteriores tambem ao offset e outrs, tudo isso é configurado)

### Apache Kafka - Politicas

**Por quanto tempo fica as mensanges no Kafkf**

O producer gera mensagnes, mas o consumer nao precisa ocorre ao mesmo tempo.

**O PROCESOS É ASSINCRONOR**

COmo nao preciso ter os doias acessando ao mesmo temo, eu preciso de uma política de retenção. POis nao posso guarda eternmanete

**Politica de retençao**
+ O kafka retem toads as mensagen publicadas indpendente do consumo por um tempo que é 168 horas, ou seja, 7 dias. Isso é o suficiente para processar dados em tempo real.
+ Cada topico pode ter uma retençao difenrete
+ Lembrese de considera o espaço em disco ao definir a poitica de retençao. Dpeois do periodo, as mensagens sao excluidas


## PARTE 4  - USAR KAFKA E ZOKEEPR REALMENTE

### Kafka cluster

Vamos criar uma kafka clusteer independende de datalake
1. COnfigurar Kafka CLuster
2. Inicializar Broker
3. Produizir e consumir mensagens de um topico
4. Por fim, ver essa mensagen sno kafka

*Lembres, agente nao vai criar um cluster kafka, entao porque tem esse nome no titulo*

Porque a idea do kafka sempre foi trabalhar com SistemDistribuido, entao ele foi feito para cluster, para haver varios brokers. Mas vamos só usar um unico cluster que ainda asism recebe a terminiologia de cluste kafka (pois setsmos testando/laboratoria)

Vamos usar SOMENTE O MASTERNDOE

Abra 4 terminais na máquina local que ussam putty na ec2 MASTER

Zooker fica na porta 2181

Usamos telnet para ver se o zookeper esta online

### Cluster com ZOokerper : a forma de operar o kafka

O kafka funciona no zookeoer. ponto.

o zookeper gerencia cluster (n maquinas trabalhando juntas). pnto

Mesmo que voce tneh uma unica maquina, voce ainda asism referenia ao zookerper, entao comandaso de lsitar/crirar/deletear topicos zonsisnte em mandar sses comandos ao zooker e ele fazer as coisa no cluster kfka de 1 ou n maquinas.

### O que soa commit logs

Sao uma fonte confiante de dados, como se fosse tranasaçoes bem registradas, nao só de insert mas tambem de alter do SQL

img-c2-7-37

img-c2-7-38

O Kafka eé como se fosse um commit log salvo, e acessado poelos consumers

### COncluindo Lab 4
(5min da ultima aula do lab 4)

Analogia que eu fiz do kafka:
uma trehad manda dados,
outr a thead mantesm s dados
outra theard retira os dados
Os dados sao odernado pela 2 trhead.

É o middleware, o nome do meio. N produtores produzem mensagens para M topicos e 1 ou mais topicos podem ser consumidos por Q consumidores

## PARTE 6 - Desnvolver um Kafka producer em Java

Apartir d aIDE INELIJ usando Maven, cria uma classe Java que vai conectar a EC2 que está rodando o kafka e asim produz 1000 mensagen de forma randomica

## PARTE 7 - COnfigurando Multi-CLuster Kafka Cluster

ANtes tinhamos 1 unico broker, agora vamos fazer mais de um broker

abrir 7 temrinais na mesma  mauqina
1 - zooker
3- 3 broker
1- produce
1- consumer
1 -teste random

O que façao
+ 3 pbrokers em portas difenrete (façoisso modificando filesfisicas) criarva varios server-0.proprieties

Houve um erro ao subir multi-broker, e isos aconteceu porque cada broker tem que ter um diretorio de logs difernetes

## Lab FInal

até aqui estudamos o Apache Kafka, agora vamos integrar o Kafka ao nosso datalake.

img-c2-7-40

**Porque vamos usar o Kafka**

**IMPORATNTE**: Tanto Flume quanto NiFi preciasram do zookeper? **NÂO**

Eles sao ferramenta nao-dsitribuidoas, cada um é feito em uma unica maquina.

Entao, como vamos slavar os dados sem salválos no DataLake? Atraves do kafka.

Lmbe-re, o Kafka nao é o HDFS mas ele vai manster os dados seguros nates de chegar la. Isso por que **ESTAMOS NUM AMBIENTE EM QUE É DISTRIBUIDO E ASINSCORNO, VAMOS MASNTE ROS DADOS ATÉ QUE ALGUEM VÁ LA, CONSUMA O BROKER E ASISM SALVE NO HDFS**

A ideia é: manter os dados como mensagem por 7 dias, e depois, ai sim, processar e talvez guardar no HDFS

Proposito das ferarmentas
+ FLume: COleta de Straming
+ Kafka: Mnater uma camada de mensagens, de pesistencia daos dados, de modo qeue, se algum node falahr eu consigo garantir a entrega dos dados
+ Nifi: Ferramenta de ETl


#### STREM-SETS

Uma nova feramenta. com 100%de certeza, vai inculuir o StreamSet nas suas ferramentas preferidas

Criado em 2014 por um engenhrio da cloudera. **GRATUITO**. FOi criado para opeçaores de DataOps entre sistemas eterogenios

**DRAG-AND-DROP VIA BROWSER**

HÁ DASHBOAR TOTALMENTE PRONTOS COM STATISCAS DE DADOS, UTILIZAÇAO DE MEORIA E TUDO O MAIS. 

img-c2-7-41

### O que faremosC

img-c2-7-42

Vamos fazer 2 pipelin
1. De IOT , Strmeiing de addsso
2. de RDMS, cada  nova row vai gerar um stream

No curso de ML e SD vamos reproduzr isso e no final vamos aplicar ML

### Instalando e usando Strem Sets

img-c2-7-44

### Criando os pipileinse no StreamSets

Criamos 2 pipelines, um para mandar do producer ao kafka (producer)

E outro para cuonsumier, do consumier para o Haddop HDFS

Nao colocamos tudo junto porque se dar erro para tudo, e tanto o processo do conumer quanto que o producer SÂO E DEVEM ESR INDEPENDENTES

DA PRA FAZER ALGUMAS COISA COMO O PENTAHO no StreamSets

Da aual 23 em dianete, é o pipeline 2 pegando do banco relacional

Agente instala o MysQL an maquina Master e agente criar a tabela em conolse
s
img-c2-7-47
