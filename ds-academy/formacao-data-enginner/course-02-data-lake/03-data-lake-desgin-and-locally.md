# Design de DataLake e Instalando Local (VirtualBox)

## Resumo

Ensina sobre a Stack do Datalake, ou seja, os componentes que fazzem o datalake funciona.

ENsina sobre o Haddop Framework e os principais compoentnes que seoa utilziados durante a formaçâo

Haddop HDFS e SPark

Por fim, Fazemos a insatalaçao real de um datalke usando maquin virtual

Nos 3 ultimos video da parte 1 - Criar 3 maquinas virtuais CentOS

Na parte 3 (capitulo 4 inteiro) é a instalaçâo do Haddop, HDFS, Spark e testar se tudo funciona como deve funcionar

## Links

Putting the Data Lake to Work - A Guide to Best Practices
https://hortonworks.com/wpcontent/uploads/2014/05/TeradataHortonworks_Datalake_White-Paper_20140410.pdf

The Data Lake Is A Design Pattern
https://medium.com/data-ops/the-data-lake-is-a-design-pattern-888323323c66

Data Lake Architecture
https://www.zaloni.com/platform/tech-stack-reference-architecture/

Moving Data into a Data Lake Hadoop Environment
https://www.attunity.com/data-lake-hadoop/

How to Guide: Architecture Patterns to Consider When Designing an Enterprise
Data Lake
https://www.cloudtp.com/doppler/how-to-guide-architecture-patterns-to-consider-when-designing-an-enterprise-data-lake/

O GDPR Ameaça o Futuro da Ciência de Dados?
http://www.cienciaedados.com/o-gdpr-ameaca-o-futuro-da-ciencia-de-dados/

Apache Hadoop
http://hadoop.apache.org/

Apache Spark
https://spark.apache.org/

Inside Google Datacenter
https://www.youtube.com/watch?v=XZmGGAbHqa0

Facebook Datacenter
https://www.youtube.com/watch?v=_r97qdyQtIk

## Intro

Para montar o datalake, é necessário usar diversas ferramentas, para diversas funçôes e há várias ferramentas par auma mesma funçao. POr isos é necesśario

**PLANEJAR AS ETAPS E QUAIS FERRAMENTAS USAR. Isto é, montar um DataLake Stack : Todas as etaps**

Vamos fazer 2 datalek
+ 1. on-premisee
+ 2. AWS (parte 2)

## PARTE 1 - Teoria - Data Lake Stack

### COmponentes do DataLake Stack

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-01.png)

Começando de baixo pra cima
+ 1 - Tipo de estrutura
  
  - CLoud, Local, Hibrida, Multi-Cloud
+ 2. Storage
  - Qual a soluçâo de armazenamento
  - Ex: HDFS
+ 3. QUal o tipo de computação
  - Ex: MapReduce, Spark
+ 4. Data Managemente
  - Governança para se trabahr com os clusters
+ 5. Aplicações que vão usar os dados
  - PowerBI? Python? e etc

**Os 4 últimos sâo independentes do tipo de infra (1 - cloud/local)**

### ETAPA 1 - Escolha da Infra

**VAI SER: CLOUD, LOCAL, MultiCloud ou Híbrida**

Vamos criar uma localmente e outra na nuvem que será a principal.

O tutor acredita que a nuvem é melhor pois:
+ Tem mais suporte e seguranaça, e simplifica muita coisa
+ Muitas responsabilidades sâo jogadas para a amazon

### Cases de Sucesso : DATA LAKE AS SERVICE DLasS

Exemplo de cases de sucesso Zaloni:
+ Ela monta o datalake Stack e vende a uma empresa

Outra empresa, Knowledgemnet:
+ Ele vende a soluçâo de BigData como serviço

**O QUE VAMOS FAZER É CRIAR ESSA SOLUÇÂO, ENQUANTO QUE ESSA EMPRESAS JÁ VENDEM ESSSA SOLUÇÂO PRONTA**

### ETAPA 2 - Escolha do Data Storage

Soluções
+ HDFS: Acabou se tornando o sistema padrâo para sistema distribuidos
+ Object Storage
  - Amzon S3
  - Microsoft Azure Blob Storage
  - Google CLoud Storage
+ Apache Hive Tables
  - Para tabelas com muitas colunas
  - ELe nâo é um sistema de armazenamento, ele é um sistema de DW
  - O Hive é rodado sobre o HFDS e facilita interagir com o HDFS
