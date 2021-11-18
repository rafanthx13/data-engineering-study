# DW na AWS RedShift

## Introdução

Duas parte:

1 -  DW RedShift 1

+ O que é AWS, Cloud, RedShift iniciar o DW

2 -  DW RedShift 2
+ Criar e interagir com o DW

Alinhando expectativas
+ Este não é um curso sobre AWS

Não há nenhum custo para a AWS para cadastro

De documentaçao, é apenas pela Amazon

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-11-1.png)

## Intro a AWS

AWS : Amazon Web Service
+ 1 ambiente em nuvem comercializado

A amazon RedShift é um dos 5 serviços que mais cresceram da amazon

## Amazon RedShift

Descriçâo do site 2021 - Amazon RedShift

+ Analise todos os seus dados com o data warehouse mais rápido e mais usado na nuvem
+ Analise todos os tipos de dados no seu data warehouse, banco de dados operacional e data lake. Use o SQL padrão para executar consultas e implantar modelos de machine learning (ML).
+ Compartilhe dados em tempo real dentro e fora da sua organização para melhorar a colaboração, isolar workloads críticas, acelerar o desenvolvimento e permitir insights em tempo real.
+ Obtenha uma performance de preço até 3x melhor e execute operações 10 vezes mais rápidas do que outros data warehouses corporativos com o AQUA (Advanced Query Accelerator).
+ Inicie um data warehouse em poucos minutos usando o gerenciamento de workload orientado por ML, otimizações de tabela e escalabilidade de simultaneidade para maximizar a performance e a taxa de transferência.

Se o cliente tem algo que impede o RedShift, ai você usa o Oracle.

## História do AWS RedShift

Amazon RedShift é na verdade uma versão modificada do PostgreSQL

Começou com a comrpa da AWS da empresa 'Paraccel', que desenvolveu uma versâo do PostgreSQL para processamento massivo de dados em DW

## Como as empresas estão usando o RedShift

A empresa Ahnagera, A editora Globo, Igreja Universal, Nubank

## RedShift Cluster

Na prática, tudo no RedShift é Cluster. Não há outra alternativa, tudo no RedShift é Cluster.

Um 'RedShift Cluster' é: Um leader Notde e um conjunto de Compute Node. **ESSE É O MESMO CONCEITO DE HADDOP**
+ Leader Node: Interaçâo com o cliente. Ele é quem distribui as ativiadas para os COmpute Nodes (Slaves)
+ Compute Node: Cada um é uma máquina com SO, CPU, Memory e Storage; Fazem a escalabildaide e sâo dedicados

**Slices**: Cada Compute Node tem *Slicess* subdivisoes que permite aumentar a capacidade de paralelimos

## Criando um Cluster RedShift

O 1 passo é criar um Cluster. Vamos criar somente um pois agente pode fazer isso na camada gratuita, e válido por 2 meses.

**Como criar**
+ Busque por "RedShift" e leia tudo, e então, você cria o Cluster

**O que diz sobre gratuito**

Experimente gratuitamente o Amazon RedShift por dois meses.
Se sua organização nunca criou um Cluster do Amazon RedShift, você está qualificado para testar gratuitamente nosso nó DC2.Large por dois meses.

Sua organização recebe 750 horas gratuitas por mês, suficientes para executar continuamente um nó DC2.Large com 160GB de armazenamento SSD compactado. Quando o teste gratuito de dois meses expirar ou a utilização exceder 750 horas por mês, você poderá encerrar o Cluster, evitando qualquer cobrança, ou mantê-lo em execução com nossa taxa sob demanda padrão.

**Como eu fiz para criar**
+ Selecionar free-trail e dar netx e inserir nome de identificador de Cluster e credenciais

**o susurro**
identify: rhavel-RedShift-Cluster-1
rhavel :: royal-Thunder_-_re7

Nova senha: royal-Thunder_-_re8

**credenciais**
Database name: dev, 
Admin user name: rhavel,
Admin user password: -.

**LEMBRE-SE DE DELTAR O Cluster APOS O PRJETO**

EndPoints: JDBC ou ODBC

utomaticamente a AWS faz o SNapshot, enfim, há varias coisas.

**Lembre-se nao altere nada da infra do Cluster**

## Usando o RedShift

O RedShift se conecta com todas as ferramentas de BI.

Mas, como queremos mandar coisas de Banco deaddos, temos que concetar com um CLiente de DB;

**Ele nao se conecta com o MySQLWorkBench**

A ferramenta usada é o SQLWorkBenchJ

https://www.sql-workbench.eu/downloads.html

Baixe o zip que vai ter para as duas versoes, linux (arquivo .sh) e windows (arquivo .exe)

## SQL WorchBench J

É ume xecútavae, mas que precisa do Java novo apra funcionar.

QUadno você conseguir abrir bastta abrir a conesoa como o MySQLWOrkbench

Na 1 vez, provavlemnte você nao vai conseguir conectar por time-out.

Isso ocorre por causa da VPC (Virtual Processing CLoud); ELa é criada quadno você cria algums erviço na AWS e precisa er habilitada 1 para poder relamente conectar **SEGURNAÇA**

