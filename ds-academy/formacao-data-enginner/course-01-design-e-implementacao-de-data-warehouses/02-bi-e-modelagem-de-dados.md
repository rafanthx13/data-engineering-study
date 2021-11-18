# Bi e Modelagem de Dados

## Links

Design e Implementação de Data Warehouses
Bibliografia, Referências e Links úteis


The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling
https://www.amazon.com.br/Data-Warehouse-Toolkit-Definitive-Dimensional-ebook/dp/B00DRZX6XS/ref=sr_1_2?ie=UTF8&qid=1521159195&sr=8-2&keywords=kimball

Business Intelligence Gartner Group
https://www.gartner.com/it-glossary/business-intelligence-bi/

10 differences between Data Science and Business Intelligence
https://www.itproportal.com/2016/08/18/10-differences-between-data-science-and-business-intelligence/

ERWin
https://erwin.com/

## O que é BI

Termo generico que inclui apps, ferramentas e melhores praticas para acesso e analise de informaçoes para tomada de decisao.
+ BI permite organizar ae analizar informaçoes que servem como suporte para otmada de decisao

## Ferramentas de Bi e de DS

A difenreça entre ambos já vimos no cap anterior

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-2-1.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-2-2.png)

No DW já tem dados esttruturadps

No Data Lake, nâo está nada estreuturado, a limpeza é feito de acrodo com o procesos que vou realizar. 
+ Se eu tentar fazer uma limpeza no DataLake,e ficaria inviável

## Fases e Desgin de um DW

O prblema: Há muitas implicaçẽs de negócio

É necessaŕio verificar as seguintes queestôes:
+ Diferentes tipos de dados (int, string, padrao de string)
+ Formas de usar esse DW
 - Vai ser muito centralizado ou mais dividio em DataMart
+ Fromas de estruturar os dados
  - Nem sempre a fonte do DW pode ser um dado estruturado. ENtao, como estruturar quando isso acontece
+ REplicaçâo, Particionamento, Carga de Dados

E é claro, apos definir tudo, é complicado mudar tudo depois

**EM UM DW há 4 fases**

1. modelo de negocio (defineri o que vai resolver)
+ Define o seu objetivo. Vai olahr para os problemas da empres,a idenitificalos e propor soluçôes
+ Se negligenciar essa etapa, vai afetar tudo oq ue tiver a seguir

2. modelo logico (entidade relacionamento)
+ É idetificar as tabelas entidade relacionamento

3. modelo dimensional (dimensao fato)
+ Só é criado a aprtir do modelo de negociio. É orientado ao model de negocio

4. modelo fisico (criar o banco)
+ AWS REdSHifht ou Oracle

## Definido modelo de negócio

Há 3 sub-eataps

+ Análise Estratégica
 - Identificar processo de negócio críticos. Em geral quem faz isso é o analista de negócios
 - Compreender bem esses processos
 - Priorizar os processos
  - COmo fazer tudo isso: Conversa com stake holders

+ Criaçâo do modelo de negócio
  - Definir os requerimentos de negócio 
    * Ou seja, definir o que sâo os relacionamentos e  que será as dimensões
  - Determinar a granularidade (o nível de detalhamento: hora, minuto, segundos)
   * Impacta na perfomance do BD
   * Isso vai impcatar, pois, nao consegurire fazer menos do que aquilo que detemrinar
  - Determinar os Metdados
    * Tudo que nos ajuda a identificar os dados (nome da tabela, nome da coluna)

+ Documentaçâo dos MetaDados
  - Documentar tudo
  - Documentar Mudanças
  - Registrar melhoraias ao longo do tempo

**O que tenho que entregar nessa etapa**
+ Identificar Dimensoes e Medidas
+ Identificar granularidade
  - Lembre-se, se tiver muito detalhe, vai ficar mais lempo
+ Identificar os metadados e asim criar um meta-data-dictionary

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-2-3.png)

É estabelecer dimensoes que atendam diversos processao da empresa

## Modelo Logisco e DImensional

O logico sera estudado no cap 3 (OLTP)

o dimensional no cap 4 (OLAP)

A difenreça é que no DW estará mais desnormalizado

## Formas do Modelo Dimensional

Esquemas de modelos DImensionais

StaSchema, SnowFlake, 3 forma normal (3NF)

**Essa é a difenreça do DataLake, o DataLake nao tem forma**


3 forma normal (3NF)
+ Alto nível de normalizaçâo

StarSchema
+ MOdelo bem desnormalizado, pois o que voce se preocupa é olhar para a tabela Fato
+ É o mais fácil de compreender. Tem o fato que fica no meio e em volta as dimensoes

SnowFlake
+ Parecido com o StarSchema mas que tambem tem algum nivel de normlalizçÂo, entao, tem mais tabelas que o StarSchema

**O que é normalizaçoa em banco de dados**
+ É voce divir uma tabela em duas

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-2-4.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-2-5.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-2-6.png)

## Tabela Fato e DImensao

Tabela Fato: Tem as FK que relaciona com as PK das DImensoes
+ É a tabela com maior volume de dados e que vai mais crescer
+ EU posso fazer já fazea multiplicaçao de colunes: ex, se na venda tenho quantiade e valor, no DW, já posso por assim o lucro total

Tabela Dimensao
+ Dados mais sttciso, entao, esle nao vao m udar
+ Infromaçoes com nivel de musança muito baixo
+ Ex: Produto (o nome nao deve mudar)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-2-7.png)



## Definido Modelo Físico

Traduzir para o modelo dimensional para o  banco de addos reais

Saô coisas como:
+ Determinar a arquitetura, Particionamento, Indexaçao, Segurnaça, Codigo DDL, Definir os MetaDados, Sizing (tamanho do BD)


![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-2-8.png)
