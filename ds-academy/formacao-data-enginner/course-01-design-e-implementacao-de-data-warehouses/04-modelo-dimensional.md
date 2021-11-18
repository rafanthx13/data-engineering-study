# Modelo Dimensional

## Links

The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling
https://www.amazon.com.br/Data-Warehouse-Toolkit-Definitive-Dimensional-ebook/dp/B00DRZX6XS/ref=sr_1_2?ie=UTF8&qid=1521159195&sr=8-2&keywords=kimball

Dimensional Modeling Techniques
https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/

## Introdução

Voce usa a parte do modelo logico (parte entidade-relacionento) para pegar os relaciioonamento e assim fazer o DW.

A diferença entre ele é: O OLTP (Entidade-Relacionamento) tem mais detalhes,enquanto que o OLAP tem os dados mais agrupados.

Em geral, o mais normal é que o DW seja StarSchema

## Modelagem Dimensional

É uma técninca para construir modelos de negócio como conjuntos de medadas desrcitas através das diferentes faces do negócio.
+ É uma técnica de projeto que procura apresentar os dados numa estrutura padronizada que seja intuitiva e permita acesso com alto desempenho [Kimball]

Tem esse nome pos a ideia desse modelo é: agrupar os dados de maneira a formar cubo, ou hipercubo (mais de 3 dimensoes), que seria uma estrutura padRâo para visualizar os dados

Essa ideia de cubo é: tenho várais , diversas colunas que assimpodem ser eixos coom x,y,z por isso hyper-cubo,pois há masi de uma dimensao. ssim poderemos fazer análise entre vários eixos.

Usamos em geral cubo, ao invez de hyper-cubo, pois é mais fácil de pensar em cubo que hyper-cubo

## Operaçoes no cubo

Essas operaçoes sao as mesmas que sâo feitas no Power BI

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-1.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-2.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-3.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-4.png)

## Beneficios da modalagem dimensaional

Normalizça: fazemos no OLTP e desnormalizmos no OLAP

Benefivicios
+ SUporte a analise multidimensional
  - NO OLTP, eu teria que faer toda hora muito JOIN par aisso
+ O Design é focado em perfomance
  - A perfomenace é mais importante que a normalizaço.
+ Permite Otimização
  - No DW, a modelagem permite mudar os atributos depois de criado, diferente do OLTP que se mudar, muda tudo
+ PErmite alterçôes frequentes, Design Extensivo
  - Diferente do OLTP, no OLAP pode mudar d eum mes para outro. Pode-se adicionar ou retirar colunas, já que o nosos foco é atender ao negóico, e nao em ser um objetio estático
+ Permite acesso a diversas feramentas de análise
  - Diversas ferramenas sao feitas para pegar um BD modelado como DW. Como por exemplo o Power BI que, junta os dados autoomaticamente pelas relaçôes

## O que sâo dimmensioes

Dimensao: conjunto de objetos que descrevem e classificam os datos atraevs de seus atributos. Sao nesse atributos das dimesnoes que pemite relizar as operaçoes do cubo: fatiamneto, agregaçao e navegaçao hierarquica (drill up/down))

Em geral, os atributos de dimensao sao dados textuais.

Em geral, as dimenoes nao sao muito populados, e os registros lá inseridos tendem a nao ser modificados depois de colocados.

O que tem na dimensao
+ COntem informçaoes textuais que representma atribuos de negocio
+ COntem dados que sao rrelativamente estaticos
+ sao relacionado com a tabela FATO atraves de FK

**LEMBRESE: VOCE ESTÁ MODELANDO PAR AO NEGÓCIO, E NAO PARA O TI. O FOCO É ATENDER AS NECESSIDADES DOS TOMADORES DE DECISÂO**

## Slowing Change Dimensions

Slowing Change Dimensions: (SCD): Retrram as dimenoes que sofrem atualizaçoes em seus campos e os classifica pelo tipo de mudança existet em cada uma delas.

Tipos SCS
+ Tipo 1: Nao há registro de que houv ealteraçao.
  - Sobrepoe e perde histórioc
+ TIpo 2: É adicionado um novo registro , mantendo assm os registros antigos
+ Tipo 3: Adiciona uma nova coluna na tabela dimensao
+ Hibrido: Combina todos os anteriores

