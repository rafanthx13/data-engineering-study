# 4.Data Pipelines com Apache Airflow

Tempo: 13h13m15s || Quantidade de Módulos 7

## File Tree

├─── 01 - Conceitos e Introdução (01h11m02s)
│       Módulo 01 - Conceitos e Introdução\Airflow vs outros Worloads Managers - Aula 10 (07m59s)
│       Módulo 01 - Conceitos e Introdução\Airflow vs Scripts Bash - Aula 09 (05m31s)
│       Módulo 01 - Conceitos e Introdução\Boas Vindas, Objetivo do Curso e Conceitos Introdutórios - Aula 01 (04m55s)
│       Módulo 01 - Conceitos e Introdução\Componentes e Arquitetura do Airflow - Aula 11 (06m35s)
│       Módulo 01 - Conceitos e Introdução\Data Pipelines para Machine Learning - Aula 05 (06m25s)
│       Módulo 01 - Conceitos e Introdução\Data Pipelines para o Processo de ETL - Aula 04 (07m39s)
│       Módulo 01 - Conceitos e Introdução\Introdução e Porque Escolher o Apache Airflow - Aula 08 (05m32s)
│       Módulo 01 - Conceitos e Introdução\Pipelines em Grafos vs Scripts Sequenciais - Aula 07 (07m19s)
│       Módulo 01 - Conceitos e Introdução\Representação em Grafos de Pipelines - Aula 06 (06m20s)
│       Módulo 01 - Conceitos e Introdução\Responsabilidades do Engenheiro de Dados na Construção do Data Pipeline - Aula 03 (06m43s)
│       Módulo 01 - Conceitos e Introdução\Responsabilidades dos Analistas e Cientistas de Dados - Aula 02 (06m04s)
│
├─── 02 - Instalação e Configuração do Airflow (35m39s)
│       Módulo 02 - Instalação e Configuração do Airflow\Criando o Container e Configurando o Airflow - Aula 14 (07m45s)
│       Módulo 02 - Instalação e Configuração do Airflow\Explorando a Interface do Airflow Webserver - Aula 15 (13m03s)
│       Módulo 02 - Instalação e Configuração do Airflow\Instalando o Airflow utilizando o Docker - Aula 13 (07m50s)
│       Módulo 02 - Instalação e Configuração do Airflow\Pré-requisitos para a Instalação do Airflow - Aula 12 (07m01s)
│
├─── 03 - Desenvolvendo as primeiras DAG's (01h19m59s)
│       Módulo 03 - Desenvolvendo as primeiras DAG's\Airflow Command Interface - Aula 17 (12m26s)
│       Módulo 03 - Desenvolvendo as primeiras DAG's\Conceitos de DAG's e Declarações - Aula 18 (06m47s)
│       Módulo 03 - Desenvolvendo as primeiras DAG's\Conceitos de Dependência e Controles de Fluxo - Aula 19 (06m37s)
│       Módulo 03 - Desenvolvendo as primeiras DAG's\Conceitos de XComs, Operadores, Introdução e Requisitos do Data Pipeline 01 - Aula 24 (08m48s)
│       Módulo 03 - Desenvolvendo as primeiras DAG's\Construindo a Primeira DAG - Aula 16 (07m05s)
│       Módulo 03 - Desenvolvendo as primeiras DAG's\Definindo Edges Labels em Dependências de Tasks - Aula 23 (10m39s)
│       Módulo 03 - Desenvolvendo as primeiras DAG's\Entendendo Regras de Acionamento - Aula 21 (06m46s)
│       Módulo 03 - Desenvolvendo as primeiras DAG's\Implementando uma DAG com Control Flow Braching - Aula 20 (11m35s)
│       Módulo 03 - Desenvolvendo as primeiras DAG's\Testando Regras de Acionamento - Aula 22 (09m16s)
│
├─── 04 - Criação do Data Pipeline para ETL (01h56m29s)
│       Módulo 04 - Criação do Data Pipeline para ETL\Configurando o Airflow para Enviar E-mails - Aula 29 (09m21s)
│       Módulo 04 - Criação do Data Pipeline para ETL\Configurando o Servidor SMTP no Airflow para Envio de E-mails - Aula 30 (10m43s)
│       Módulo 04 - Criação do Data Pipeline para ETL\Construindo o Ambiente OLAP do Data Pipeline - Aula 28 (10m03s)
│       Módulo 04 - Criação do Data Pipeline para ETL\Criando a Estrutura e Carregando os Dados no Ambiente OLTP - Aula 26 (11m32s)
│       Módulo 04 - Criação do Data Pipeline para ETL\Criando e Configurando o Ambiente OLTP para o Data Pipeline - Aula 25 (10m53s)
│       Módulo 04 - Criação do Data Pipeline para ETL\Definindo Operadores do Pipeline e suas Configurações - Aula 33 (12m10s)
│       Módulo 04 - Criação do Data Pipeline para ETL\Desenvolvendo a DAG para o Data Pipeline (Função Extract) - Aula 31 (14m28s)
│       Módulo 04 - Criação do Data Pipeline para ETL\Desenvolvendo a DAG para o Data Pipeline (Funções Transform e Load) - Aula 32 (09m47s)
│       Módulo 04 - Criação do Data Pipeline para ETL\Executando o Pipeline e Avaliando os Resultados - Aula 34 (18m49s)
│       Módulo 04 - Criação do Data Pipeline para ETL\Realizando Consultas e Entendendo a Estrutura dos Dados - Aula 27 (08m43s)
│
├─── 05 - Trabalhando com Agendamento e Pipelines Incrementais (02h47m18s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Agendamento baseado em intervalos vs ponto no tempo - Aula 38 (07m25s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Conceitos de Agendamentos - Aula 35 (07m07s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Configurando a conexão e carregando dados - Aula 53 (10m39s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Definindo delay para re-execução de tarefas - Aula 44 (05m36s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Definindo um Pipeline para buscar dados incrementais do MySQL - Aula 52 (06m47s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Desenvolvendo a DAG para automatização do Pipeline - Aula 50 (10m07s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Desenvolvendo DAG's com parametros dinâmicos utilizando templates - Aula 47 (09m16s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Desenvolvendo um Pipeline para Buscar Dados Incrementais do Mercado Financeiro - Aula 48 (07m23s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Desenvolvendo uma DAG utilizando re-execução de tarefas - Aula 42 (08m53s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Entendendo como funcionam as variáveis no Airflow - Aula 45 (11m22s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Entendendo e aplicando o agendamento baseado em frequência - Aula 40 (09m10s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Entendendo intervalos de agendamento diário - Aula 36 (07m07s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Entendendo o agendamento cron based - Aula 39 (06m55s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Entendendo o recursos de templates e macro no Airflow - Aula 46 (08m46s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Entendendo o script para coletar dados através da API - Aula 49 (06m14s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Entendendo os conceitos de re-execução de tarefas - Aula 41 (05m21s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Executando e avaliando os resultados do Pipeline para buscar dados do Mercado Financeiro - Aula 51 (09m38s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Executando o Pipeline e Avaliando os Resultados - Aula 54 (09m37s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Executando uma DAG com agendamento diário - Aula 37 (10m09s)
│       Módulo 05 - Trabalhando com Agendamento e Pipelines Incrementais\Executando uma DAG utilizando re-execução de tarefas - Aula 43 (09m46s)
│
├─── 06 - Trabalhando com Comunicação entre Tarefas e Sensores (01h46m55s)
│       Módulo 06 - Trabalhando com Comunicação entre Tarefas e Sensores\Conceitos de Operadores Especiais do tipo Sensores - Aula 60 (07m56s)
│       Módulo 06 - Trabalhando com Comunicação entre Tarefas e Sensores\Conceitos Fundamentais de Cross Comunications - Aula 55 (07m19s)
│       Módulo 06 - Trabalhando com Comunicação entre Tarefas e Sensores\Desenvolvendo a DAG para a Seleção de Modelos Automáticos - Aula 58 (13m10s)
│       Módulo 06 - Trabalhando com Comunicação entre Tarefas e Sensores\Entendendo cenários para a implementação de XComs - Aula 56 (07m34s)
│       Módulo 06 - Trabalhando com Comunicação entre Tarefas e Sensores\Escrevendo a primeira DAG com o Operador do tipo Sensor - Aula 61 (06m48s)
│       Módulo 06 - Trabalhando com Comunicação entre Tarefas e Sensores\Executando a DAG e analisando os resultados - Aula 62 (07m17s)
│       Módulo 06 - Trabalhando com Comunicação entre Tarefas e Sensores\Executando o Pipeline e Analisando os Resultados - Aula 59 (06m57s)
│       Módulo 06 - Trabalhando com Comunicação entre Tarefas e Sensores\Executando o Pipeline para Monitoramento de Diretórios e avaliando os resultados - Aula 64 (09m26s)
│       Módulo 06 - Trabalhando com Comunicação entre Tarefas e Sensores\Pipeline para Seleção de Modelos Automáticos - Aula 57 (13m06s)
│       Módulo 06 - Trabalhando com Comunicação entre Tarefas e Sensores\Trabalhando com Sensores do tipo diretórios - Aula 63 (09m28s)
│       Módulo 06 - Trabalhando com Comunicação entre Tarefas e Sensores\Trabalhando com Sensores do tipo SQL - Aula 65 (17m54s)
│
├─── 07 - Automação de um Projeto de Data Science (03h35m53s)
│       Módulo 07 - Automação de um Projeto de Data Science\Automação de um projeto de Data Science - Aula 66 (06m42s)
│       Módulo 07 - Automação de um Projeto de Data Science\Desenvolvendo as tarefas para a Dag de automação do projeto de Data Science - Aula 83 (08m03s)
│       Módulo 07 - Automação de um Projeto de Data Science\Detalhando o projeto a ser automatizado com o Airflow - Aula 76 (11m54s)
│       Módulo 07 - Automação de um Projeto de Data Science\Entendendo a estrutura da Dag para automação do projeto de Data Science - Aula 81 (09m23s)
│       Módulo 07 - Automação de um Projeto de Data Science\Entendendo as funções utilizadas para a automação do projeto de Data Science - Aula 82 (21m36s)
│       Módulo 07 - Automação de um Projeto de Data Science\Etapas de um projeto de Data Science - Aula 75 (07m12s)
│       Módulo 07 - Automação de um Projeto de Data Science\Executando a Dag e avaliando os resultados - Aula 84 (15m19s)
│       Módulo 07 - Automação de um Projeto de Data Science\Executando as etapas de Feature Engineering (Parte 2) - Aula 79 (08m32s)
│       Módulo 07 - Automação de um Projeto de Data Science\Executando as etapas de Feature Engineering - Aula 78 (10m01s)
│       Módulo 07 - Automação de um Projeto de Data Science\Executando as etapas de Machine Learning e Tunning - Aula 80 (13m15s)
│       Módulo 07 - Automação de um Projeto de Data Science\Executando notebooks e definindo parametros - Aula 68 (18m59s)
│       Módulo 07 - Automação de um Projeto de Data Science\Executando o Papermill através de Dags do Airflow - Aula 72 (06m47s)
│       Módulo 07 - Automação de um Projeto de Data Science\Executando o Papermill através de Dags do Airflow com a interface Python - Aula 73 (11m47s)
│       Módulo 07 - Automação de um Projeto de Data Science\Executando o Papermill utilizando a interface Python - Aula 69 (06m40s)
│       Módulo 07 - Automação de um Projeto de Data Science\Executando o projeto e verificando os resultados - Aula 77 (08m24s)
│       Módulo 07 - Automação de um Projeto de Data Science\Instalando o Papermill e executando o notebook do projeto - Aula 67 (10m52s)
│       Módulo 07 - Automação de um Projeto de Data Science\Instalando o provider para o Papermill no Airflow e praparando o ambiente - Aula 70 (10m22s)
│       Módulo 07 - Automação de um Projeto de Data Science\Integrando o Papermill ao Airflow para executar notebooks do projeto - Aula 71 (10m49s)
│       Módulo 07 - Automação de um Projeto de Data Science\Vantagens e Desvantagens da abordagem de automação de projeto utilizando o Airflow - Aula 85 (08m56s)
│       Módulo 07 - Automação de um Projeto de Data Science\Vantagens e Desvantagens da abordagem utilizando o Papermill - Aula 74 (10m20s)
│