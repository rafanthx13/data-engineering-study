# ML em Larga Escala Parte 2


## Resumo

Depois de instalado e configurdao o apache Spartk, vamos usalo.

Principla framework par aprocessadomento em tempor eal de big data

**OBS**: Há diversos pdfs par aser lido agora

**Reumo**: Instala python e executa pyspark; RDD do spark (abstração de trabaalhar com N node como se fossem um só). conceito de só executar tranformaçao quando uma açao for requisitada

## PARTE 1 - Teoria para o Spark

### Componentes do Apache Spark

Resillent Distributed Datasets: A API foi feita para ambietnte distribuidos e mais uma maquina e o processamento em mais de uma maquina

SQL, dataframe, dataset: Trabalhar com dados estruturados

Stremaing (DStremaing): Processamendo de daods em tempo real

MLlib: COleçâo de modelos de ML já prontos para rodar no spark
+ Vamos usar para rodar os modeos ML

Graphx: COmputação para grafos,

### Formas de executar o Spark

Há duas forasm:
stand-alone: é em uma maquina so
cluster: quando há cluster, prmetie processamento paralelo e usar mais de uma maquina

**como funciona o spark**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-03-01.png)
O progmra spark manda para o spark context, e ele que vai usar um ou mais nós a depende da forma de funcionamento que você escolher

**StandAlone**
+ Abro ospark e apenas indico quemé o mates. Somente o master

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-03-02.png)
**Apache Mesos**
+  Se eu tenbalho com amais de um cluster, eu preciso gerenciar ele. Para isso há o apache mesos quue vai fonrcer a possibilidade de configurar o processmaentos nos vários Nódes do Spark
+ Serve para gestâo de Nodes cluster e é de proposito geral (ou seja, serve para o spark e para outras aplicaçôes)

**Apache Yarn**
+ Fas parte do haddop, dos 3 comentens (hdfs,mapreduce,yanr) é o mais novo

**Kuberntes**
+ vamos estudar nos capítulos do docker

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-03-03.png)

### Resillent Distributed Datasets

RDD: É a abstratação para não precismsor nos preocupar com o ambiente distribuido. ssim, agnte pode focar somente em alto nível

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-03-05.png)
## PARTE 2 - Usando Spark


### PySpark


Há 3 lingaugesn para o spark: R, Python, Java, Scala

Na máquinas master digito

````
$ pyspark
````

Só que está usando python 2, então, vai isntlar o anacanonda para abixar python 3 e os pacaotes necesśarios. Assim ao executar o pyspark depois de instlado o anacaonda, vai usar pytohn 3

**Criando um objeto paralelisavel**

Pytohn poder defualt não é paralelizado. Para faemozr isso depois que usar métodos do sparkCOntext para que nososs dados sejm aparalelizaveis. A seguir há um exemplo para paralelizar uma lsita de string

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-03-06.png)
**Executar operaçôes paralelizaveis**

O spark é um ferramente para procesasmento paraleloe, o que temos de fazer é apenas parassar os dados para o tipo do SparkCOntext

**Como funciona spark: açao/tranformaao**

EM resumo é: o spark não executa os sseus comandos a nãos er que precise retornar algo explicitamente. Eu posos posarsar 5 comandso de tranformação e o pyspark não vai executar nada, ele só vai executar para uma ação.

Você tem que consultar a documntaao paara fazer o que é e quais são as açoes/tranformações

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-03-07.png)