+ Apache HBase
  - Para tabelas com poucas colunas e muitos registros
+ ElasticSearch
  - Serviço de busca em arquivos
+ Pode também montar com MongoDB e Cassandara

Lembre-se, O datalake é um conceito

### ETAPA 3 - Processamento de dados

Antes de tudo, voce precisa saber o tipo de processamento que vai ser feito: **BATCH e STREMIANG** pois as soluções de um nâo resolvem a do outro.

SOluçâo para processar Batch
+ Apache MapReduce
+ Apache Spark
+ Apache Hive
+ Apache Pig

Soluçâo para processar Streaming
+ Apache Spark Streaming
+ APache Kafka
+ Apache Flume
+ Apache Storm

Soluçôes de intragrçaô
+ Apache Drill
+ Apache NiFi
+ Apache Beam
+ Apache Sqoop

### Etapa 4  -Governaça

Ver PDF, é politicagem

### Etapa 5

Quem vai usar o datlake nao faz parte do datalke, mas como vai suslao, é necessário considerar as soluôes qu eutilizarao os dados

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-02.png)

### Referência para Design de Data Lake

EMpresa: ZALONI

Exemplo de design para um datalke

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-03.png)

### Diferneça entre DataLka e e DW

### Data Lake – Design, Projeto e Integração ####

  ---- Data Storage e Retenção ----
---- Data Lake x Data Warehouse ----

	Um Data Lake, por definição, oferece um armazenamento de dados muito
mais econômico do que um Data Warehouse. Afinal, com o modelo schema-onwrite
tradicional dos Data Warehouses, o armazenamento de dados é altamente
ineficiente - mesmo na nuvem.

	Grandes quantidades de dados podem ser desperdiçadas devido ao
problema de tabela esparsa.

	Para entender esse problema, imagine construir uma planilha que combina
duas fontes de dados diferentes, uma com 200 campos e outra com 400 campos.
Para combiná-los, você teria que adicionar 400 novas colunas na planilha original
de 200 campos. As linhas da planilha original não possuiriam dados para essas 400
novas colunas e linhas da segunda planilha não conteriam dados das 200 colunas
originais. O resultado? Espaço em disco desperdiçado e sobrecarga extra de
processamento.

	Um Data Lake minimiza esse tipo de desperdício. Cada parte dos dados é
atribuída a uma célula e, como os dados não precisam ser combinados na
entrada, não existem linhas ou colunas vazias. Isso possibilita armazenar grandes
volumes de dados em menos espaço do que o necessário para bancos de dados
convencionais relativamente pequenos.

	Além de precisar de menos armazenamento, quando o armazenamento e a
computação são separados, os clientes podem pagar pelo armazenamento a uma
taxa menor, independentemente das necessidades de computação (caso estejam
usando ambiente em nuvem). Os provedores de serviços de nuvem, como o
Amazon Web Services (AWS), oferecem até mesmo uma variedade de opções de
armazenamento em diferentes faixas de preço, dependendo dos requisitos de
acessibilidade.

	Ao considerar a função de armazenamento de um Data Lake, podemos
ainda criar e impor a retenção de dados baseada em diretivas. Por exemplo,
muitas organizações usam o Hadoop como um sistema de arquivamento ativo
para que possam consultar dados antigos sem precisar ir para a fita. No entanto,
o espaço se torna um problema ao longo do tempo, mesmo no Hadoop; Como
resultado, tem que haver um processo para determinar por quanto tempo os
dados devem ser atendidos no repositório bruto e como e onde arquivá-los.

## PARTE 2 - Sistemas Distribuidos, Haddop, HDFS, CLuster

Usaremso apache Haddop e Spark, e no proximo cap, vamos construir em nuvem

### O que é Apache Hadoop

**NÂO SERÁ FEITO UMA INTRODUÇÃO BÁSICA POIS JÁ ESTÁ NO CURSO GRATUITO DA DSA**

**APACHE HADDOP É UM FRAMEWORK, E POSSUI VÁRIOS COMPONENTES**

São eles
+ Haddop COmmon
+ HDFS (Haddop Distributed File System)
+ Haddop Yarn
+ Haddop MapReduce


Usamreos HDFS para Storage e Apache SPark para processamento de Dados.

O MapReduce é recomedado para yota bytes, enquantoque o spark para TeraBytes



### O que é HDFS

