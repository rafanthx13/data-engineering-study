# ML em larga escala

## Resumo

Executar um caso completo com Spark, do início ao fim. Vamos implementar um proejto, um pouco de ML.

Usamos o JupyterNotebbok rodandno o pyspark no nosos cluster e tendocomo o rigem nossa maquina local. ROdamos somente o Jupyete notebbok 1 - IMportaçao , limpeza e engenhraia dos dados, de 3 noteboks.

## PARTE 1 - Teoria

### Caso de estudo

## PARTE 2

### O que vamos fazer

**Caso de uso de ML**

img-c4-04-01

Iremos fazer previsâo de defeito de uma máquina de acordo com dados de gestores.

img-c4-04-02

### Bussiness Case

img-c4-04-03

img-c4-04-04

Vamos quere saber se a maquian vai falhar nos proximos 7 dias

img-c4-04-05

### Hardware : Caso sua maquina for fraca

Caso sua maquna for fraca para as 3 virtual box, ou nao consiga montar um cluster

**A AZURE OFERECE UMA MAQUINA PARA CIENCIA DE DADOS GRATUITA. CENTOS  e tudo o mais (py, jupyete, spark, hdfs, spark em cluster)**

https://docs.microsoft.com/pt-br/azure/machine-learning/data-science-virtual-machine/linux-dsvm-intro

### Uso de Memory/Storafge do spark

````
/opt/spark/conf/spark-defaults.conf.template
````

````
$ 
````



Copie esse arquivo com o comando

````
$ cp spark-defaults.conf.template spark-defaults.conf
````

liste diretorio

````
$ ls -la
````

editar arquivo
````
$ vi spark-defaults.conf
````

ajuste os parametrod de 'spark.drive.memory' de 5g par ao que voce quiser.

COnfigure spar.local.dir para '/temp' pois pé para fazer operaçoes de disco naessa pasta
+ Pode ser um disco de perfomance melhor

### Ajustar SistemOperacional

Vmaos configurar algumas coisa do SO par podemos fazer 

````
$ sudo vi /etc/security/limits.conf
````

digite ENTER para entrar no modo de inserção.

````
$ * TAB soft TAB nofile 65536
$ * TAB hard TAB nofile 65536
````

Onde TAB é a tecla tab, não é a string 'tab'

Estou modificando o numero de arquivos que podem ser abertso pelos sitsema operacional, pois o apache esparkvai abrir vários arquivos, mas **O LINUX/WINDOWS TEM UM LIMITE DE ARQUIVOS QUE PODEM SER ABERTOS AO MESMO TEMPO**

Digite o codigo abaico pra sair do vi
````
$ :q
````

### Conectar da minha maquina local com o cluster

no cluster


````
$ cd /opt/spark/sbin/
$ ./start-all.sh
````

Digite o comando abaixo tantno no master quanto nos works para ve se estao rodando o processi


````
$ jps
````

descompacte o dataset.zip de 27Mb e vai ter um arquivo de 1,37 Gb.

Instalae na sua maquina local java/anacnond/spark e seja caapz de ordar localemtne.

Vamos conectar da nossa mauian lcal ao spark da master (ou seja, do cluster)


````
$ pyspark --master spark://192.168.1.139:7077
````

ou seja, configuramos para usar o spark do remoto.

**INICIE pySpark no direotrio que tem seus arquivo .jupyter_notebook**

**AGORA, VAMOS EXECUTAR NOSOS JUPYER NOTEBOBK RODADNO OS CAMONADO PYTHONSPARK NO CLUSTER MA TENDO COMO O ORIGEM A NOSSA MÁQUINA LOCAL**



###

Demoorou de 3h a 4h para executear os 3 jupyter notebooks

São 172 colunas e 2 milhoes de linhas

Padronizamos os nomes das colunas e retiramos coluas tem qutem NAN

**Tratar valoes missing**

Damos um Drop em valoes com NanN, mas temos que usar semancitca. Para lgunas valores: "UNown", vazio e 0 podem ser considerados como valores NaN. ENtâo pode-se um replace de 0,"Unkonw" por NaN e assim.

Nocaso, vamos usar outros valore de outros colunas para os valores faltantasn quando há "" ou "Unknow"

**Construççao de grafico**

Usamos lingaugme SQL apra acessar os dados

````
sqlStatement = """
    SELECT problem_type_1, problem_type_2, problem_type_3, problem_type_4,
    error_count_1, error_count_2, error_count_3, error_count_4, 
    error_count_5, error_count_6, error_count_7, error_count_8, problemreported
    FROM df1
"""
plotdata = spark.sql(sqlStatement).toPandas();

**Feature ENgering**
+ Vamo criar/remover/alterar/unir colunas usnado criterios matematico/estatisticos

O que vamos fazer
+ Extraiomos dados do dia
+ Utilizamos regras de neǵocio + matematica/estatiscia para fazer isso
+ APLICAMOS NORMALIZAÇÃO para nivelar todas as variavies. Agente só está mudando a escala mas nâo a informação
+ OneHot ENconding para dados categóriocs
+ Reduçâo de simensionalidade com PCA. O PCA já é uma tecnica de ML nao-supervisionado. Vamosgerar 20 componentes principais 