Vá no ENDPOINT do Cluster e procure pelas configurançaoes de segurança (InBound e OutBound). 

Busque por "Editi inbou rules":
+ TIpo 'RedShift"/ Protocolo TCP; Src: Custom/ ANywhere

**ULTRA=====================================================**
**ULTRA=====================================================**
**ULTRA=====================================================**
**ULTRA=====================================================**
**ULTRA=====================================================**
**ULTRA=====================================================**
**ULTRA=====================================================**
**ULTRA=====================================================**

Consegui conectar nessa bosta.
+ Como tudo que é podre nesse mundo, ao conectar de primeira, fornecendo todos os parâmetros, vai dar problema
+ PORQU EÉ UMA BOSTA
+ Para conectar voce tem que ter feito 2 coisa que nem DEUS sabia que precisava
  - 1. Habilitar para acesso Externo
  - 2. Habilitar essa configuraçâo de inbound (entrada e saida) do VPC security Group

** Habilitar para acesso Externo**
+ ABSOLUTAMNETE NINGUEM FALA DISSO, MAS É UMA CONFIGURAÇÂO ANTERIOR A PÁGINA QUE VOCE VER OS DADOS DO SEU CLUSTER
+ NO MEU CASO FOI NA url: https://console.aws.amazon.com/redshiftv2/home?region=us-east-1#clusters
+ sELECIONA NO CLUSTER > ACTIONS > modify publicy acess settings
+ ESTA PORRA INCIA NAO ESTANDO DESABILITADA, ENTAO HABILITA

**INBOUD MALUCO**
+ Faça parecido com o do video, o meu ficou assim com a VPC que to usando:
sgr-039f68fe80c9ada7e	IPv4	Redshift	TCP	5439	0.0.0.0/0	–
sgr-0d2f469b44a32c033	IPv6	Redshift	TCP	5439	::/0	–

Ou seja, 2 regras de entras, as duas para RedShift para qualquer IPV4 e qualquer IPV6



## Precificação

Uma das tarefas mais desafiadoras, pois
+ você usa mais de um serviço da AWS
+ Cada um tem faixas e precificaçao difrente
+ Cada regiâo tem preçoes difernete

Tem uma calculadora para estimur, ai você coloca o quanto deve ser o seu gsato do dia

## Caracteristicas do RedShift

+ Query Otimization
+ Heurísticas e estatisticas internas (automatico)
+ ACID Compliance (Atomicidade, consistencia e durabildiade): sao as garantias de uma boa transação. Tem em todo banco Relacional
+ DATA DISTRIBUITION
  - Diferente de qualquer outro banco, aqui, os dados sao inseridos num ambiente distribuido (conjunto de maquinas que trabalham com se fossem uma)

## Como é feito o Cluster e a Distribution

O RedShif foi consrtruido para ser altamente-perfomático, isso por conta da Parrccel. Isso se deve aos 3 estilos de distribuiçao.

Quando você manda inserir algo no RedShift, vai para 1 ou mais nodes (Como no Haddop)

E na hora de consulta?
+ Pega os dados de várias máquinas

3 estilos de Distribuiçao
+ Even Distribution
+ Key Distribution
+ ALl Distribution

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-11-3.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-11-4.png)

Assim, podemos altera o estilo do RedShift para se adequar ao estilo do DW

Por default, usa-se o estilo **EVEN**

Para mudar para **Key** Basta indicar qual a colunas que vai ser a key adicionando no script SQL "distkey", na hora de criar a tabela.

ao ser criado você pode verificar pelo código abaixo.

**Nao é possívle mudar o estilo de distribuiçao apos criar a tabela**

## Armazenamento orientado a coluna

O RedShift é orientado a coluna **O QUE É COMPLETAMENTE DIFERETNE** do modelo relacional que é orientado a Row.

O que muda: Exemplo
+ Row: Ele carrega a linha inteira na coluna
+ Column: Armazena ascolunas em blocos distintos

então, por exmeplo, se você faz um Group by nesse modelo, vai muito mais rápido

Difenreça: Enquanto que na orientada a ROW, um group By agrupa e scanea vários colunas, no orientado a COLUMN, você consegue fazer isso para apenas aquela coluna.
+ Assim, operaçoes em uma unica coluna carrega somente o bloco daquela colunas (RedShift), enquanto que no modelo ROW, a alteraçao de umacoluna é ver todas as rows queela vai afeta (entidate-rlacionemnto)

**Isso é útil se você trabalha com DW, se quer sumarizar com GROUP BY**

Como o paradigma é difenrente, então:
+ Não há Cluster nem index
+ Por ser orientado a coluna, é MASSIVAMENTE PARALELA
+ Não deve ser usado para ambiente de CRUD (OLTP)



![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-11-6.png)

## Compressão de dados

Como ele olha uma coluna,e, muitas vezes, os dados de uma mesma coluna se repetem (exemplo, M/F) a  RedShift consegue reduzir bastante com COMPRESSÃO DE DADOS


![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-11-7.png)

**HOJE NÃO TEMOS UMA OPÇÃO TAO BOA QUANTO O RedShift para fazer DW**

## Documentação Oficial

Use o ambiente HTML pois é constantemente atualizado









