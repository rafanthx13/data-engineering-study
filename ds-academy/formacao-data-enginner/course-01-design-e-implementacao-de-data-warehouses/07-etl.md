# Extract, Transformation, Load (ETL)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-1.png)

## Introdução

Conceito de ETL: Coletar dados de uma fonte; Realizar alguma transformação e inserir num destino;

Complexidade: Existe muitas formas de fazer ETL, usando várias ferramentas, e entre muitas fontes/destino e entre diversos tipos de dados.

Operações:
+ 1. Extrair da fonte
+ 2. Por numa Staging Area 
+ 3. Transformar na Staging Area (ex: converter M/F para 1/0)
+ 4. Carregar no DW

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-2.png)

## O processo ETL

O que fazemos mesmo no ETL
+ Extrair (get os dados)
+ Limpeza (limpar os dados)
+ Consolidar e Reestruturar os dados
+ Ser capaz de dar Refresh e lidar com quaisquer erros durante o caminho

## Processo de Extração

Dados são extraídos de diversas fontes. 

É necessário criar rotina para extrair e considerar as regras de negócios e possível erros. Trilhas de auditoria.

### Examinar as fontes de dados

As empresa tem uma pilha e pilha de dados espalhados por vários lugares diferentes.

BackUps, Archives, Arquivos externos, planilhas excel e outras questões.

### Cuidados ao extrair da Produção

Em que horário e terei autorização para extrair os dados?

### Extrair dados históricos

O que é dados históricos? (Archive Data)
+ Para evitar que o banco em produção fique muito grande, coloca-se numa região mais distante chamada ARCHIVE.
+ Ex: Tirar os dados que tem mais de 5 anos, para deixar o banco e as consultas mais perfomáticas

### Dados Internos e Externos

E se eu quiser dados de fora, como dados governamentais par ajuntar ao meu DW? Ou por WebScraping?

### Possíveis técnicas para a Extração

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-3.png)

## Processo de Transformação

A mais importante, e a que tem muito mais trabalho.

É a etapa em que os dados vão ser modificados, melhorados, limpados e reestruturados para os seus destinos

## Staging Area

Eu nâo posso fazer a manipulaçâo dos dados na fonte, e nem mesmo no DW.

Entâo, tenho que fazer as modificaçôes no Staging.

Há duas estrtegias de Staging: Remoto
+ Ou o Staging está dentro do DW (ou seja, é uma tabela do DW), como num schema separado
+ Staging ser um BD separado

O tutor particulament não gosta de usar o staging no DW, mas se não houver outra opçao, fica dentr do DW


Staging ON-site
+ No mesmo local da origem dos dados, na fonte

## Rotinas de Transformação

Rotinas mais comuns nessa rotinas de ETL

+ Limpeza de Dados
+ Eliminar inconsistencias
+ incluisão elementos
+ Merging de dados
+ Integração

Vamos ver diversos problemas e como resolve-los

### Problemas durante a T - Anomalias

É alguma coisa que fugiu do padrão


Ex: 

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-4.png)

Solução: Consultar a área de negócio e asim manipular para todos os caasos de 'Nome_Cliente' está com o mesmo padrão

### Problemas durante a T - Padronização

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-5.png)

Problema: Qual o padrão vamos utilizar para data, medida, moeda.

Enfim, voce tem que escolher um padrâo e fazer em tudo.

### Problemas durante a T - Valores Faltantates

O que fazer:
1. Faz um replace por um valor constante
2. O que pode fazer é a média do que está disponível



### Problemas durante a T - MuiltiPart Keys

No BD relacional voce pode ter várias tabelas espressando um mesmo valor. E asism, o identificaor real será a uniâo de todos eeles.

NO exemplo abaixo temos o código do prdoutod, que está expresso em pedaços, e cada pedaço está em locais diferentes.

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-6.png)

### Problemas durante a T - Valores Duplicados

Valores duplicados PODE OU NÃO SER DUPLICADOS.

Ex: Transaçâo de hora-minutos, pode haver casos de haver 2 tranaçoes no mesmo momeneo, e assim voce acahr que é duplciado, mas na verdade nâo é

### Problemas durante a T - Convenção de Nomes

Dados em sistema difenrte podem ter nomes difernete como na imagem abaixo.

É seu trabalho conversa com o pessoal de negócio para saber cada coisa

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-8.png)

Soluçâo: conversa com todo mundo e fazas operaçoes no Staging

### Problemas durante a T - Formato de Dados

Converter dados. Nem sempre as conversões sâo boas. 

Unicode, GeoLocalizaçâo, String <=> Number e vice-versa.

### Problemas durante a T - Significado de Elementos

Crítico, pois pode fazer que voce carregue errado

Aqui é um problema de interpretaçâo e de comunicação. É ncessário documentar e perguntar bem ao negócio/usuário.

Ex: O usuário quer detalhes do cleinte. Quais detalhes ele quer. Se ele fala só detlhes voce pode mandar errado, entao converse bme com ele.

### Problemas durante a T - Integridade Refrencial

É um dos problemas mais críticos, pois influencia muito.

É caso em que, eu pego os dados mas eles sao deletado depois. Entao, meus dados esto referenciando a nada real. Ou seja problema de PK/FK

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-10.png)

Olha na iamge, o departamento te 4 valores e na tabela ao lado há o caso de '50' e '60'. Ou seja, esse dois (50,60) estâo ou nâo no departametn. E eu mantenho ou não eles no DW.

É divícil detectar, crie queries para detectar isso.

## Padrôes de Qualidade dos dados

FUndamental que voce garanta isso

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-11.png)

