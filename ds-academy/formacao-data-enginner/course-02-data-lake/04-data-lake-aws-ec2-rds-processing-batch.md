# Data Lake  - AWS EC2 - Processando Batch

## Resumo

## Links

## PARTE 1 -INTRODUÇAO E TEOIRIA

### Intro

Vamos construir um DataLake na AWS durante 5 capítulos, próximo do mundo real. E no fim, há o DatLake Servelss onde você cria o datalake sem especificar a infra.

img-c2-5-01

### Aquisiçâod e Dados

É a porta de entrada do nosso datalake.

Vamos trabalhar com DFS e Sccop: Que permite conectar a bancos relacionais e levar para a HDFS e vice-verça

**HDFS** e  **Apaceh Scoop**

### O que são dados em Batch

É o ETL do Pentaho

img-c2-5-06 (2, a 6)

## Real-Time x Batch Data

img-c2-5-07

O REal time é oprocessamento na hora, enquanto que o Bathc esepra um tempo para fazer (em geral, faz de noite a carga)

## Mapeando os dados do nosos projeto

Este é um schema conceitual

img-c2-5-08

RMDS : Banco RElacional
Sccop: Pega os dados do banco relacional (Ferramente de ETL)
Haddop: Implementa o HDFS nosos storage

Os dados de strremin vamos pegar com o APache FLume e Kafaka (iremos ver isos no ppróximocapítulo_

## PARTE 2 - APACHE SQOOP

## O que é Apache Sccop

Ferramenta para levar dados de banco de dados esturutados para o Haddop. 

Usaremos uma lingaugem SQL para acessar e pegar os dados do RMDS.

Usaremos o Sqoop v1 1.4.7: Ele é mais simples

### IMport/Export com Sqoop/Haddop

**Import**
+ EU conecto o scocop ao RMDS
+ Eu posso pegar parte dos daods ou todo ele
img-c2-5-09

**Export**
img-c2-5-10

### COnectores Sqoop

Antes de começar o Sqoop, verifique  na sua documentaçâo se ele tem conectrores para o seu banco de dados.

Usaremos o PostGreSQL

## PARTE 3 - MONTANTO EC2 NA AWS

### Start DataLake na AWS

Essa aula explica
+ No primeiros 4 minutos, o motivo de ser melhor criar em nuvem
+ Profissional: A AWS é a maior do market-share, por ser lider, ela disponibiliza varios certificados.

ESTE NÃO É UM CURSO DE AWS

### Como monetizar o DataLake em Nuvem

Há 3 profissionais:

+ Funcionario:
+ Consultor:
+ Empreendedor:

**A área de BIg Data, ML oferece a grande vantagem de permitier que voce empreenda, pois nao é todo mundo que usa isso. E boa parte das ferramentas sâo open-source, free**


**O INSTRUTOR TEM VARIAS CONTA NA AWS, ONDE TEM DW, ML, BIG DATA E OFERECE AO CLIENTE COMO PRIDUTO**

**Muitas empresa nao tem como ter um time de TI só pra fazer isso, se voce pode fazer dirto para lea e entregar como produto,fic amuito bom**

**COMO MONETIZAR COM DATA LAKE**

+ Voce pode vender toda a estrutura de DataLake como um produto.
+ Crie um web-site oferencedo isso: armazneamneto, procesasmento e combra dele por gigaByte, teraByte

Outro exemplo:
+ Criar ua ferramenta para captura de dados nao-estruturados e vender isso par ao cliente 

**HOJE, FALSE MUITO DE ML, MAS NAO DA PRA FAZER ML SEM TER DADOS BEM MODELADOS, ESSA É UMA ARE QUE ESTÁ CRESCENDO: DATA ENGERIING**

### Conta AWS

VIXI:

PARA IMPLEMENTAR AS COISA DAS AULAS, SERÁ NECESSÁRIO USAR SERVIÇOES PAGAOS. TANTO É QUE VÂ OFERECRER R$ 100,00 para reembolso por ter que gastar dinheiro na EC2.

Com R$10,,0 voce caonsegue fazezr esse e os proximos capitulos 2 vezes

### AWS EC2

ElascticCloundComputer

Ele disponibiliza capacidade computacional.

O EC2 pode ser usadao gratuitamente, 750h mas para uma instancia com apenas 1GB de RAM, Isso limita agente para fazer um Haddop.

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

### PART 4 - 

**Vou escrever e tirar print das principais partes, par alemrbar e nao ficarm somente como HD**




├── 107. Implementação do Data Lake em Nuvem  Provisionando as Instâncias EC2  NameNode.mp4
+ Criar na WAS a instancia com NameNode

├── 108. Implementação do Data Lake em Nuvem  Provisionando as Instâncias EC2  DataNodes.mp4
+ Criar na WAS a instancia com DataNode

├── 110. Implementação do Data Lake em Nuvem  Conectando nas Instâncias EC2 via SSH.mp4
+ Ttera que abrir em 2 instancias do Putty para concetcat
+ Conectados com a chave particular da AWS
+ OBS: As inscnaica do EC2 podem ser copiadas, entao, depois de criada, voce pod cuplicar os DataNOde

├── 111. Implementação do Data Lake em Nuvem  Criando Usuário de Configuração.mp4
+ Primeiro, temos que encontrar o endereço DNS público e privado
+ OBS: configuraçoes de rede da AWS podem ser alteradas, peloa ROuteS3, mas é pago
+ O que faz: Cria-se usuários sudo específicos para o haddop nas inatnaicas

````
Criando usuário hadoop (nos 3 servidores do cluster)

sudo useradd -m hadoop
sudo passwd hadoop (datalake9182)

Obs: Inclua o usuário hadoop no arquivo /etc/sudoers
````

├── 112. Implementação do Data Lake em Nuvem  Instalando o Java JDK nas Máquinas do Cluster.mp4
+ Instalar JDK nas 3 máquinas
+ para acessar o usuário habop `su haddop`
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
+ Para uma máquina se ligar a outra semm precisar de senha, vamos criar uma conexao SSH

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

COntinauaçao do anterior


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

Aqui usamos DNS privados, entoa, se voce implementar, vai ter que olhar o seu EC2

├── 118. Implementação do Data Lake em Nuvem  Configuração do Hadoop nos Nodes Slaves.mp4

+ **MUITO INTERRESSANTE**: Como esass máquina vao ser ligadas e fizmeos um SSH sem senha: **EU COPIO DE UMA PASTA A OUTRA TODO O DIRETÓRIO HADDOP: DA MASTER PAR AO SLAVE**

├── 119. Implementação do Data Lake em Nuvem  Inicializando e Testando o Cluster na Nuvem.mp4

+ Formatar o namenode 
+ Depois suobe, inicializa o HDFSS

**NO FIMNAL, COM O HADDOP SUBIDO, ELE OFERECE UMA PAGINA WERB PARA VSIUALIZAR**, ELEA É NA PORTA 9870 




├── 120. O Que é Amazon AWS RDS.mp4
+ Amaozn RDS é o banco relacional da Amaozn: POde ser: AuroraDb (é um mysql/psotregre modificado pela amzon), MySQL, PostGre, SQLServer, MariaDB
+ É fácil criar, rapidinho


├── 121. Preparando o Banco de Dados Transacional com PostgreSQL.mp4
+ Procure o pgAdmin para concetatr no posgree
+ O **CLIENTE ABRE NO BROWSER**
  - Clique em Serve e coloca as coisas


├── 122. Conectando Remotamente no Banco de Dados.mp4
+ COnectar no postgre pelo pgadmin


├── 123. Carga de Dados no Banco Relacional.mp4
+ Criar e popula o banco relacional

├── 124. Camada de Aquisição de Dados em Batch  Instalação Sqoop.mp4
├── 125. Configurando o Driver JDBC.mp4
├── 126. Testando a Configuração do Data Lake com o Banco Relacional.mp4
├── 127. Importando Dados do Banco Transacional Para o Data Lake.mp4
├── 128. Preparando o Ambiente Web Para o Data Lake e Agendando Jobs.mp4

## O que é o AWS RDS

BEm, para fazer o procesasmento em Batch precisamos de um DB estrutuardo, uma bnaoc de dados relacionalo **AMAZON RDS**.

De qualquer forma, voce pode criar um local tambem

Com o RDS da amaozn, há uma simplificaçAe tanta coisa, que ta matando a profissoa de DBA. POis dá para automatizar as tarfeas de uma DBA

## Haddop Sqoop

Criando a camad de aquisiçâo de dados

O apache sqoop nao é a.

**Instalar**

Vamos instalar o Sccop no nameNode

+ Baixo wget papor um url 
+ Descompacta
+ Renomeia e altera seu path
+ COloca as permisoes
+ crescenta varaivesi de ambiente

`sccop helper`

O sccop nao vem drives, entoa vaos ter que baixalos manualemnte

**Observaçoes**
+ O sccop é para genrencia o Haddop entao, temos duas funçoes
+ IMportar dados de fora par ao haddop
+ Exportar dados do haddop para algo de fora

**TroubleSHotting: Usando Sccop e AWS**
+ O InBOund default da AWS nao permite acesso alem da sua maquina. ENtao se voce tentea acessar o banco de uma das instancias EC2, vai dar erros, pois elas nao sao a sua máquina/net

**COmprando MapREcuce e Sccop**
+ O Sccop faz apenas a parte do "MAP"

## Lab 2

Permite acessar o HDFS Via Browser

## Lab 3

Criar JObs, para fazer a cargas e buscar os dados de noite.







https://cdn-videos.lpsg.com/data/photos/s/9432/9432701-1637899893-ff61ec5ec705f2ef36311ee9cf5a0f14.jpg
https://cdn-videos.lpsg.com/data/photos/s/9432/9432731-1637899902-6b9287820a24de7e9c53eeb1f4aff498.jpg