Ex: Tenho o seguinte BD, com a seguinte tabela que é uma DIMENSAO. Eu quero mudar o nome do responsável. COmo vou fazer isso?

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-5.png)

Tipo:1 Sobrescreve
Tipo 2: Cria um novo registro (mantem histórico)
Tipo 3: Cria uma outra coluna

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-6.png)

É necessário então pensar, se houver alguma mudnaaç, qual estratégia utilziar? e qual gasta menos espaço, enfim, pensar em qual desssa sutilizar. POde ser também que nem precise do histórico. Tavles o negócio nem precsise saber o histórico do responsável.

EM geral, o predomeinante é o SCD de tipo 2


## Tipos de DImenoes

Slowly CHanging DImension
+ Que recebe alguma modificaçâo

Dengerate Dimension
+ É uma dimensoa que ao invez de ser uma dimensao, virou uma coluna da tabela fato por nao precisar de uma dimensao explusiva

Role-playing Dimension
+ Tem as SurroGate Key

Conformed DImension
+ EM pratica, é ideal deixar todas as dimenoes nessa forma. São fatos

Junk DImension
+ Em geral nao é lembrada. É agrupar tudo em uma unica tabbela. Ela é uteis quando há pouca cardinaldiade, como por exemplo, uma tabela de categoria. Ela teria somente a PK, FK e uma descriçâo

## O que sâo fatos


Sâo mediçeos do negócio. Geralmente sao dados numerosc e aditivos, ou seja, podem ser agregados por soma, media, e outras funçoes GROUP BY

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-7.png)

É a prinicpal tabela no modelo dimensaional. Na pratica eu crio o DW para obter os aftos, e os fatos sao os cruzamentos das varias dimensaoes

## Tipos de Fatos

"COPY PASTE DO PDF/TXT"

Tipos de Fatos


	A tabela fato é a principal tabela do Data Warehouse e ela fica no centro do Star
Schema, sendo rodeada por dimensões. A tabela fato armazena o que ocorreu, é o fato
propriamente dito. É na tabela fato onde as métricas são armazenadas, junto com as Surrogate
Keys que ligam às dimensões que descrevem essa métrica.

	Existem 6 tipos de fatos:
		- Fato transacional
		- Fato consolidada
		- Fato agregada
		- Fato de snapshot periódico
		- Fato de snapshot acumulado
		- Fato sem fato
	
	Fatos transacionais são as mais comuns. A maioria dos bilhões de linhas que temos no
Data Warehouse são de tabelas de fato transacional. Elas geralmente utilizam métricas aditivas,
aquelas métricas que podemos somar por todas as dimensões.

	A tabela fato consolidada é bem parecida com a agregada, mas serve para combinar 2
tipos de processos. O que é processo? Área de negócio, área de assunto, processo de negócio.
Diferente da tabela fato agregada, que serve para fazer agregações em geral, a fato consolidada
é para consolidar duas fatos. No processamento ETL, na hora de carregar a fato, você vai
carregar uma, carregar a outra, e misturar as duas. Evidente que a granularidade precisa ser a
mesmo. Um exemplo clássico: você tem uma tabela fato venda e depois precisa unir com uma
tabela fato venda orçada. É claro que você pode fazer uma dimensão de cenário e já colocar lá
se ela é orçada. Mas isso é em um mundo ideal onde você começa seu Data Warehouse do zero
sem nenhum problema. E muitas vezes, mesmo que não tenha sido um desleixo, na hora de
fazer o levantamento de requisitos, ninguém nunca falou que seria necessário trabalhar com
orçamento de venda, então ao invés de criar uma dimensão de cenário e reprocessar tudo, foi
criada uma nova tabela fato. São várias situações em que isso pode acontecer. As tabelas fatos
consolidadas adicionam uma complexidade extra no processamento do ETL. Você vai ter que
reconfigurar todo o processo ou simplesmente fazer um novo.

	A tabela fato agregada tem a função de acelerar o desempenho das consultas. Ela serve
para agregar dados quando eu não quero analisar no nível do grão.

	A snapshot periódica é a famosa foto. Tiramos uma foto do momento atual e salvamos.
Ela tem as colunas de entrada e saída, que são opcionais, mas é bom colocar, porque a equipe
de negócio sempre pede esse tipo de métrica adicional. Isso é bem comum em redes de varejo
onde precisamos usar esse tipo de tabela, onde vai ter somente o consolidado daquele dia.

	E qual a diferença de um snapshot acumulado para periódico? O periódico pega o