O que é um cluster: Um conjunto de máquinias que se comportam como uma só.

Nosso DataLke será um clsuter, e usaresmo o HDFS para fazer isso

O HDFS é um sistema de arquivos para ambiente distribuido, ou seja num cluster.

### Pricipais Características do HDFS

O que é um sistema distribuidos: É gerenciar n máquians como se fosse uma só.

**Para suportar BigData, é necessário mais de uma máquina**

**Características**
+ Tolerância a Falhas
  - Se uma máquina falhar, ele já replicou os dados em outro cluster, e asism ele pega de lá.
  - De tal forma que o usuário não precisa fazer nada
+ Integridade
  - 
+ Segurança
  - Privilégios de acesos ao arquivos
+ Desempenho
  - POssui desempenho

### Outros sistemas de Arquivos Distribuidos

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-04.png)

NFS
+ É como se fosse um serevr dentral de uma empresa de médio/pequeno porter. Uma pasta compatilhada.
+ Tem isso por default no WIndows

GFS
+ Desenvolvimento em C++
+ É o sistema que foi inspiraçâo apra a criaçâo do Haddop
+ Usa sistema Mestre/Escravo

HDFS
+ Desemvolvimento em Java
+ Bem parecido com o GFS da gogle, mas de free-source
+ Há notícias de um cluster de 7.000 máquins rodando sobre o HDFS

**O QUE O HDFS FAZ DE TÃO ESPECIAL**
Replica um bloco do arquivo em diversos clustsers. Esse bloco de arquivo tem o tamanho de 64Mb bem maior que os blocos de arquivo default do win/unix

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-05.png)

### Arquitetura HFS

Usa o schema Master/Slave ou pode ser encontrado como Master/Worker

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-06.png)

**Imagem**
+ TEmos 2 clusterm cada um com 3 máquinas/caizas/servers.
+ EM cada um dos cluster, há somente um nó que tem o NameNode (Masstrre), e os outros só tem DataNode (Worker)
+ Todos estao conectados por um switch

O HDFS replica o dado em vários CLuster, assim, se um deles falhar, tem no outro com  o dado.

O name Node deve ser implementado na melhor máquina (principamente memória), e os slaves em piores. 
+ FSImage: Armazena
+ EditLOg: Armaznea as alteraçôes nos meta-dados dos arquivos

Secondary NameNode:
+ Nâo é um backup do NameNode. Se o NameNode principal falhar, eu tenho esse secondary
+ O SecondNameNode faz a junçâo do FSImage e o EditLog, criando um checkpoint

**DataNode E Slaves/Worker**
+ Armaenznam mesmo os dados
+ EM cada DataNOde há o TaskTracker que faz o processmaneto pelo MapReduce (Nós nao vamos ver o MapREduce, usarremos Spark)
+ O DataNode fica enviando constantemtne para o NameNode, e asism o NameNode sabe que blosocs estoa em cada datanode

### Replicaçâo de Blocos no HDFS

Porque fazemos replicaçÂo

+ Tolerância a falhas e confiabildaide dos dados
+ Se o slaves falaha, o processamento vai ser feita em outra. O HDFS faz iso de forma autoomatica que nao impacta em nada no processamento
+ Se um Slave falaha, ele nâosó busca o bloco de outro Node, mas tambem duplica, garantindo que tenha sempre 3 nós vivos prontos

Há a recomendaçâo de duplciar o mesmo bloco no mesmo hack mas em nós distantos

### Como Funciona o Cluster Haddop

É um conjunto de Máquinas criaod para armzanear e processar um grande volumes de dados, sejam eles estruturados ou nâo-estruturados EM PARALELO num sistema DSITRIBUIDO

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-07.png)

**FUNCIONMENTO REAL DO HADDOP**
+ 1 - Request do cliente para o HDFS/MapREduce;
  - Aí um Job é criado e começa o processamento do Haddop
  - É consultado o NameNode, e se for para um processametno de MapReduce, é consultado o JobTracker
+ 2 - Os dados sâo dividiso em blocos, e Jobs sâo divididos em tareafas
+ 3 - Aloca as partes menores para cada CLuster, fazendo asism, processamento distribuido
+ 4 - Cada nó do clsuter vai estrá trabalhando de froam individula e processando a sua parte que compoe o Job Completo
  - É recomendado que todas as maquinas tenham o mesmo desempenho, pois asim, o que determina a velocidade do job É A MÁQUINA MAIS LENTA
