# Apache Hop - Grimaldo Oliveira

## Requisitos

Ter o java instlaado (configrando nas variavesi de ambiente)

## INstlar

baixe o zio da pasta a aseguir (478Mb)

https://hop.apache.org/download/

## COnfigurar caso der pau

no arquivo hop-gui (bat/sh) vai indicar que ele pega primeiro a varaivel HOP_JAVA ao invez da JAVA_HOME,  além disso, há uma linha que indica a quantiade de memória a ser usadas.

sapoa as primeiras linhas

````
ORIGINDIR=$(pwd)
BASEDIR=$(dirname $0)
cd $BASEDIR

# set java primary is HOP_JAVA_HOME fallback to JAVA_HOME or default java
if [ -n "$HOP_JAVA_HOME" ]; then
  _HOP_JAVA=$HOP_JAVA_HOME/bin/java
elif [ -n "$JAVA_HOME" ]; then
  _HOP_JAVA=$JAVA_HOME/bin/java
else
  _HOP_JAVA="java"
fi

# Settings for all OSses
#
if [ -z "$HOP_OPTIONS" ]; then
  HOP_OPTIONS="-Xmx2048m"
fi
````

executar

linux
$ ./hop-gui.sh


ou ./hop-gui.bat
para windows

FUNCIONA
