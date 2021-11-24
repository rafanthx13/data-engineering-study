# O que é DataLake


## Intro

Alinhar a termonologia, arquitetura e como é o conteiode um datalake

O datalake é um conceito apra uma estrategia central de gestâo de dados: **É UM RESPOSITÓRIO DE DADOS**, Como se fosse um bloco único (Singel Customer View)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-01.png)

SOmente com um grande volume dae dados é possivel fazr IA, que é nada mais que estatístaca 

## Conceito de DataLake

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-02.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-03.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-04.png)


Principias conceitos
+ ddso brutos: ou seja nao estruturadaso entra tambe
+ repositorio: tem uma série de coisas la dentro
+ processar, analisa e entregar resultados (Machine Laerning e BI)

## Vantagens e Desvantagens

Se a emrpesa nao tem uma cultura orientada a dados, esquece datalake.

Beneficios

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-05.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-06.png)

Desvantagesn

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-08.png)

## Arquitetura do DataLake

Há duas formas de lahar o datalak

Olhando por serviços que ela oferece

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-09.png)

Vamoe estaudar coada uma

A estrutura final fica da seuinte forma

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-11.png)

### Aquisiçâo de dados

Nâo dá para pegar todo e qualquer dados, eu preciso de um objetivo.

**TENHO QUE ORIENTAR A EMRPSA A USAR O DATALAKE ORIENTADAO A UM OBJETIVO. NAO É EPGAR QUALQUER COISA E VIRRA UM DATA SWAMP**. É claro, pode ser que os objetivo mude com o tempo, mas deve sempre haver

### Procesamento de dados

A tecnica para processar esse dados depende do que voce vai fazer com ele. Nâo é qualquer técnica. É uma soluçao de negócio

Aqui é quando aplicamos o T do ETL.

### Análise de Dados

Feerramentas de BI, ML, IA.

### Armazenemaneto

Os dados podem ou nao ficar no DataLkae apos serem usadasos

### Qualidade e ciclo de vida dos dados

**Qualidade**

Aqualidade é algo improtante durante todo o processo. Se vinher lixo, vai sair lixo. 

Podemos criar algum filtro, etl, limpeza de ddos e estcc.

Ex: Se voce pega dados de rede social voce vai precisar dos emojis? se nao ja filtra; Se voce for pegar datas, porque nao formatar elas; Transforme-as

**Ciclo de Vida**

Baseada na palestra encontrda no link abaixo

https://www.youtube.com/watch?v=bTRNkouGO-Q

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-12.png)

CIclo de vida de uma arquitetura agil dos dados:
+ começa em 'logical data lake"

**Reasista a aula para enternder melhor o ciclo de vida dos dados**

## Quais plataformas usamos para construir DataLake

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-13.png)

=> 1. COleta, 2. Ingestao (quando relamente inserimos em algum lugar no repositorio); 3. Bledn (mistura das varais fontes); 4. Tranforma eles, Puplica e os usa em distribute

Para etapa 2: INGEST
+ Usamos ou (Hadoop + Spark) ou soluçao prpria da AWS ou Azure
 - Haddop nao é concorrente do Spark, por isso, podem ser usados juntos. O MapREduce é um processametno em disco, enquanto que o Spark é o processamento em memória, por isso da pra usar os 2 juntos
+ Outras opçoes
  - Um banco NoSQL
  - DataStore (O AWS S3 é um exemplo, um repositorio que pdoe ser usado para ser um datalake)
+ VOce nâo copoe um DataLka ecom um banco relacional (pois foram criados par adaod ssomente estruturadsos)


## Data Lame Management Software

A seguri tem a 'kylo plataform', uam statrupque tem um modelo de Datalake interressanete

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-14.png)

A Kylo é um prdouto e criaram uma gestâo de um datalake, uma arquitetura completa

Ela abstraiu as dificultadade de montar um datalake e sorgiu entao um produto.

**É ISSO QUE FAZ A DIFENREÇA ENTER UM PRODUTO/SERVIÇO**

Ela resolveu o rpblema que é : como maontar um datalake já que parece ser uma sopa de letrinhas?

E tudo isso com soluçâo OpenSource

**Busque resoolver um soluçao de negpocio**

## Como construir um datalake

Uma visao geral, como voce conseguiria construir um datalake.

Visao em camadas

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-16.png)

EM geralessa camaasd sao encontradas em todo datalae, mas boa parte sao bem opscionais, como a acamada de mensagens

### 1. Aquisiçao de dados

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-17.png)

Precismos de um conector que seja capaz de pegar diversos fontes de dados. É uma camada de transporte de dados, é possivel fazxer algum ETL mas é reocmendado que seja pouco, pois nao é a sua repsonsabildiade.

Em seguida viria a camada de mensagem.

O que acontece se der enrro entre elas? preciso ter algum sistema para nao perder esses dados.
+ Em geral, fica em um buffer local

Iremos ver 2 caps: buscar os dados em bathc (3) e em striemgin (4)


### 2.Camad de mensagens

cap5: apache kafka

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-18.png)

É o que cahamamos de middleware. Ela é muito usada quando voce temum sistema distribuido

É tambem chamado de MOM. A troca de mensagem é melhor do que compartilhar uma mesma memoria, pois assim OS SISTSEMAS/SO PODEM SER COMPLETAMENTE DIFERNTES ENTRE SI.

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-19.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-20.png)

O Kafka é extremamente excelente para fazer isso

### 3. Camad de Ingestâo de dados

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-21.png)

Receber as mensagen e levalas para processamento. Esstá junto do Kafka

Aqui já posso começar a pensar em aplicar o ETL

