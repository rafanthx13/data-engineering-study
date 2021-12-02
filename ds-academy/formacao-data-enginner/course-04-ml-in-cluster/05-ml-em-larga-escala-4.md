# ml em larga escala 4

## Resumo

Vamos concluir o nosos projeto.

## PARTE 1

### Series Temporais - ROlling Statistics

É uma estatisca movel, numa serie temporais com uma janela

img-c4-05-01

No exempllo a seguri: calculamos meiads numa janela de 7 potnos

img-c4-05-02

link do post sobre rolling average

How do I calculate a rolling average?
https://www.portent.com/blog/analytics/rolling-averages-math-moron.htm

Grafico da qtd de visitas

img-c4-05-03

Percb que há alguns picaos. Há alguma tendencia


gafico da rolling average
img-c4-05-04

img-c4-05-05
Essa tencica é bem pesada. Demorou 2 ho para fazer isso no nosos dataste

img-c4-05-06

ROlling Vaerage é um tipo de convoluçâo (CNN

img-c4-05-07

oOu seja, calculcar média aqui é inutl, já ue se trata de séries temporais. ENtao, apra reolveir isso, precisamos de algo mais poderoso


## PARTE 2 - JUPYTER not 2 - Rolling Calculations in time series

ELe é basicamente dedicada ao calculo dessa staticas rolantes

lag: tamanho da janela

### Dicas para executar hardware

Essa rllin gcomputing é muito pesadas, entao a seguri há algumas dicas.

1. Salve o seu progresso no formato '.parquet' para poder dedicar um notebobok somente para fazer esse processamretno. Parquet é o formato preferido do spark. Ele nao so salva dados, mas salva es
2. improima duraten o procesos para acompnaha

### Calculo da rolling

media, diferneaç, desvio padrao, max e min

juntamos tudo (esse processo é coplexo, leia o codigo e video - aual 83 a 85
3. use coamando 'htop' para montiorra uso da 'cpu'


## PARTE 3 - Jupyter not 3 - labeling, feature egenerih  emodeling

O que fazmos
+ Carregamos os dados
+  a label (target) deve ser do tipo dobule
+ famzos o psca, porque como adicionameos rolling features, temos agora 1150 variaveis
  - Faço uma normzatizçao dos dados
+ Separamos em dados de treino e teste

+ Os addos estao desbalanceados, agente faz um seu balancemnetocom uma tecnica simples

+ Vamos por dados em mororaia (esse é traalho do en geherio de dados, de rodar o codigo de ML com a melhor perfomance posisivle)

````
train_downsalmped.cache()
testing.cache()
````

+ Usamos 2 modelos, RandomTree  e GBT. Eles tiveram perfomances paraceidas, mas buscamos o Random ao outro por causa da regra de negocio. 
  - Para projetos reais, o cuso de um falso-positivo pode ser muito maior do que agente pensa, assim, a regra de negócio influncia no melhor modelo para o nosos problema.

+ Faço HyperTUning para a Random Forest. Demorou 54min

+ Por fim, criamos um modelo

## PARTE 3 - Pipeline com Hbase usando API Java

### O que vamos fazer

**Vamos construir um piplne usando api java**

porque java:
+ pythno e R sao excelente para anlise de dados, agora uma aplicação automatizada, talvez java/scala seja melhor

porque Hbase
+ Hbase é NoSQL que roda sobre o HDFS.
+ O Hbase é uma interfaca acima do HDFS para acessar os dados do clsuter

O piplein é: ETL e por num local par aso cinceits poderem acessar os dados.


### VM da clidera

Usaremos uma VM da cloudera 'QUicjStarts for CDH 5.13" para virtual box

Poruq eusamos isso:
+ Ja vem com GUI
+ HBASE e Haddop já estao configurandos
+ vem com o eclipse para desnvolvermos em java

### COdigo Java

Vamos chamar API java que já está pronta e acessa o Hbase.

Build Path/ COnfigure BUild Path/

Vmoce vai inserier 'add external JARS' e busacr em usr/lib/haddop/ e seleciona todos os JAR.

Assim o eclipse vai econtrar os JARs que queremos. 

Famozs o mESMO CO as pastas de mapreduce, hfs, hbase.

Por fim, nao deve masi ter problema ao importar as PAI java

## MExendo com Hbse

use o shell para acessar hbase

execute o codigo java

observe que nosos codigo criou a taebla hbase.

POr fim, voce pode incluir outros itens e brinar amais até que seu programa java tenha capaccaide de fazer diversas funçoes no Hbase
