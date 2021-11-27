# Data Lake - Processamento de Streaming - Flume e NiFi

## Links

## PARTE 1  - STREAMING TEORIA

### Introduçâo

No cap 5, usamos o apache sqoop, agora, vamos trabalhar com o apache flume

### Aquisição de dados em Straming

Big Data: 4 V: VOlumes, Variedade, Velocidade e Veracidade

Aquisiçâo em Batcth trate de volumes, em Streaming, tarata-se de Velocidade 

Isso gera outro conecito: **FAST DATA**: Ecossitem apara coletar e analisar dados em tempo real, gerado no momento que o dado foi criado.

E tanto dados em Batch quanto em Stremiang vao para uma única arquitetrua: o DataLake

### O que é Streming de dados

img-c2-6-01

Exemplos:

img-c2-6-02

Em suma, o resumo para essa catagorias sao:
+ Dados gerados em tempo real, de forma continua em alta velodidade
+ Tamanho pequeno (ex: twitter)
+ Há uma Sequencia (time Series) : tenhoq eu garantir uma sequencia, ou, pelo menos, me preocupar com isso

**Eu tenho que guardar todos os dados de streaming?**

Depende, há muitas empresa que simplimente pegam os dados, processa e do reusltado do processo é que guarda

## PART 2 - Apache Flume

### Apache FLume

Funciona de forma semelhante do Sqoop, mas agora para Streming.

### Difernça entre FLume e Sqoop

img-c2-6-03

### Características do FLume

**COnfiabildiade**

**TODOS OS PRODUTOS DO FRAMEWORK HADDOP FORAM DESENVOLVIDOS PARA RODAR NUM AMBIENTE DISTRIUBIDO. OU SEJA, JÁ ESTÁ PREPARADO PARA FALHAS DE HARDWARE/REDE E PARA TRABALHAR COM MAQUINAS DE CUSTO DE VIDA MENOR**

Falha é considerado regra no sistema haddop

**Escalabildiade**

Se precisar de mais potência, pode-se adicionar maquinas para auamentar a capacidade

**Gestao**

Sistema Master/Slave

**Extensibilidade**

Ele usa Java, e free-source, entao voce pode estendelo

### Arquiteteura FLume

img-c2-6-04

Nos temso essas 3 estruturas no FLume: Source, Channel e SInk. E podemos manejalas e formas diversas topologias, que sao listadas a seguir

img-c2-6-05

### Topologia Pipeline Distribuido


**O que é PipeLine**: LInhas de tudos/canos. É um conceito bastante comun no EUA. A ideia é ser uma linha de produçâo, como uma fábrica de carros

A seguri temos o exemplo de um pipelin do pentaho

Ex; img-c2-6-06

## TOpologia Fan-Out e Fan-In

Fan-Out: 1 SOurce, vários SInk
+ O nome van out quer dizer 'ventilando par afora', quer dizer que mando par amuita gente
+ Essa topologia é indicada para armazenar os dados

img-c2-6-07

Fan-In
+ Busca de várias fontes
+ Ideal para processar os dados, ai, voce so guarda o resultado

img-c2-6-08

A TOPOLGIA DEPENDE DO SEU OBJETIVO


Voce aida pode criar a sua topoligia se quiser

img-c2-6-09

## Arquitetura flume : Design de 3 camadas

O flume tem 3 camadas FÍSICAS

img-c2-6-10

img-c2-6-11

**O APACHE FLUME É UM TOOL ACOMPLÁVEL, ENTAO, VOCE TEM BASTANTE FLEXIBILDIADE PARA FAZER AS COISA MAIS DEOISDAS QUE SEU PROBELMA NECESSITAR**

**POR FIM, LEIA O MATERIAL SOBRE A COLETA DO FLUME**

## PARTE 3 - INSTALL FLUME e App Stremiang

### Instalar Flume 

**4 vídeos**

O flume é mais simples que o Haddop para configurarr, mas ainda é algo chato.

Vamos colcoar o FLume na NodeMaster

**Na pasta Lib há vaários 'jar' que soa formas para concetar a um streming de dados**

img-c2-6-12

vamos editar flume.sh, copiando e renomeado do template

### Twitter App

Vamos consultar APi do Twitter

Vamos precisr de 4 chaves
+ Consumer Key
+ Consumer Secret
+ Access Token
+ Acess TOken Secret

### Flume Source

**CONECTAR E FAZER A EXTRAÇAO**

Vamos voltar ao MatterNOde, oude está o flumes e vamos criar o arquivo 'teitter.conf' onde vou criar o flume-agent e já por as configurações

EM Twitter.keyword agente defini o criterio para buscar do twtitter

### Flume Sink

**DECIDIR A SAIDA DOS DADOS**

Está nas configuraçoes, tudo é feito num arquivo só

