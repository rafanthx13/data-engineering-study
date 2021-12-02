# ML em Larga Escala - Parte 1

## Resumo

Crair Cluster, Instalar spark /(masteNode e workNodes); Teoria do que é escalbildaide e larga-escala


## PARTE 1 - Teoiria de ML em Larga Escala e Spark

### Reumo do que vamos fazer no próximos caps

+ Executar um modelo de ML em Produção
+ Estudar ML
+ Como chamar o modelo

Sâo 4 modulo,studo em larga escala
+ Modulo 2 - Apache Spark 1
+ Modulo 3 - Apache Spark 2
+ Modulo 4 - ML em Stream e Grafos
+ Modulo 5 - Deep Learning

**O que é ML em larga escala**

img-c4-02-01

## Compreendendo Problema e Dados para ML

ML nâo é soluçâo para todos os problemas. É necessário especificar qual problema quer resolver

img-c4-02-02

**Dicas para valair se ML é asolução**

1 - Ao começar em ML, tente resolver um rpoblema real da empresa ou das pessoas

2 - É necessário ter o contexto do problema de negócio. Nâo importa  se tecnicamente eé bem feito, mas se a sua soluçâo nao traz calramente os benefícios apra a empresa, se resolve ou nâo problema, ninguem vai ligar.

3 - Espere para altera/ajustar até encontrar algum ROI. Ou seja, depois de pronto é bem capaz que tenha que mudar alguma coisa, entao, é necessaŕio fazer alguns ajustes

## O que é escalabildiade

img-c4-02-03

escalabilidade: capacidade de crescer o seu sistema ao lngo do tempo.

**Escalabildiade horizontal**
+ scale out/in
+ Significa adicionar mais máquinas ao seu ambiente


**Escalabilidade Vertical**
+ Adicionar mais recursos em uma única máquina
+ Seria adicionar mais memoria/ram/cpu

## O que é uma APp em alrga escala

As susaa acracteris tica sao

+ É ser um cluster: ou seja, envolve mais de uma máquina
+ Escalável
+ Alta Perfomance
+ ALta Disponibilidade (24/7)
+ Arquitetura MOderna de MicroService
  - Pois podemos escalar apenas a parte que queremos

## O que é Apache Spark

Difernte de todos os outros curso,s aqui **VAMOS TRABALHAR COM SPARK EM AMBIENTE DE MULTI-NODE CLUSTER**

O Spark é um a tool para processar dados de forma distribuida em Ram. O apache Haddop HDFS é apra armaznear de forma distribuida. E o MapREduce é o processamento mas ssobre Sotorage

O Spark funcione junto do Haddop.

### PARTE 2 - Apache Spark : configurarando cluster multi-node

**O que vamos fazer**
+ Cluster de 3 máquinas; instalar e configurar apache spark; processar (feature engering, pipileine de dados, executar ML)

├── 33. Configurando Um Multinode Cluster Spark  Parte 1.9.mp4
+ Virtual Box (3 virtual box CentOS - DVD ISO)
+ Instalar Java 1.8

├── 34. Configurando Um Multinode Cluster Spark  Parte 2.9.mp4
+ rqutitetrua do Spark
+ Mais conf de virtual box

img-c4-02-04

├── 35. Configurando Um Multinode Cluster Spark  Parte 3.9.mp4
+ Fazer Virutla nas 3 maquinas


````
==> Instalação Spark

=> Instalando e Configurando o Java JDK (nos 3 servidores do cluster)

=> Acessa o diretório
cd /opt/

=> Instala o wget
sudo yum install wget

=> Faz o download
wget http://datascienceacademy.com.br/blog/aluno/JDK/jdk-8u181-linux-x64.tar.gz

=> Descompacta o arquivo
tar xzf jdk-8u181-linux-x64.tar.gz

=> Verifica a versão
java -version
sudo mv jdk1.8 /opt/jdk

=> Configurando as variáveis de ambiente

vi .bash_profile

=> Java JDK 1.8
export JAVA_HOME=/opt/jdk
export JRE_HOME=/opt/jdk/jre
export PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin

source .bash_profile

java -version


=> Atualiza o SO
sudo yum update
````

├── 36. Configurando Um Multinode Cluster Spark  Parte 4.9.mp4
+ Vamos certificar se as 3 máquinas consegue se comunicar entre si

````

````
=> usa o caoando a seguri para buscar ip
% ip addr

=> faz ping
% ping 172.6......

=> inserir enderços, atalho
% sudo vi /etc/hosts

inserio 172.20.10.8 master
inserio 172.20.10.9 node1
inserio 172.20.10.10 node2

````

E faz isso nas outras maquinas. Isso é para que eles se comuniquem de forma mais fácil, pro nome





├── 37. Configurando Um Multinode Cluster Spark  Parte 5.9.mp4



├── 38. Configurando Um Multinode Cluster Spark  Parte 6.9.mp4

+ Criando SH sem senha
+ CHeka se tem ssh (ver o comando no video que espliaca com instalr)
  -Por default, o CentOS já vem no OS
+ Na msatesr cria a PrivateKey
  - `ssh-keygen -t rsa -P ""`
+ vai criar `id_rsa` e `id_rsa.pub`
+ Vamos cpiar a pub para as outra maquinas

% cat id_rsa.pub > authorozed_keys
  _ É pra master tambem ter acessao a esas chave publica

+ Fazne copia da master para node 1
+ `scp authorized_keys aluno@node1:/home/aluno/.ssh
  - Eu copia o autrohrized _keys; infroma a senha do node1

+ testnado a conexao ssh sem senha
+ `ssh node1`
  -Deu problema, pediu senha

├── 39. Configurando Um Multinode Cluster Spark  Parte 7.9.mp4
+ POruqe deu problema na node2, mas nao deu na node1
+ O problema é o privilégio do ndoe2. Ese problema foi criado porque eu creiei esse diretório manulamente, **O RPOBELMA É QUE A PERMISAO DO DIRETORIO SSH DEVE SER DE UM TIPO ESPECÍFICO**
+ Fanzeod a minha maquina ao node2 que está na virtual box `ssh -vvv aluno@node2`

├── 40. Configurando Um Multinode Cluster Spark  Parte 8.9.mp4
+ INstlar o apache SPARK 2.3.2 (setembro de 2018)
+ Descompacta; mude variavel de ambiente
+ teste com % sapark-shell


├── 41. Configurando Um Multinode Cluster Spark  Parte 9.9.mp4
+ copiamos spark-env.sh sem o 'template'
+ copiando slaves tambem
  - slaves indica quem sao os wokers: no caso, vamos por node1 e node2
+ INicializa o spark em
 `/sbin/start-all.sh` somente na master e as 
  - Roda em 2 plano
+ Se u eu digito `jps` deve mostra o processo
+ SPARK NAO DEPENDE DO HADDOP. Posso aponta o Spark paara apontar para um S3 ou Sistema de Arqvios local

+ % spark-shel
  

