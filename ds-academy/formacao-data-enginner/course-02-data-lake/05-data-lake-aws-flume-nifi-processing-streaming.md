# Data Lake - Processamento de Streaming - Flume e NiFi

## Links



## PARTE 1  - STREAMING TEORIA



### Introdução

No cap 5, usamos o apache sqoop, agora, vamos trabalhar com o apache flume



### Aquisição de dados em Streaming

Big Data: 4 V: Volumes, Variedade, Velocidade e Veracidade

Aquisição em Batch trate de volumes, em Streaming, trata-se de Velocidade 

Isso gera outro conceito: **FAST DATA** Ecossistema Para coletar e analisar dados em tempo real, gerado no momento que o dado foi criado.

E tanto dados em Batch quanto em Streaming vão para uma única arquitetura: do Data Lake



### O que é Streaming de dados

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-01.png)

Exemplos:

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-02.png)

Em suma, o resumo para essa categorias são:
+ Dados gerados em tempo real, de forma continua em alta velocidade
+ Tamanho pequeno (ex: twitter)
+ Há uma Sequência (time Series) : tenho que garantir uma sequência, ou, pelo menos, me preocupar com isso

**Eu tenho que guardar todos os dados de streaming?**

Depende, há muitas empresa que simplesmente pegam os dados, processa e do resultado do processo é que guarda



## PARTE 2 - Apache Flume



### Apache Flume

Funciona de forma semelhante ao Sqoop, mas agora para Streaming.



### Diferença entre Flume e Sqoop

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-03.png)



### Características do Flume

**Confiabilidade**

**TODOS OS PRODUTOS DO FRAMEWORK HADOOP FORAM DESENVOLVIDOS PARA RODAR NUM AMBIENTE DISTRIBUÍDO. OU SEJA, JÁ ESTÁ PREPARADO PARA FALHAS DE HARDWARE/REDE E PARA TRABALHAR COM MÁQUINAS DE CUSTO DE VIDA MENOR**

Falha é considerado regra no sistema hadoop

**Escalabilidade**

Se precisar de mais potência, pode-se adicionar máquinas para aumentar a capacidade

**Gestão**

Sistema Master/Slave

**Extensibilidade**

Ele usa Java, e free-source, então você pode estendê-lo



### Arquitetura Flume

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-04.png)

Nos temos essas 3 estruturas no Flume: Source, Channel e Sink. E podemos manejá-las e formas diversas topologias, que são listadas a seguir

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-05.png)



### Topologia Pipeline Distribuído

**O que é Pipeline**: Linhas de tubos/canos. É um conceito bastante comum nos EUA. A ideia é ser uma linha de produção, como uma fábrica de carros

A seguir temos o exemplo de um pipeline do Pentaho

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-06.png)



### Topologia Fan-Out e Fan-In

Fan-Out: 1 Source, vários Sink
+ O nome van out quer dizer 'ventilando para fora', quer dizer que mando para muita gente
+ Essa topologia é indicada para armazenar os dados

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-07.png)

Fan-In
+ Busca de várias fontes
+ Ideal para processar os dados, ai, você só guarda o resultado

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-08.png)

A TOPOLOGIA DEPENDE DO SEU OBJETIVO


Você ainda pode criar a sua topologia se quiser

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-09.png)



### Arquitetura flume : Design de 3 camadas

O filme tem 3 camadas FÍSICAS

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-10.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-11.png)

**O APACHE FLUME É UM TOOL ACOPLÁVEL, ENTÃO, VOCÊ TEM BASTANTE FLEXIBILIDADE PARA FAZER AS COISA MAIS DOIDAS QUE SEU PROBLEMA NECESSITAR**

**POR FIM, LEIA O MATERIAL SOBRE A COLETA DO FLUME**



## PARTE 3 - Instalar Flume e Twitter Streaming



### Instalar Flume 

**4 vídeos**

O flume é mais simples que o Hadoop para configurar, mas ainda é algo chato.

Vamos colocar o Flume na NodeMaster

**Na pasta Lib há vários 'jar' que são formas para conectar a um streaming de dados**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-12.png)

vamos editar flume.sh, copiando e renomeado do template



### Twitter App

Vamos consultar API do Twitter

Vamos precisar de 4 chaves
+ Consumer Key
+ Consumer Secret
+ Access Token
+ Access TOken Secret



### Flume Source

**CONECTAR E FAZER A EXTRAÇÃO**

Vamos voltar ao MasterNode, onde está o flumes e vamos criar o arquivo 'twitter.conf' onde vou criar o flume-agent e já por as configurações

EM Twitter.keyword agente defini o critério para busca do twitter



