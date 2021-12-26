# INstall airflow

##  virtual env

$ pip install virtualenv

Start by making a new directory to work with:

$ mkdir python-virtual-environments && cd python-virtual-environments

Create a new virtual environment inside the directory:

# Python 2:
$ virtualenv virtual_env

# Python 3
ython3 -m venv virtual_env

cria a pasta virutal_env. ELa nao deve subri no git. Nela vai ficar os pacotes python. Ela via ficar pesada.

source virtual_env/bin/activate

vai aaprecer (virtak_env) indicando que está nessa especie de python zerado. e use deactivate para sair

$ pip freeze > requirements.txt

##  Projeto 1 - Airflow no Heroku Medium

https://medium.com/@gilsondev/usando-o-airflow-no-heroku-562f2c5ad021

$ source .venv/bin/activate
$ pip install "apache-airflow[postgres,password]" cryptography
$ pip freeze > requirements.txt

### Executando aiflow

$ export AIRFLOW_HOME=$PWD  # Definindo a raiz do airflow na pasta corrente
$ airflow db init

vai criar arquivos e pastas

airflow.cfg  airflow.db  logs    webserver_config.py

coloque essa pasta de logs no git ignore, pois nao vmaos usals, nem virtual_env

Esse comando irá criar os arquivos necessários para o Airflow, e rodar as migrações em um banco SQLite, em que ele armazena os metadados dos workflows. Para uso local e didático, com esse tipo de banco é o suficiente, mas tem outros procedimentos para preparar o seu uso em produção. Outra observação: não se preocupe com o pedido do módulo cryptography. Isso não vai afetar na experiência, isso é importante quando precisa encriptar algumas informações que não é o caso levantar agora, mas o seu uso real é necessário.

### alterar air.cfg

# 30...
sql_alchemy_conn = postgresql+psycopg2://postgres:postgres@localhost:5432/airflow#


# 24 ...
executor = LocalExecutor

# 123 line code ...
fernet_key = $(python "contrib/generage_fernet_key.py")


Dessa forma o Airflow irá usar o banco PostgreSQL para armazenar os metadados das DAGs e suas execuções como o também o seu scheduler.

Remova o arquivo airflow.db e rode novamente o airflow initdb para que as migrations do airflow seja aplicados no banco.

### fernet

Por fim, crie o arquivo generate_fernet_key.py e insira na pasta contrib. Ela irá gerar uma chave para que o Airflow use para encriptação de dados sensíveis. Insira o conteúdo abaixo no módulo citado:

#!/usr/bin/env python
from cryptography import fernet

print(fernet.Fernet.generate_key().decode("utf-8"))

Dessa forma o Airflow irá usar o banco PostgreSQL para armazenar os metadados das DAGs e suas execuções como o também o seu scheduler.

Remova o arquivo airflow.db (é um arquivo default para ser o banco do sqlite) e rode novamente o airflow initdb para que as migrations do airflow seja aplicados no banco.

## Excutar locamente

Esse tutorialé para por um airlfow rodando no heroku.

em um outro ensina a usa locamente

# Definindo o diretório airflow-tutorial como raiz do Airflow
$ export AIRFLOW_HOME=$PWD
(venv) airflow webserver

## INstalar Postgre no ubunut

melhor site

https://www.tecmint.com/install-postgresql-and-pgadmin-in-ubuntu/

garanta que tenha curl:

sudo apt install curl

https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart-pt

Passo 1 — Instalando o PostgreSQL

Para instalar o PostgreSQL, primeiro atualize o índice de pacotes local do seu servidor:

    sudo apt update


Então, instale o pacote Postgres jutamente com um pacote -contrib que adiciona alguns serviços e funcionalidade adicionais:

    sudo apt install postgresql postgresql-contrib
    

# configurar priemiro user par ao postgr
sudo su - postgres
postgres@rhavel-VirtualBox:~$ psql
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
Type "help" for help.

postgres=# 

 CREATE USER rhavel WITH PASSWORD 'crowthunder';
 CREATE DATABASE first_db_postgre;
 GRANT ALL PRIVILEGES ON DATABASE first_db_postgre to rhavel;
 \q
 exit




### preparar para o deploy no heroku

instalar heroku cli
sudo snap install --classic heroku

Configurando projeto para o Heroku

Agora vamos fazer algumas mudanças para que o Airflow seja executado corretamente no Heroku, juntamente com um usuário para acessar o painel de administração da ferramenta.

No caso do Heroku vamos aproveitar o uso de variávels de ambiente para sobrescrever propriedades do Airflow. Faça uso do config:set. Lembre-se de criar o app e os addons necessários:

heroku login


 heroku apps:create heroku-airflow
 heroku addons:create heroku-postgresql:hobby-dev heroku config:set SLUGIFY_USES_TEXT_UNIDECODE=yes
 heroku config:set AIRFLOW_HOME="/app"
 heroku config:set AIRFLOW__CORE__DAGS_FOLDER="/app/dags"
 heroku config:set AIRFLOW__CORE__FERNET_KEY=`python contrib/generate_fernet_key.py`
 heroku config:set AIRFLOW__CORE__LOAD_EXAMPLES=False
 heroku config:set AIRFLOW__CORE__SQL_ALCHEMY_CONN=`heroku config:get DATABASE_URL`
 heroku config:set AIRFLOW__CORE__EXECUTOR="LocalExecutor"

Crie o arquivo Procfile para o Heroku inicializar a aplicação corretamente:

release: airflow initdb
web: airflow webserver -p $PORT --daemon && airflow scheduler

Agora vamos versionar e enviar os arquivos para o Heroku:

$ git add .
$ git commit -m "Arquivos para o ambiente Airflow"
$ git push heroku master

Com isso conseguimos fazer com que o Airflow execute no ambiente:

Mas como pode perceber, deixar aberto o painel dessa forma não é seguro. Vamos tornar mais seguro.










