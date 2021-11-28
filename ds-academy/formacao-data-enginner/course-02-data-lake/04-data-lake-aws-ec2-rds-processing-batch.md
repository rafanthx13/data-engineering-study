# Data Lake  - AWS EC2 - Processando Batch



## PARTE 1 - INTRODUÇÃO E TEORIA

### Intro

Vamos construir um Data Lake na AWS durante 5 capítulos, próximo do mundo real. E no fim, há o Data Lake Servelss onde você cria o datalake sem especificar a infra.

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-5-01.png)
### Aquisição de Dados

É a porta de entrada do nosso datalake.

Vamos trabalhar com HDFS e Sqoop: Que permite conectar a bancos relacionais e levar para a HDFS e vice-versa

**HDFS** e  **Apache Scoop**

### O que são dados em Batch

É o ETL do Pentaho

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-5-06 (2, a 6).png)
### Real-Time x Batch Data

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-5-07.png)
O Real time é o processamento na hora, enquanto que o Batch espera um tempo para fazer (em geral, faz de noite a carga)

### Mapeando os dados do nosso projeto

Este é um schema conceitual

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-5-08.png)
RMDS : Banco RElacional
Sqoop: Pega os dados do banco relacional (Ferramenta de ETL)
Hadoop: Implementa o HDFS nossos storage

Os dados de streaming vamos pegar com o Apache Flume e Kafka (iremos ver isso no próximo capítulo)

## PARTE 2 - APACHE SQOOP

###  O que é Apache Sqoop

Ferramenta para levar dados de banco de dados estruturados para o Hadoop. 

Usaremos uma linguagem SQL para acessar e pegar os dados do RMDS.

Usaremos o Sqoop v1 1.4.7: Ele é mais simples

### Import/Export com Sqoop/Hadoop

**Import**
+ EU conecto o sqoop ao RMDS
+ Eu posso pegar parte dos dados ou todo ele
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-5-09.png)
**Export**
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-5-10.png)
### Conectores Sqoop

Antes de começar o Sqoop, verifique  na sua documentação se ele tem conectores para o seu banco de dados.

Usaremos o PostGreSQL

## PARTE 3 - MONTANDO EC2 NA AWS

### Start Date Lake na AWS

Essa aula explica
+ No primeiros 4 minutos, o motivo de ser melhor criar em nuvem
+ Profissional: A AWS é a maior do market-share, por ser líder, ela disponibiliza vários certificados.

ESTE NÃO É UM CURSO DE AWS

### Como monetizar o Data Lake em Nuvem

Há 3 profissionais:

+ Funcionário:
+ Consultor:
+ Empreendedor:

**A área de Big Data, ML oferece a grande vantagem de permitir que você empreenda, pois não é todo mundo que usa isso. E boa parte das ferramentas são open-source, free**


**O INSTRUTOR TEM VARIAS CONTA NA AWS, ONDE TEM DW, ML, BIG DATA E OFERECE AO CLIENTE COMO PRODUTO**

**Muitas empresa não tem como ter um time de TI só pra fazer isso, se você pode fazer direto para ela e entregar como produto,fica muito bom**

**COMO MONETIZAR COM DATA LAKE**

+ Você pode vender toda a estrutura de Data Lake como um produto.
+ Crie um web-site oferecendo isso: armazenamento, processamento e cobra dele por gigaByte, teraByte

Outro exemplo:
+ Criar uma ferramenta para captura de dados não-estruturados e vender isso para o cliente 

**HOJE, HÁ MUITO DE ML, MAS NAO DA PRA FAZER ML SEM TER DADOS BEM MODELADOS, ESSA É UMA ARE QUE ESTÁ CRESCENDO: DATA ENGINEERING**

### Conta AWS

VIXI:

PARA IMPLEMENTAR AS COISA DAS AULAS, SERÁ NECESSÁRIO USAR SERVIÇOS PAGOS. TANTO É QUE VAI OFERECER R$ 100,00 para reembolso por ter que gastar dinheiro na EC2.

Com R$10,,0 você consegue fazer esse e os proximos capitulos 2 vezes

### AWS EC2

Elastic Cloud Computer

Ele disponibiliza capacidade computacional.

O EC2 pode ser usado gratuitamente, 750h mas para uma instância com apenas 1GB de RAM, Isso limita o agente para fazer um Hadoop.

Usaremos 2 de 4Gb e 1 de 8Gb

### Tree Files

**Vídeos**