momento no período, tira uma fotografia e insere na tabela fato. O acumulado também é uma
fotografia, mas em mais de um momento.

	E temos ainda a “Fato Sem Fato” (Factless Fact Table). Uma tradução livre seria fato sem
métricas. Ela também é chamada de fato de associação ou de interseção, mas o termo técnico é
fato sem fato ou factless fact table. E para que serve? Para fazer uma interseção de dimensões.
Às vezes queremos comparar ou cruzar algo somente entre duas dimensões e não tem uma
métrica para fazer essas comparações. Essa tabela fato é a exceção, só é usada quando se
precisa fazer uma interseção entre as dimensões. Dois exemplos de fato sem fato: frequência
de aluno ou venda com promoção.

	Nem todos esses tipos de fatos serão usados no dia a dia, mas é sempre bom saber que
existem, para quando houver uma necessidade específica.


## Tipos de Métricas

O que buscamos dos fatos sao as metricas, o valor numerico que está na tabela fato agrupado. Sâo chamads de KPI (Key perfomance indicadotr),  ou de simplesimenete metricas


**Fatos Adtivos**
+ Essa metrica é provenite da intersesao de todas as dimesnoes

**Metriacas Semi-aditivos**
+ Podem ser somadas por todas as dimenoes, exceto pela dimensao tempo
+ Ex: saldo de stoque, saldo bancario

**Metricas na-aditivas**
+ nao podem ser adicionadas atraves das dimensoes
+ sao em gral, porcentagens; EM geral, voce nao salva ela no DW, voce calcula

**metrica derivada**
+ metrica calculada sobre as metrica que já estao na tabela fato. É uma informaçao adicional. Isso pode ser feito pelo ETL, na hora da integraçao, e asism, fica calculada antes de ser inserida no DW, apra facilitar o BI

## Dados Normalizadoe  Desnomoralaizados

Normalização: é está na 3 forma normal.
+ Permite armazenamento consistente, e crud eficiente. Usado em OLTP

Desnormalizao: Foco na consulta, em OLAP
+ Agente DESNORMALIZAR poruqe a noralziao geera um mal desemepenho em consultas
+ É claor, no OLAP voce pode ter alterçoes, mas voce faz em batch, umotne de uma só vez num processo ETL
+ CUsto da dernosmrlaiazço: pperca de constistente e o banco fica maior
+ Teremos uma redundncai de dados, mas, apra consutlar, ficara mais rápido

ex:

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-8.png)

Observe acima. Imagine que tenho a lcoadidade Rio de Janeiro. No modelo OLTP, ele va aparece ruma unica vez, um unico registro na tabela Localidade. ENquanto que no DW, ele pode aparecer várias vezes.

É isso que nos queremos mesmo. Para consultar voce tem que usar FK no OLTP, enquanto que no DW nâo

## O que é NOrmalizaçao

"Copiado do pdf (está como txt)"

Mas o que é Normalização?


O Que é Normalização?

	A normalização do banco de dados é o processo de transformações na estrutura de um
banco de dados que visa a eliminar redundâncias e a eliminar anomalias de inserção,
atualização e exclusão.

	Ao efetuar o processo de normalização, os dados cadastrados no banco de dados ficarão
organizados de uma forma melhor e ocuparão menos espaço físico. Entretanto, o processo de
normalização também faz aumentar o número de tabelas e em muitos casos pode ser uma
tarefa difícil de ser realizada. Além disso, bancos de dados normalizados além do necessário
podem ter desempenho ruim e/ou complexidade excessiva.

	A principal finalidade do processo de normalização é eliminar as anomalias de inserção,
atualização e exclusão. A anomalia ocorre quando não há forma de se cadastrar alguma
determinada informação sem que alguma outra informação também seja diretamente
cadastrada. Por exemplo, imagine que você tenha uma tabela funcionário com os seguintes
dados: codigo, nome, projeto; onde a tabela projeto corresponde ao nome do projeto no qual
um funcionário foi alocado.

	codigo		nome		projeto
	1		Pedro		Vendas
	2		Maria		Vendas
	3		Carlos		Cadastro de Clientes
	
	E então surgiu um projeto novo, o de emissão de notas fiscais. Como você cadastra esse