### 4. Camada de procesasmento

Dividia em duas partes: Batch Layer e Stream Layer (tambem chamada na literatura de Speed Layer)
+ Batche: MapReduce, pois prcessa em disco. O Spark nao consegue fazer isso com uma tonelada de arquivos
+ Stremaing: Spark, é muito mais desafiador e etc.

**OBS: Perceba que até o momento nao tem nada de armzaenemnto. O dalake é uma soluçao para gestao global e centrla dos dados**

### 5. Camada de Armaznemanto

A camada que sim, armaqenz os dados.

Paralela a camad de procesamsento, pois a origem e destino deses processamento é nessa camdada

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-02-data-lake/imgs/img-c2-2-22.png)

## Bonus  Roadmap Para um Data Lake de Sucesso

	As empresas hoje estão explodindo de dados, incluindo dados das bases
existentes, outputs de aplicativos, dados de streaming de comércio eletrônico,
mídia social, aplicativos e dispositivos conectados na Internet das Coisas (IoT).

	Estamos todos bem versados no Data Warehouse, projetado para capturar
a essência do negócio de outros sistemas empresariais, como sistemas ERP e
CRM, estoque e transações de vendas que permitem que analistas e usuários de
negócios obtenham insights e façam importantes decisões de negócios a partir
desses dados.

	Mas novas tecnologias, incluindo plataformas móveis, sociais e IoT, estão
impulsionando volumes de dados muito maiores, maiores expectativas dos
usuários e uma rápida globalização das economias.

	As organizações estão percebendo que as tecnologias tradicionais não
podem atender às novas necessidades de negócios.

	Como resultado, muitas organizações estão se voltando para arquiteturas
de scale-out, como Data Lakes, usando o Apache Hadoop e outras tecnologias de
Big Data. No entanto, apesar do crescente investimento em Data Lakes e
tecnologia de Big Data - US $ 150,8 bilhões em 2017, um aumento de 12,4% em
relação a 2016 - apenas 14% das organizações relatam implementar seu projeto
de prova de conceito (PoC) de Big Data, em produção.

	Uma razão para essa discrepância é que muitas organizações não veem um
retorno do seu investimento inicial em tecnologia e infraestrutura de Big Data.
Isso geralmente é porque essas organizações falham em fazer a coisa certa,
ficando aquém quando se trata de projetar os dados corretamente. Em (muitos)
outros casos, não há uma cultura data-driven.

	Em última análise, essas organizações criam "pântanos" de dados (Data
Swamps) que são realmente úteis apenas em casos de uso exploratório ad-hoc
(algo ainda incomum em muitas empresas, embora seja utilizado em pesquisa e
desenvolvimento). Para as organizações que se movem para além de uma PoC,
muitas estão unindo a flexibilidade de um Data Lake com boas práticas da
governança e controle de dados. Essa é a chave para obter um ROI significativo
dos investimentos de tecnologia para Big Data.

	Se você (Engenheiro de Dados) perguntar aos seus Analistas e Cientistas de
Dados quais dados eles querem usar no futuro eles provavelmente dirão "Tudo
que estiver disponível". Mas realmente precisamos de todos os dados possíveis
ou apenas do que é relevante para resolver determinado problema de negócio?
Em geral, usamos o Data Lake para armazenar:

	• Dados transacionais brutos
	• Dados semi-estruturados e não estruturados
	• Streaming de dados
	• Dados históricos que não foram migrados para os sistemas de produção
	• Dados que podem ser úteis para análises no futuro
	
	Data Lakes tornam-se pântanos de dados se não são gerenciados
corretamente. Certifique-se de que seu Data Lake possui as seguintes
características:

	• Arquitetura para atender às metas de negócio da empresa
	• Gerenciamento para proteger os dados
	• Integração para ser alimentado com dados de diferentes fontes
	• Acessibilidade para “self-service” e oferecer aos Cientistas de Dados a
	  oportunidade de aplicar Real-Time Analytics
	
	O Roadmap de sucesso para um Data Lake, deve contemplar:

1. Amplas capacidades analíticas
	• Fontes variadas de dados
	• Acesso a partir de diferentes ferramentas analíticas
	• Computação intensa para a execução de algoritmos de Machine
	  Learning

2. Interoperabilidade
	• Integração com diferentes sistemas heterogêneos
	• Processamento de eventos e mensagens

3. Continuidade do Negócio
	• Alta disponibilidade e tolerância a falhas
	• Disaster Recovery (Backup e Restore)
	• Data Recovery (recuperação contra falhas e corrupção nos dados

4. Custo Reduzido
	• Uso de hardware commodity (de baixo custo)
	• Baixo overhead de administração
	• Alta performance
	• Compartilhamento de recursos (virtualização)

5. Capacidades Multi-tenancy
	• Habilidade de gerenciar diversos recursos (computacionais) a partir de
	  um único ponto

	Conseguir reunir todas essas características em um Data Lake é muito
difícil, mas este deve ser o Roadmap e o objetivo de qualquer organização
interessada em obter o máximo do Big Data Analytics. E você, como Engenheiro
de Dados, é um dos responsáveis por isso.



Referências:

IDC. “Worldwide Semiannual Big Data & Analytics Spending Guide.”

Gartner. “Market Guide for Hadoop Distributions.”

Architecting Data Lakes (Free e-book)
https://www.oreilly.com/data/free/architecting-data-lakes.csp

Como Construir um Data Lake de Sucesso
https://mapr.com/resources/videos/how-build-successful-datalake/assets/how_to_build_a_successful_data_lake_webinar_-_160517.pdf