├── 94. Introdução.mp4
├── 95. Contexto no Data Lake  Aquisição de Dados.mp4
├── 96. O Que São Dados em Batch.mp4
├── 97. RealTime Data x Batch Data.mp4
├── 98. Mapeamento de Dados.mp4
├── 99. O Que é Apache Sqoop.mp4
├── 100. Arquitetura de Importação.Exportação de Dados com Sqoop.mp4
├── 101. Conectores Sqoop.mp4
├── 102. Data Lake em Nuvem com AWS (Amazon Web Service).mp4
├── 103. Como Monetizar o Data Lake em Nuvem.mp4
├── 104. Criando a Conta AWS.mp4
├── 106. O Que é Amazon AWS EC2.mp4
├── 107. Implementação do Data Lake em Nuvem  Provisionando as Instâncias EC2  NameNode.mp4
├── 108. Implementação do Data Lake em Nuvem  Provisionando as Instâncias EC2  DataNodes.mp4
├── 110. Implementação do Data Lake em Nuvem  Conectando nas Instâncias EC2 via SSH.mp4
├── 111. Implementação do Data Lake em Nuvem  Criando Usuário de Configuração.mp4
├── 112. Implementação do Data Lake em Nuvem  Instalando o Java JDK nas Máquinas do Cluster.mp4
├── 113. Implementação do Data Lake em Nuvem  DNS x Arquivo Hosts.mp4
├── 114. Implementação do Data Lake em Nuvem  Configurando Autenticação SSH Sem Senha 1.2.mp4
├── 115. Implementação do Data Lake em Nuvem  Configurando Autenticação SSH Sem Senha 2.2.mp4
├── 116. Implementação do Data Lake em Nuvem  Instalação do Hadoop.mp4
├── 117. Implementação do Data Lake em Nuvem  Configuração do Hadoop no Node Master.mp4
├── 118. Implementação do Data Lake em Nuvem  Configuração do Hadoop nos Nodes Slaves.mp4
├── 119. Implementação do Data Lake em Nuvem  Inicializando e Testando o Cluster na Nuvem.mp4
├── 120. O Que é Amazon AWS RDS.mp4
├── 121. Preparando o Banco de Dados Transacional com PostgreSQL.mp4
├── 122. Conectando Remotamente no Banco de Dados.mp4
├── 123. Carga de Dados no Banco Relacional.mp4
├── 124. Camada de Aquisição de Dados em Batch  Instalação Sqoop.mp4
├── 125. Configurando o Driver JDBC.mp4
├── 126. Testando a Configuração do Data Lake com o Banco Relacional.mp4
├── 127. Importando Dados do Banco Transacional Para o Data Lake.mp4
├── 128. Preparando o Ambiente Web Para o Data Lake e Agendando Jobs.mp4

**Files**

├── 105. Como Receber o Crédito de R$100 na AWS.txt
├── 109. Alerta de Segurança AWS.txt
├── 111.1 1-01-Data-Lake-Cria_usuario_hadoop.zip
├── 112.1 1-02-Data-Lake-Java.zip
├── 113.1 1-03-Data-Lake-DNS.zip
├── 114.1 1-04-Data-Lake-User-SSH.zip
├── 116.1 1-05-Data-Lake-Hadoop.zip
├── 117.1 1-06-Data-Lake-Hadoop-Config-Files.zip
├── 118.1 1-07-Data-Lake-Hadoop-Slaves.zip
├── 119.1 1-08-Data-Lake-Hadoop-Teste-Cluster.zip
├── 123.1 1-database.zip
├── 126.1 1-database.zip
├── 129. Lab 2 Instalando o HUE (Hadoop User experience) e Acessando os Dados no Data Lake via Browser.txt
├── 130.1 1-database.zip
├── 130. Lab 3  Criando e Automatizando Jobs de Importação de Dados Para o Data Lake.txt
├── 131.1 desafioPentaho.jpg.pdf
├── 131. Desafio  Usando Pentaho Data Integration Para Carga de Dados no Hadoop.pdf
├── 131. links - Desafio  Usando Pentaho Data Integration Para Carga de Dados no Hadoop.txt
├── 132. AWS Calculator.txt
├── 133. Bibliografia, Referências e Links Úteis.txt
├── 134. Slides Módulo 05.pdf

## PART 4 - Criando Cluster Hadoop e buscando Bath com Sqoop

**Vou escrever e tirar print das principais partes, para lembrar e não ficaram somente como HD**