novo projeto? A resposta é que não dá para cadastrar, pois para fazer isso você teria que ter
algum funcionário nesse projeto - ou seja, temos uma anomalia de inserção.

	Se no exemplo anterior, o funcionário Carlos fosse desligado da empresa e o
removermos da tabela, a informação sobre o projeto de cadastro de clientes é perdida. Isso é
um efeito colateral indesejado - é a anomalia de exclusão. Se, no entanto, ele apenas fosse
remanejado para o novo projeto de notas fiscais, nós também perderíamos a informação sobre
a existência do projeto de cadastro de clientes - essa é a anomalia de alteração.

	O problema que origina essas anomalias é o fato de a informação do projeto estar toda
dentro da tabela de funcionários, que não é o lugar dela. Se tivermos duas tabelas relacionadas
(1-para-N) - funcionários e projetos - as anomalias desaparecem. Anomalias também têm
relação com o conceito de integridade referencial.


Integridade Referencial

	Integridade referencial é um conceito relacionado a chaves estrangeiras. Este conceito
diz que o valor que é chave estrangeira em uma tabela destino, deve ser chave primária de
algum registro na tabela origem. Quando essa regra é desrespeitada, então temos o caso em
que a integridade referencial é violada.

	Vejamos a terminologia: Integridade vem de íntegro, inteiro, completo, correto.
Referencial vem de referência, indicar algo ou alguém. Portanto, integridade referencial é
indicar algo ou alguém de forma íntegra, completa, correta. Por exemplo, veja essas duas
tabelas:

	Carros
	Placa (PK)	| Modelo	| Proprietário (FK)
	----------------+---------------+------------------
	ABC-1233	| Passat	| 1
	DEF-4566	| Fiesta	| 2
	UVV-7890	| Palio		| 1
	
	Proprietários
	ID (PK)	| Nome
	--------+------
	1	| Pedro
	2	| Maria
	
	Estas tabelas têm integridade referencial, pois os carros que têm proprietário com ID 1,
podem ser encontrados na tabela de proprietários como sendo do Pedro. O carro de
proprietário com ID 2 pode ser encontrado como sendo da Maria.

	Agora, imagine que nós venhamos inserir um carro de placa EJB-6520, do modelo Civic e
do proprietário com o ID 3. Ocorre que não há nenhum proprietário de ID 3. Se o banco de
dados permitir essa inclusão, ocorrerá uma violação da integridade referencial, pois estará
sendo feita uma referência a uma entidade inexistente. O mesmo ocorreria se quisermos
alterar o proprietário de um dos carros colocando o ID do proprietário como 3.

	Por outro lado, se nós quisermos deletar a Maria do banco de dados sem deletar o carro
de placa DEF-4566 e nem alterá-lo, novamente teremos uma violação da integridade
referencial, pois se o banco de dados permitir que essa exclusão seja feita, a integridade
referencial será violada ao termos um carro que tem como dono, uma entidade agora
inexistente.

	A maioria dos bancos de dados relacionais modernos existentes impõe integridade
referencial quando você tenta inserir, alterar ou excluir entidades no qual há chaves
estrangeiras envolvidas. Se uma violação de integridade ocorrer, o seu banco de dados
apresentará registros inconsistentes que apontam para entidades que não existem, o que
tende a se manifestar nas aplicações sob a forma de vários tipos de problemas.


Formas Normais

	Normalização de dados é um conjunto de regras aplicadas a tabelas de banco de dados
relacionais a fim de manter a consistência dos dados, evitar duplicações/redundância e
problemas com remoções ou atualizações de registros.

	As formas normais são 1FN, 2FN, 3FN, BCNF, 4FN e 5FN. As tabelas geralmente são
normalizadas até a terceira forma, a quarta e quinta formas normais tratam de problemas
específicos. Vejamos aqui as 3 primeiras formas normais.

	Antes de prosseguir com as formas normais, faz-se necessário introduzir os conceitos de
chaves candidatas e superchaves.

	A chave primária é aquele conjunto de colunas que serve para identificar a tupla de uma
forma única (pode ser só uma coluna, ou podem ser duas ou mais). É importante que o
projetista do banco de dados saiba identificar quais são as colunas mais apropriadas para serem
eleitas como parte da chave primária.

	Entretanto, às vezes há mais do que um conjunto de colunas que poderia ser chave
