# Apache Hop - Grimaldo Oliveira

## Terminalogoa em relaçao ao Pentaho

Hop		Pentaho
Pipeline = Tranformation
Workflow = Job

## Instalar

depden de ter java onsmtalado, e a variavel JAVA_HOME

É um zip, descopcat e usa os sqruivos

``hop-gui.bat hop-gui.sh``

## Configruando algumas coisas

esse sarquiv ``hop-gui` nas primeiras linhas tem algo que pode ser configurado

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


+ o parametro: Xmx2048m significa que vai pegar até 2GB de RAM
+ Informa que a variavel do Java que vai pegar é a 'HOP_JAVA_HOME' e se nâo tiver a 'JAVA_HOME'

## 1 projeto
**Criar projeto**

Cloque no P com + (Create new project)
 
Selecione um direotiro para se o seu ambiente

**Criar pipeline**
+ cloque no botao '1+' no topo esquerda (na barra lateral, o 1 de cima pra baixo) e selecione pipleine

+ Clique na área, selecione csv, e selecione o noso saqruivo 'vinhos_mundo'.
  - Use codificaçâo UTF-8 SMEPRE

 Em seguida faremos uma filtragem apra pegar somente aqueles com 'country=It'.
?+ Na saida, vai gera um csv, o nome da tranformation é 'text input fiçe'. Especifique para ser sCSV e use as 3 abas par agerenciar o processo a ser feito