├── 107. Implementação do Data Lake em Nuvem  Provisionando as Instâncias EC2  NameNode.mp4
+ Criar na WAS a instancia com NameNode

├── 108. Implementação do Data Lake em Nuvem  Provisionando as Instâncias EC2  DataNodes.mp4
+ Criar na WAS a instancia com DataNode

├── 110. Implementação do Data Lake em Nuvem  Conectando nas Instâncias EC2 via SSH.mp4
+ Terá que abrir em 2 instâncias do Putty para conectar
+ Conectados com a chave particular da AWS
+ OBS: As instância do EC2 podem ser copiadas, então, depois de criada, você pode duplicar os DataNOde

├── 111. Implementação do Data Lake em Nuvem  Criando Usuário de Configuração.mp4
+ Primeiro, temos que encontrar o endereço DNS público e privado
+ OBS: configurações de rede da AWS podem ser alteradas, pelo RouteS3, mas é pago
+ O que faz: Cria-se usuários sudo específicos para o hadoop nas instâncias

````
Criando usuário hadoop (nos 3 servidores do cluster)

sudo useradd -m hadoop
sudo passwd hadoop (datalake9182)

Obs: Inclua o usuário hadoop no arquivo /etc/sudoers
````

├── 112. Implementação do Data Lake em Nuvem  Instalando o Java JDK nas Máquinas do Cluster.mp4
+ Instalar JDK nas 3 máquinas
+ para acessar o usuário hadoop `su hadoop`
+ `sudo yum install wget`

````
# Instalação Data Lake

# Instalando e Configurando o Java JDK (nos 3 servidores do cluster)

# Acesso como usuário hadoop
su hadoop


# Acessa o diretório
cd /opt


# Instala o wget
sudo yum install wget


# Faz o download
sudo wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.tar.gz"


# Descompacta o arquivo
sudo tar -xvf jdk-8u171-linux-x64.tar.gz


# Renomeia o diretório
sudo mv jdk1.8.0_171/ jdk


# Ajusta os privilégios
sudo chown -R root:root jdk


# Configurando as variáveis de ambiente

cd ~
vi .bash_profile

# Java JDK 1.8
export JAVA_HOME=/opt/jdk
export JRE_HOME=/opt/jdk/jre
export PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin

source .bash_profile


# Verifica a versão
java -version
````

├── 113. Implementação do Data Lake em Nuvem  DNS x Arquivo Hosts.mp4
+ Vamos usar somente DNS

├── 114. Implementação do Data Lake em Nuvem  Configurando Autenticação SSH Sem Senha 1.2.mp4
+ Para uma máquina se ligar a outra sem precisar de senha, vamos criar uma conexão SSH

````
# Instalação Data Lake

# Como usuário ec2-user (em todos os servidores):
sudo mkdir /home/hadoop/.ssh
sudo chown -R hadoop:hadoop /home/hadoop/
sudo cp ~/.ssh/authorized_keys /home/hadoop/.ssh/authorized_keys
sudo chown hadoop:hadoop /home/hadoop/.ssh/authorized_keys
sudo chmod 600 /home/hadoop/.ssh/authorized_keys


# Configurando o SSH (nos 3 servidores do cluster)
sudo vi /etc/ssh/sshd_config


# Certifique-se que estas configurações estejam ativas:

Port 22
#AddressFamily any
ListenAddress 0.0.0.0
ListenAddress ::
PubkeyAuthentication yes


# Restart do SSH
sudo systemctl restart sshd.service


# Apenas no Node Master (como usuário hadoop)
cd ~
ssh-keygen


# Copia a chave

Em cada node slave, copie a chave id_rsa.pub do servidor node master


# Em todos os servidores como usuário Hadoop
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys


# Testa a conexão (usando DNS interno)

ssh hadoop@ip-172-31-7-63.us-east-2.compute.internal
ssh hadoop@ip-172-31-2-100.us-east-2.compute.internal
ssh hadoop@ip-172-31-14-249.us-east-2.compute.internal
````

├── 115. Implementação do Data Lake em Nuvem  Configurando Autenticação SSH Sem Senha 2.2.mp4

Continuação do anterior


├── 116. Implementação do Data Lake em Nuvem  Instalação do Hadoop.mp4

````
# Instalação Data Lake

Obs: Configurar as variáveis de ambiente do Java no usuário hadoop

# Instalando e Configurando o Hadoop

# Acessa o diretório
cd /opt


