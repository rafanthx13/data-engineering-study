# Apache Hop - Grimaldo Oliveira

Curos: [Academia Engenharia de Dados](https://www.udemy.com/course/academia-engenharia-de-dados/)

## Terminologia em relação ao Pentaho

+ Apache Hop == derivado do Pentaho


+ Pipeline == Transformation
+ Workflow == Job

## Como Instalar

1. Baixar o `zip` e executar ``hop-gui.bat // hop-gui.sh``
2. depende de ter java instalado, e a variável `JAVA_HOME`

## Configurando algumas coisas

Esse arquivo ``hop-gui` nas primeiras linhas tem algo que pode ser configurado

````bat
REM set java primary is HOP_JAVA_HOME fallback to JAVA_HOME or default java
if not "%HOP_JAVA_HOME%"=="" (
    set _HOP_JAVA="%HOP_JAVA_HOME%\bin\java"
) else if not "%JAVA_HOME%"=="" (
    set _HOP_JAVA="%JAVA_HOME%\bin\java"
) else (
    set _HOP_JAVA=java
)

REM # Settings for all OSses

if "%HOP_OPTIONS%"=="" set HOP_OPTIONS=-Xmx2048m
````


+ O parâmetro: **Xmx2048m significa que vai pegar até 2GB de RAM**
+ Informa que a variável do Java que vai pegar é a 'HOP_JAVA_HOME' e se não tiver a 'JAVA_HOME'

## Projetos realizados no curso

### projeto 1 - Pipeline para vinhos

**Aulas**: 6 a 10

**Arquivo De Entrada:** `vinhos_mundo.csv`

**Arquivo do projeto:**`01-first-pipeline-wines.hpl`

**Criar projeto**

Clique no P com + (Create new project)

Selecione um diretório para se o seu ambiente

**Criar pipeline**
+ clique no botão '1+' no topo esquerda (na barra lateral, o 1 de cima pra baixo) e selecione pipeline

+ Clique na área, selecione csv, e selecione o nosso arquivo 'vinhos_mundo'.
  - Use codificação UTF-8 SEMPRE

+ Em seguida faremos uma filtragem para pegar somente aqueles com 'country=It'. 

+ Na saída, vai gerar um csv, o nome da transformation é 'text input file'. Especifique para ser CSVe use as 3 abas para gerenciar o processo a ser feito

  ​

### projeto 2 - Pipeline Merge de dados

**Arquivo do projeto:**`02-merge-de-dados.hpl`

**Arquivo De Entrada:** `Cliente.xlsx, Marca.xlsx, Produto.xlsx, Vendas.xlsx`

**Arquivo de Saida:** `merge-dos-dados.csv`

O que é feito de interessante:
+ Merge de dados: Para fazer, é ideal ordenar antes



### projeto 3 - Ajuste de Strings

**Arquivo do projeto:** `03-ajustar-dataset-cliente-veiculo.hpl`

**Arquivo De Entrada: ** `cliente_veiculo.csv`

**Arquivo de Saida:** sem saída de dados

o que é feito de interessante 
+ tratamento de string



### projeto 4 - Chamada de API REST

**Arquivo do projeto: ** `04-use-api.hpl`

**Arquivo De Entrada:** chama de API RES de CPF

**Arquivo de Saida:** `saida-api.csv , result_json_api.js`

```
hop-run.bat -j treinamento -r local -f C:........\05-trata_banco.hpl
```



### projeto 5 - Usando DB

Criação de tabelas no PostGreSQL

**Arquivo do projeto:** `05-handle-database.hpl`



## WorkFlow

No Apache Hop á dois tipos de arquivos: Pipeline e Worflow.

O worflow é o job do pentaho, ou seja, é um orquestrador de pipeline.

O que faz de interessante
+ Tem o sucesso e falha
+ Permite executar n arquivos workflow de forma sequencial/paralela
+ Escreve em log
+ Cria variáveis em memória  que pode ser usadas nos pipeline

O workflow possui passos diferentes do workflow



## Hop-Run : Executar Hop em CMD

Você executa através do 'hope-run', é possíve então automatizar a carga ao usar em conjunto com `crontab`

Para ver a documentação
https://hop.apache.org/manual/latest/hop-run/index.html

exemplo

```
./hop-run.sh -j transforms -r local -f /path/to/workflow/file.hwf
```