+ 5 - Unir os redulstados
  - Etapa do SHuffle: Faz o MapReduce usando JobTracker sobre os TasckTracker
+ 6 - Resultado final

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-08.png)



**OS DADOS FICAM NO DATANODE, E OS METADADOS NO NAMENODE**. 
+O name Nde mantenm os dados em memória

MapReduce/Spark: O processamento do MapReduce é feito em arquivo. O do SPark é em memoria

### Modos de Execuçâo do Haddop

Modos de Execução do Hadoop ----


	Embora uma aplicação Hadoop seja tipicamente executada em um
conjunto de máquinas, ela pode também ser executada em um único node. Essa
possibilidade permite adotar configurações simplificadas para as fases iniciais de
implementação e testes, visto que depurar aplicações distribuídas não é algo
trivial. Posteriormente, outras configurações mais sofisticadas podem ser
utilizadas para usufruir de todas as vantagens oferecidas pelo framework Hadoop.
São três modos possíveis de execução do Hadoop:	

	• Modo Local (Standalone)
	• Modo Pseud-Distribuido (Pseudo-Distributed)
	• Modo Totalmente Distribuido (Fully Distributed)
	
	Para alternar entre essas configurações é necessária a edição de três
arquivos: core-site.xml, hdfs-site.xml e mapred-site.xml. Veremos isso mais a
frente!


Modo Local (Standalone)

	O Hadoop é por padrão configurado para ser executado no modo local.
Dessa maneira, se essa for a sua opção escolhida, os parâmetros nos arquivos de
configuração não precisam de alterações. Esse modo é o mais recomendado para
a fase de desenvolvimento, onde normalmente ocorre a maior incidência de
erros, sendo necessária a realização de vários testes de execução. Nessa
configuração, todo o processamento da aplicação é executado apenas na
máquina local. Dessa forma simplificada, fica mais fácil para o usuário realizar a
depuração de seu código, aumentando sua produtividade.


Modo Pseudo-distribuído

	Uma segunda alternativa para executar uma aplicação Hadoop é o modo
Pseudo-distribuído. Nesse modo são aplicadas todas as configurações,
semelhantes às necessárias para execução em um cluster, entretanto, toda a
aplicação é processada em modo local, por isso o termo Pseudo-distribuído ou
também chamado “cluster” de uma máquina só. Embora não seja executado
realmente em paralelo, esse modo permite a sua simulação, pois utiliza todos os
processos de uma execução paralela efetiva: NameNode, DataNode, JobTracker,
TaskTracker e SecondaryNameNode.
	

Modo Totalmente Distribuído

	Por fim, o terceiro e último modo de execução é utilizado para o
processamento distribuído da aplicação Hadoop em um cluster de computadores
real. Nessa opção, como no modo pseudo-distribuído, também é necessário
editar os três arquivos de configuração, definindo parâmetros específicos e a
localização do SecondaryNameNode e dos nós escravos. Todavia, como nesse
modo temos diversos computadores, devemos indicar quais máquinas irão
efetivamente executar cada componente. Esse é o modo com o qual vamos
construir nosso Data Lake na sequência deste capítulo.

### REcomendaçao de máquinas físicas

Recomendações de hardware para os nós slaves:

• Storage
	Em um ambiente de intensivo de IO, recomenda-se 12 discos SATA 7200 RPM
	de 2 TB cada um, para balanceamento entre custo e performance. RAID não é
	recomendado em máquinas com serviços slaves do Hadoop.

• Memória
	Nodes slaves requerem normalmente entre 24 e 48 GB de memória RAM.
	Memória não utilizada será consumida por outras aplicações Hadoop.

• Processador
	Processadores com clock médio e menos de 2 sockets são recomendados.

• Rede
	Cluster de tamanho considerável, tipicamente requer links de 1 GB para todos os
	nodes em um rack com 20 nodes

---------------------------------------------------------------------------------------

Recomendações de hardware para nós master:

• Storage
	Deve-se utilizar 2 servidores: um para o NameNode Principal e outro para o
	Secundário. O Master deve ter pelo menos 4 volumes de storage redundantes,
	seja local ou em rede.

• Memória
	64 GB de RAM suportam aproximadamente 100 milhões de arquivos

• Processador
	16 ou 24 CPU's para suportar o tráfego de mensagens