### Flume Sink

**DECIDIR A SAÍDA DOS DADOS**

Está nas configurações, tudo é feito num arquivo só

vamos criar um diretório no HDFS

Vamos coletar em tempo real, palmas para coletar os dados, vai acumular 100 eventos, assim, vai ser de mil em mil. Podemos ainda fazer um delay



Use o comando 'top' para ver os processos. Para para 'kill -9 8535'



### Acessando os dados

URL + Porta:9870  => Os dados são salvos no HDFS e podem ser baixados.

**BASH**


**Ele criou um arquivo, agen.sh e colou para rodar em BackGround, segundo plano. ( ou seja, sem precisar de abrir terminal). 

Ainda é possível com esse .sh configurar no chrom (o gerenciador do linux) e agendar para rodar/terminar esse processo



### Ferramenta

Apache Flume é simples. Se tiver o jar para o seu source, então é bem simples.

Entretanto, caso não tenha, você precisa desenvolver para a linguagem Java.

**ALTERNATIVAS AO FLUME**

Apache Flink e Apache Flink

Apache Flink permite que você processe os dados antes de mandar. Com o FLink eu posso processar e entregar o resultado, e não salvar no storage.

Ele é mais complicado, mas ideal para quem quer processar os dados em tempo real

**A saída do flink pode ser a entrada do flume**

Apache niFI

Concorrente do Flumes, ele tem uma interface drag-drop, o que facilita muito o trabalho

Vamos trabalhar com um mini projeto usando o Apache Nifi



## PARTE 4 - Apache Nifi



### O que é Apache Nifi

Apache Nifi cria um dataflow. Usa o conceito de grafo direcionável. 

**É UMA ESPÉCIE DE ETL SUPER-POTENTE**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-14.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-15.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-16.png)

Computação distribuida
+ É quando fazemos coisas complexas. O niFi serve para ETL que são atividades simples
Eventos COMPLEXOS



### Componentes

FLowFile, Processor

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-17.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-18.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-20.png)

processor built-in do nifi

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-19.png)

fluxograma completo

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-21.png)

É uma ferramenta ETL para ambientes distribuídos



### Instalar o nifi

vamos instalar o nifi na masterNOde, mas poderíamos fazer em nossa própria máquina, ou em outra EC2

df -h : testar o uso do HD da AWS EC2

Para Instalar: 
1. vamos baixara com wget, vamos mandar para o diretório opt/ e descompactar lá
2. no ambiente unix, temos que configurar o java-home em nifi-env.sh 
3. execute /nifi.sh run



### Explorando

Vai subir a na porta 8080, então como eu vou acessar pela EC2 se o EC2 não tem browser.

**COMO ELE SOBE NUMA PORTA, ENTÃO VAMOS ACESSAR PELO SEU DNS PÚBLICO NA PORTA 8080/nifi**

Lembre-se, coloque o inbound para o seu IP, por questão de segurança

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-22.png)

Entre dois processos, é criado um conector

Na parte 3 de Apache Nifi ETL 3 tem uma informação muito importante

O NiFI se comporta como o Pentaho (são parecidos) mas o Nifi além de executar 24h a todo momento, **QUANDO ELE MOVE OS DADOS ELE DEIXA SALVO**.

No exemplo desse vídeo, ele cria um arquivo de texto básico. Esse arquivo é então capturado pelo conector do nifi. Ele some na hora, e não aparece na pasta '/artege' porque esse processador não está executando. ENTÃO SALVA OS DADOS, MANTENDO ELES SEGURADOS E EM ALGUM LUGAR CASO ESTEJA NO MEIO PARRA NO MEIO DO PROCESSO

**ELE ARMAZENA NUMA FILA**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-23.png)



### Mini projeto de coleta de dados de IOT

Ele considera o Apache NiFI uma excelente ferramenta

MQTT é o protocolo parecido com o FTP, orientado a list/subscribe, semelhante ao apache kafka

Usaremos o HiveMQ para simular o Broker do IOT

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-6-24.png)



### Configurando Broker e Websockets

Vamos configurar um broker e gerar dados fictícios

HiveMQ é gratuito e usado para testar e brincar com IOT



### Usando

ConsumeMQQ e depois vamos configura-lo

e depois vai ligar com PutHDFS

Inicializar o HDFS (caso esteja desligado)

```
=> $HADDOP_HOME/Sbin/start-dfs.dh
=> $HADDOP_HOME/Sbin/start-yarn.sh
```

Ver processos

```
=> jps
```

Criar diretorio no hadoop

```
=> hdfs dfs -mkdir /user/haddop/iotdata
```