vamos criar um diretitorio no HDFS

Vamos coletar em tempo real, pamas para coletar os dados, vai acumula 100 eventos, assim, vai ser de mil em mil. Podemos ainda fazer um delay



Use o comando 'top' para ver os processos. Para para 'kill -9 8535'

### Acessando os dados

URL + Porta:9870  => Os dados sâo salvos no HDFS e podem ser baixados.

**BASH**


**Ele criou um arquivo, agen.sh e colou para rodar nem BackGOrun, segundo plano. ( ou seja, sem precisar dde abirr terminal). 

Ainda é possivel com esse .sh configurar no chrom (o gerenciardo do linux) e agendar para rodar/temrinar esse processo

### Ferramenta

Apache FLume é simples.Se tiver o jar para o seu sorue, entao é bem siples.

Etretanro, caso nao tenha, voce precisa desenvolver par aa linaugem Java.

**ALTERNATIVAS AO FLUME**

Apache Flink e Apache Flink

Apaceh FLink permite que vocÊ processe os dados antes de mandar. COm o FLink eu posso processar e entregar o resultado, e nao salvar no storage.

Ele é mais complicado, mas ideal para quem quer processar os dados em tempo real

**A saida do flinkpode ser a entrada do flume**

Aapache niFI

COncorrente do FLumes, ele tem uma interface drap-drop, o que facilita muito o trabalho

Vamos trabalhar com um mini projeto usando o Apache Nifi

## Parte 4 - Apache Nifi

### O que é Apache Nifi

Apache Nifi cria um dataflow. Usa conceito de grafo direcionável. 

**É UAM ESPÉCIE DE ETL SUPER-POTNETE**

img-c2-6-14

img-c2-6-15

img-c2-6-16

Computaçao distribuida
+ É quando fazemos coisas compleaxas. O niFi serve para ETL que sao atividades simples
Eventos CEOMPLXEOS

### Componentes

FLowFIle, Processor

img-c2-6-17

img-c2-6-18

img-c2-6-20

processor built-in do nifi

img-c2-6-19

fluxo-grama compleo

img-c2-6-21

É uma ferramenta ETL para ambientes disrtribuidos

### Instlar o nifi

vamos instlar o nifi na masterNOde, mas poderiamos fazer em nossa propria maquina, ou em outra EC2

df -h : testar o uso do HD da AWS EC2

Par ainastlar: 
1. vamos baixara ocm wget, vamos mandar para o diretorio opt/ e descompacto la
2. no ambiente unix, ttemos que configrurar o java-home em nifi-env.sh 
3. execute /nifi.sh run

### Explorando

Vai subri a na porta 8080, entao como eu vou acessar pela EC2 se o EC2 nao tem browser.

**COMO ELE SIBE NUMA PORTA, ENTAO VAMOS ACESSAR PELO SEU DNS PUBLICO NA POTA 8080/nifi**

Lembre-se, coloque o inboun para o seu IP, por questao de segurança

img-c2-6-22

ENtre dois processros, é criado um connector

Na parte 3 de Apaceh Nifi ETL 3 tem uma informaça muito improtante

O NiFI se comporta como o Pentaho (sao parecidos) mas o Nifi além de executar 24h a todo momento, **QUANDO ELE MOVE OS DADDOS ELE DEIXA SALVO**.

No exmeplo desse video, ele cria um arquivo de texto básico. Esse arquivo é entao capturado pelo connector do nifi. Ele some na hora, e nâo aparece na pastat '/artege' porque esse processor nao está executando. ENTAO SALVA OS DADOS, MANETENDO ELES SEGURADOS E EM ALGUM LUGAR CASO ESTEJA NO MEIO PARRA NO MEIO DO PROCESSO

**ELE ARMAZENA NUMA FILA**

img-c2-6-23

### Mini projeto de coleta de daddos de IOT

Ele considera o Apaceh NiFI uma excelente ferramenta

MQTT é o protocolo parecido com o FTP, orienteado a lsite/subscribe, semelhante ao apache kafka

Usaremos o HiveMQ para simular oBroker do IOT

img-c2-6-24

### COnfigurando Broker e Web Sockets

Vmaos configurar um broker e gerar dados ficitícios

HiveMQ é gratuito e usadao para testar e brincar com IOT

### Usando

COnsumeMQQ e depois vamos configuralo

e deposi vai ligar com PutHDFS

Inicializar o HDFS (caso esteja desligado)
=> $HADDOP_HOME/Sbin/start-dfs.dh
=> $HADDOP_HOME/Sbin/start-yarn.sh

Ver procesoss
=> jps

Criar diretorio no haddop
=> hdfs dfs -mkdir /user/haddop/iotdata



### PARTE 5 - REvendo oq ue nos fizmeos

Geramos uma maça de dadod no webSocket/IOT
