# Data Lake: Deploy, RollOut e Boas Práticas

## Links

Apache Ambari
https://ambari.apache.org/

15 Best Cluster Managements
https://siftery.com/categories/devops/cluster-management

Cloudera Manager
https://www.cloudera.com/downloads/manager/5-9-0.html

Ganglia
http://ganglia.sourceforge.net/

Nagios
https://www.nagios.org/

Erro no Deploy do Apache Ambari
https://community.hortonworks.com/questions/109996/hdp-26-requires-libtirpc-devel.html

## PARTE 1 - Cloud and Hadoop Management

### Introdução

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-9-01.png)

**OU SEJA, AO INVÉS DE TER QUE FAZER TUDO NA LINHA DE COMANDO TODA VEZ QUE VAI SUBIR UM CLUSTER  HADOOP, FAZER A APARTIR DE NUMA INTERFACE WEB**

Passamos pelo processo manual para aprender a fazer mesmo na mão.

Agora, vamos usar Apache Ambari, desenvolvido pela hortnwork que faz isso automático.

### O que será feito nesse capítulo

Vamos criar um cluster hadoop e fazer o seu deploy via Apache Ambari, ou seja via wizard step-by-step

### O que é Apache Ambari

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-9-02.png)

O ambari serve para subir hadoop e seus apps, ver as versões e monitorar as aplicações.

Ele é um ferramenta de gerenciamento e deploy. Exemplo da sua tela:

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-9-03.png)

**Features**

+ Você pode adicionar novos cluster ao hdfs e monitorar os aps como na imagem acima
+ OpenSource
+ Monitora não só o haddop quanto as aplicaçôes do sistema haddop (spark,kafka,sqoop)
+ É possível configurar as variáveis direto no Ambari, oq ue evitar acessar cada máquina

### Outras soluções de Cloud/Hadoop management

**Cluster Management**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-9-04.png)

**Hadoop Management**

+ Apache Ambari

+ Ganglia 

+ Nagios

### Arquitetura do Ambari


arquitetura do apache ambari

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-9-05.png)

+ Temos um REST CLIENTE, ou seja, uma interface web que se liga ao banco de dados postgres (ele mesmo vai fazer isso automaticamente,se quiser, você pode configurar para outro banco ou o seu próprio postgres)

Vamos instalar o ambari na Master, ele vai então instalar Agent em cada Nó e assim, fica se conectando ao nó principal do ambari além de mandar métricas.

OBS: O nó principal do ambari não precisa ser o mesmo nó principal do hadoop. Pois, O AMBARI CONSOME BASTANTE MEMÓRIA

Como instalar os agentes em cada node?

=> SSH sem senha: na master vamos gerar 2 chaves, uma pública e privada. Vamos mandar a chave pública para os DataNode,pois essa conexão é somente de uma via, do master para os datanode

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-9-06.png)



## PARTE 2 - Instalar Ambari

├── 283. Deploy do Data Lake  Provisionando os Servidores e Sistema Operacional. 
+ Cria outras 5 AWS EC2 Para fazer isso. Pois o nosso cluster já está devidamente configurado

+ Será 5 EC2: Uma será Master Node do Hadoop, 3 Serão DataNode do Hadoop, e 1 será só para o Ambari, pois ele é um pouco pesado e vai precisar se dedicar para fazer o monitoramento e deploy do cluster

  

├── 284. Deploy do Data Lake  Matriz de Suporte e Documentação. 
+ O ambari tem a documentação da hortonWorks
+ E lá procuramos como instalar o apache ambari



├── 285. Deploy do Data Lake  Configurando SSH Sem Senha. 
+ ssh-keygen: gerar chave pública e privada
+ copia a chave pública para as outras máquinas




├── 286. Deploy do Data Lake  Instalando o Apache Ambari. 
+ instalar o ambari-server, e baixe também o postgres se não tiver



├── 287. Deploy do Data Lake  Configurando o Apache Ambari. 
+ configurar o ambari
+ ele faz uma série de perguntas e aí você responde
+ user e senha são admin, na porta 8080




├── 288. Deploy do Data Lake  Deploy do Cluster  Parte 1.3. 
+ Vai mostra uma wizard step-by-step para instalar as coisas do hadoop em outras máquinas 
+ faz mais configurações para ligar a MasterAmbari com dataNode Ambari




├── 289. Deploy do Data Lake  Deploy do Cluster  Parte 2.3. 
+ Escolhemos os serviços para nosso clusters
+ ei posso escolher qual Node será master/slave para cada uma das máquinas
+ abre a parte de configuração para cada app
+ o deploy demora muito: 15min




├── 290. Deploy do Data Lake Troubleshooting. 
+ resolvendo o erro no deploy com o ambari
+ precisava instalar uma lib
+ instale o pacote em todas as máquinas



├── 291. Deploy do Data Lake  Deploy do Cluster  Parte 3.3. 
+ Mostra a dashboard, e coletar as métricas




├── 292. Deploy do Data Lake Dashboard de Monitoramento e Gestão do Cluster HDFS  Parte 1.2. 
+ vendo as dashboard e explorando o ambari



├── 293. Deploy do Data Lake Dashboard de Monitoramento e Gestão do Cluster HDFS  Parte 2.2. 



## PARTE 3 - Após Deploy do Data Lake

### RollOut e SysOps

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-9-07.png)

Mesmo no ambari, a gente fez muita coisa ainda. Depois de pronto, qual o próximo passo.

RollOut: Passagem de bastão do ambiente para equipe de suporte: SysOps

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-9-08.png)

Existe uma certificação da AWS de SysOPS

SysOps: Operador de sistema, e alguém pra tratar de erros e bizarrices no sistema.


### Precisamos de uma sandbox

SANDBOX: ambiente de teste, sem pôr em ambiente real.

É interessante ter um cluster pequeno para testar algumas coisas. Ou pelo menos um Pseudo Cluster (com bastante memória pois vai rodar muita coisa na RAM).

Cloudera e HortonWorks oferecem SandBox

Á máquina virtual tem 15Gb, onde já está tudo instalado

HortonWorks HDP. Use o VIrtual Box e acesse do seu local host : 1080; usuário

user/senha da HDP: raj_ops ou maria_dev

Ai você usa e abre o ambari, e ver tudo que já está instalado.

Leva muito tempo para inicializar tudo da sandbox, quando você abrir a sandbox pela primeira vez