## Design do processo de Transformação

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-12.png)

Pode ser bom consultar um analista de quailidade

## Processo de Carga dos dados

É carregar os dados no DW

Como passar bilhoes, talvez, 1 TB de dados para o DW. Eu vou fazer 1 bilhão de Insert pela internet?

Há 3 alternativas

**1. FlatFiles**
+ Em gero arquivos txt, csv e esse arquivos sâo carregados no DW

**2. Distributed Systems**
+ Se conectar a outro banco de dados e carrega de outros servidores
+ Conectar 2 bancos de dados e passa de um apra outro

**3. Transportable TableSpaces**
+ É feito no Oracle. É praticamente dizer que os dados do Staging fazem parte de outra tabla, so mudandado a referencia. 
+ É necessário que ambos tenham o mesmo char-set


## Carga inicial dos dados

Carga inical: a 1 carga para o DW. Demora muito
Refresh: Realizar atualização dos dados. Essa atualização pode ser semanal, diária. Enfim, essa periocidade depende dão negócio.

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-13.png)

## Modelos de Refresh

Extract Processing Enviroment
+ Em intervalos específicos, cria um novo snapshot na fonte para carregar no DW
+ O critério para atualizar é de acordo com a fonte.
+ Ex: Caro DBA, a cada 1h gere Snapshot das tabelas x,y,z pois vai ser alimentado na staging area. E durante a notie faço a tranformação e o carregamento dos dados
+ Essa estratégias é interressante quando os dados sao atualizados na fonte com frequencia.
  - não quer dizer que vou fazer ETL a 1 hora, mas sim que terei até 1 hora de certeza que os dados estao atualizados até chegar a hora de fazer o ETL

Warehouse Processing Enviroment
+ A cada intervalod e tempo, carrega no DW, mudanças na fonte de dados
+ Aqui depende do destino, no DW

A decisão é de acordo com a regra de negócio

### Design da carga

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-14.png)

dos 3 processos de ETL, é o mais fácil

### Granularidade dos dados

Se voce definiu a granularidade muito alta (ex: por minuto), voce vai demorar demais para fazer o ETL

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-15.png)

Enfim, se a granularide estiver atrapalhando, fale com o pessoal do negócio.

### Técnicas e Ferramentas de Carga de Dados

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-16.png)

## Pós Carga

Depois de fazer é necessário fazer algumas coisas:
+ Criar/recriar os índices
+ Gerar chaves
+ Criar tabelas de sumário
+ Filtrar dados

Enfim, tarefas apos a carga dos dados

## Indexação

Tipos de Indexação
+ Indicam o melhor caminho para buscar os dados.
+ **Objetivo**: Melhorar perfomance nas consultas
+ Se você cria o indice, as consulta ficam mais rápidas, pois evita fazer full-table scan.
+ Todo BD tem uma indexação
+ EU crio indexes para as colunas que mais vou quere filtrar

### Btree Index

Balance Tree Index.

Tipos mais comun de index.

Usado para colunas com alta cardinaldiade (não se repetem), como por exeplo chave primaria, CPF e etc..

Indicado quando precissamos retornar poucos registros

### BitMap Index

BitMap Index

+ Indicado para colunas com baixa cardinalidade (dados que se repetem com frequencia)
+ Oferece boa perfomance e economiza storage
+ Pode ser usado com grandes tabelas

**ESSE É O QUE VOCE VAI MAIS ENCONTRAD NO DW, PORTER MUITOS VALORES REPETIDOS**.

### Diferença entre esses indexes

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-18.png)

### Outros indexes

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-21.png)


## Integridade dos Dados

Verificar se os dados estão certinhos ou não

Pode ser detectado ao fazer indexes ou CONSTRAINTS.

Voce pode fazer alguma Query SQL, para garanti que os dados estejam certos.


## Ferramentas de ETL

Aqui ele apresenta diversa ferramentas de ETL e até mesmo como instalar/usar.

### Vídeos

├── 177. Ferramentas ETL ou de Integração de Dados.mp4
├── 178. Ferramentas ETL Para Data Warehouses.mp4

├── 179. Oracle Data Integrator.mp4
├── 180. Instalando o ODI  Parte 1.mp4
├── 181. Instalando o ODI  Parte 2.mp4
├── 182. Instalando o ODI  Parte 3.mp4
├── 183. Pentaho Data Integration.mp4
├── 184. Instalando o Pentaho Data Integration.mp4

├── 185. SQL Loader.mp4
├── 186. Bonus  Exemplo de Carga ETL com Store Procedure PL.SQL.mp4

├── 187. Solução Lab04  Criando Partições no DW  Criando Tablespaces.mp4
├── 188. Solução Lab04  Criando Partições no DW  Criando Tabela e Partições.mp4
├── 189. Solução Lab04  Criando Partições no DW  Carregando Dados na Tabela Particionada.mp4

## Ranking das Ferramentas

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-7-19.png)

Hoje utiliza-se ferramentas para integração do dados.

As grande e as melhores que o tutor propoe são:
+ 1. PowerCenter (informática)
     + ótima mas bem cara
+ 3. Oracle Data Integrator - ODI
+ 4. SQL Server Integration Srvices - SSIS 
+ 5. Talend
+ 9. Pentaho
  - O pessoal adora o pentaho.

### Sobre o Pentaho

Sobre Pentaho as pessoas amam ou odeiam pelo mesmo motivo: **Ela é muito fácil, visual**

O que torna fácil mexer nela e também limita o que dá pra fazer com ela (não dá para customizar).

Pentaho É uma empresa. Queremos o PDI (Pentaho Data Integration).

Ele ensina a instalar.