# Faz download do Hadoop
sudo wget http://www-us.apache.org/dist/hadoop/common/hadoop-3.1.0/hadoop-3.1.0.tar.gz


# Descompacta o arquivo
sudo tar -xvf hadoop-3.1.0.tar.gz


# Muda o proprietário
sudo mv /opt/hadoop-3.1.0 /opt/hadoop
sudo chown -R hadoop:hadoop /opt/hadoop


# Testando a instalação

cd /opt/hadoop/bin
./hadoop version


# Variáveis de ambiente do usuário Hadoop (configurar em todos os servidores)

vi .bash_profile

# Java JDK 1.8
export JAVA_HOME=/opt/jdk
export JRE_HOME=/opt/jdk/jre
export PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin

# Hadoop
export HADOOP_HOME=/opt/hadoop
export PATH=$PATH:$HADOOP_HOME/bin

source .bash_profile

````
├── 117. Implementação do Data Lake em Nuvem  Configuração do Hadoop no Node Master.mp4

Aqui usamos DNS privados, então, se você implementar, vai ter que olhar o seu EC2

├── 118. Implementação do Data Lake em Nuvem  Configuração do Hadoop nos Nodes Slaves.mp4

+ **MUITO INTERESSANTE**: Como essa máquina vai ser ligadas e fizemos um SSH sem senha: **EU COPIO DE UMA PASTA A OUTRA TODO O DIRETÓRIO HADOOP: DA MASTER PARA SLAVE**

├── 119. Implementação do Data Lake em Nuvem  Inicializando e Testando o Cluster na Nuvem.mp4

+ Formatar o namenode 
+ Depois soube, inicializa o HDFS

**NO FINAL, COM O HADOOP SUBIDO, ELE OFERECE UMA PÁGINA WEB PARA VISUALIZAR**, ELA É NA PORTA 9870 




├── 120. O Que é Amazon AWS RDS.mp4
+ Amazon RDS é o banco relacional da Amazon: POde ser: Aurora Db (é um mysql/psotregre modificado pela amazon), MySQL, PostGre, SQL Server, MariaDB
+ É fácil criar, rapidinho


├── 121. Preparando o Banco de Dados Transacional com PostgreSQL.mp4
+ Procure o pgAdmin para conectar no postgre
+ O **CLIENTE ABRE NO BROWSER**
  - Clique em Server e coloca as coisas


├── 122. Conectando Remotamente no Banco de Dados.mp4
+ COnectar no postgre pelo pgadmin


├── 123. Carga de Dados no Banco Relacional.mp4
+ Criar e popula o banco relacional

├── 124. Camada de Aquisição de Dados em Batch  Instalação Sqoop.mp4
├── 125. Configurando o Driver JDBC.mp4
├── 126. Testando a Configuração do Data Lake com o Banco Relacional.mp4
├── 127. Importando Dados do Banco Transacional Para o Data Lake.mp4
├── 128. Preparando o Ambiente Web Para o Data Lake e Agendando Jobs.mp4

### O que é o AWS RDS

BEm, para fazer o processamento em Batch precisamos de um DB estruturado, um banco de dados relacional **AMAZON RDS**.

De qualquer forma, você pode criar um local também

Com o RDS da amazon, há uma simplificação de tanta coisa, que está matando a profissão de DBA. POis dá para automatizar as tarefas de uma DBA

### Hadoop Sqoop

Criando a camada de aquisição de dados

O apache sqoop não é a.

**Instalar**

Vamos instalar o Sqoop no nameNode

+ Baixo wget por um url 
+ Descompacta
+ Renomeia e altera seu path
+ COloca as permissões
+ crescenta variáveis de ambiente

`sqoop helper`

O scoop nao vem drives, então vamos ter que baixá-los manualmente

**Observações**
+ O sqoop é para gerencia o Hadoop então, temos duas funções
+ IMportar dados de fora para o hadoop
+ Exportar dados do hadoop para algo de fora

**TroubleShooting: Usando Sqoop e AWS**

+ O InBOund default da AWS não permite acesso além da sua máquina. ENtão se você tenta acessar o banco de uma das instâncias EC2, vai dar erros, pois elas nao sao a sua máquina/net

**Comprando MapReduce e Sqoop**

+ O Sqoop faz apenas a parte do "MAP"

## PARTE 5 - Lab 2

Permite acessar o HDFS Via Browser

## PARTE 6 - Lab 3

Criar Jobs, para fazer a cargas e buscar os dados de noite automaticamente com sqoop