### COnhecendo outras distribuiçoes do Haddop

Exexmeplo: A empresa **CLoudera** já disponibiliza uma máquin virtual com haddop já instalado. Isso é gratuito e por na sua virtual box.

Hortonworks: Desemvolveros seus próprios produtos sobre o Haddop. É a maems idiae: o haddop é grautiro, mas eles pegaram, modificaram e colocaram em virtual =box. ALém de oferecer como produto, els também dão suporte

MAPR: A mesma coisa que as outras

Esas sao as 3 que dominam o Haddop no mercado.

**Vamos usar o Apache Haddop Raiz que dá muito mais trabalho que usar o Haddop desass empresas** 

## Parte 3 - SPARK

### Apache Spark

Usaremos o Spark para procesamsetno paralelo/distribuido

A imensa maioria do BigData que é gerado hoje, 80%, é de dados NÂO ESTRUTURADOS

**PROBLEMA**

**COMO ARMZENAR E PROCESSA TODOS OS DADOS, SE SEU VOLUME CRESCE DE FORMA EXPOENCIAL**
+ Vamos usar um cluster para resolver isso

Para processar isos, usamos o SPark que faz o procesamento em memoria: É possivel utiliza ele nas linaguae
+ Java, Scala, Python, R 

É um dos principais projetos da Apache Foundation. O Spark é bem rápido.

ELe utiliza a memoria distribuida de diveross clustsers, o mapa reduce utiliza somente o Storage do cluster, que é mais lento, só que ageunta mais carga.

O apache spark é melhor que o mapReduce SE E SOMENTE SE EU CONSEGUIR PROCESASR TUDO EM MEMÓRIA. 

POis a memoria RAM é bem menor que a Stoarge

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-09.png)

Foi criado sobre o Scala que por sua vez usa a JVM.

### COmpoentne do Spark

4 modulos principais
+ Streaming
  - Processa dados em tempo real, fazneod ETL numa janela de processametno
+ Mlib
  - Bibilitoe da estatisticas
+ SQL
  - É o Spark sobre pandas, e permite tambme processar JSON
+ GrapX
 - Permite fazer o processamento de Grafos de forma paralela (Há um curso da ADS sobre GrapX o único PT-BR no Brasil)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-10.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-11.png)

Spark CORE API
+  Possui as funcionalidades bascias do Spark
  - POde ser usado com R, SQL, Python, Scala, Java

O pessoal que criou a SPark fundou a 'databricks'

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-12.png)

**Quando usamos Spark**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-3-13.png)

## PARTE 4 - DataLake Local

### Definido o design do DataLke Local

Usaremos 
1. INFRA: ON-premisse (em máquians virtuais)
2. STORAGE: HDFS
3. COMPUTE: SPARK

As outras nao vamos trabalhar agora.

Vamos construir um cluster com 3 nodes, um Master e 2 slaves. 

As 3 máquinas vao ser feitas simultanemante



## Parte 5 - Instlar HDFS e Spark em VirtualBox

### DataLake Part 1 - COmeçando a cosntruir datalke local

+ Virtual Box
+ Usaremos CentOS pcom a Minimal ISO para ser o mais simples possível

### DataLkae Part 2 - Install Datalake, HDFS, Spark tudo local

A parte 2 é descrita nos vídeos a seugir

├── 81. Introdução.mp4
├── 82. Data Lake OnPremises  Parte 4  Conectando nos Servidores via SSH.mp4
├── 84. Data Lake OnPremises  Parte 5  Instalando e Configurando o Java JDK.mp4
├── 85. Data Lake OnPremises  Parte 6  Gerando as Chaves de Segurança.mp4
├── 86. Data Lake OnPremises  Parte 7  Instalando o Apache Hadoop no Node Master.mp4
├── 87. Data Lake OnPremises  Parte 8  Configurando o Apache Hadoop no Node Master.mp4
├── 88. Data Lake OnPremises  Parte 9  Instalando e Configurando o Hadoop nos Datanodes.mp4
├── 89. Data Lake OnPremises  Parte 10  Formatando o Namenode e Inicializando o Cluster Hadoop.mp4
├── 90. Data Lake OnPremises  Parte 11  Testando o Cluster.mp4


+ Usar SSH
+ Instalar JDK
+ Gerar Chaves de Segurnaça
+ Instalar Haddop : NodeMaster e NOdeSlave
+ Testar CLuster
+ Executar Spark