primária. Cada um desses conjuntos é chamado de chave candidata. Por exemplo, em uma
tabela Pessoa que tenha os campos CPF, RG, Estado e Nome, tanto o CPF quanto o RG junto
com o Estado são chaves candidatas. Assim, é possível chegar-se ao Nome a partir do CPF, mas
também é possível chegar-se ao Nome a partir do RG e do Estado.

	Qualquer conjunto de colunas que tenha como subconjunto, uma chave candidata é
denominado de superchave.

## Star Schema

A modelagem dimensional é utilziada para otimizar consultas. O modelo mais utilizado é o StarSchem craido por Ralph Kimball.

Em geral usamos a mesma notaçao utilizada no modelos entidade-relacionaemnto

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-9.png)

Em geral, há o relacionemtno 1,N entre as dimesnoe e a tabela fato

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-10.png)

## SnowFlake Schema

é uma variaçao do StarSchema, em que faz uma normalizçao nas tabelas de dimensao (cria tabelas auxiliares para as dimensoes)

Entao é bsaicmentes: normalizar algumas dimensoes criando assim tabelas com PK/FK.

**FAZMOES ISOS PARA MITICAR O PRINCIPLA PROBLEMA DO STAR SCHEMA: REDNUDANCIA**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-11.png)

Caracteristica em relação ao star Schema
+ masi flexivela mudanças
+ o processo ETL pode ser mais rápido
+ Infelismente degrada perfomance de queries

**O BANCO TRANSACIONAL (OLTP) nâo é bom para consultas grande (pegar varias tabelas, varias pk/fk), entao, crie um DW ou DataMart. Ou seja, nao é bom apra fazer relaórios complexos**

**Tem gente que quer rodar uma queries no OLTP e demora 4h, e nao entende porque demorar tanto. Ele consegue otimizar e vai para 3h. A soluçao seria: criar um DW/DataMart e asism essa queries vai demorar 5minutos**

## Tipos de Chaves

PK
+ Chave primaria. Identifica cada registra
FK
+ Ajuda a fazer o relacionamento entre duas tabelas
+ A tabela fato tem varias FK que aponta para as PK das tambelas dimenoes

Composite Key
+ CHave composta. Uma chave composta por mais de uma coluna
+ A PK da tabela Fato, ou seja, o identificador do regitstro, será a composiçoa de n-FK que apontm apra as dimenoes

E a Surrogate Key


## Surrogate Key

É uma chave artificial. Nâo está amarardo ao negócio.

AJuda a manter a establidade, atravś da neutralidade. 

Servem apenas como ligaçao entre dimenoes e fatos.

Desvantagem: a tabela fato nao pdoe ser consultada diretamente, pois os camposde filtro estaramo armazenadsa nas dimenoes

## Dimensao Tempo

Merece um destaque especial

Observe essas perguntas

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-12.png)

A dimensão Tempo é crítica em um DW

Precisamos definir o nível de granularidade para esta dimensao. Ano, Semestre, Trimester, Mes, meio-mes, semana, dia, hora, miuto, segundo. Temos que definir com a área de negócio qual é o mínimo que vai utilizar

Se eu definir a granularidade menor, vai custar mais espaço/tempo. Se for muito alta, nao tem como bucsca um drill drown.

## Hierarquia de Dimensões

Definido pelo pesosal de negocio. Mas voce, como profissional deve perguntar: Questione se alta/baixa hierarquia é mesmo necessaŕio;


![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-13.png)

Essa hierarquia é importante para fazer drill-up/drill-down

## Regras de ouro para modelagem dimensional

Passos par amodelagem dimension l(sugerido tambem no kimball)

+ Definição da área de negócio
+ Definir processos dentro da área de negócio
+ Definir a granularaide desejada para cada um dos processos
  - Considerar volumes e dificuldae de se obter o nível desejado
+ Definir atributos e hierarquia das dimenoes
+ Definir as mericos da tablea fato
  - Observar os valores aditivos, semi-adtivios e nao-aditivos

É claro, é necesśario ter ba compunicçaoa para comunicar e perguntar tudo isos e asism construir um bom modelo.

Como preparar o modelo dimensional

**REGRAS ULTRA IMPORTANTES**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-14.png)

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-01-design-e-implementacao-de-data-warehouses/imgs/img-3-15.png)


