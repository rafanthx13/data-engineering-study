# Apache NiFi

## O que é o NiFi

+ Se fala (naifai
+ É uma plataforma para transição e ingestão de dados
   - Uma analogia: é o LOAD do ET**L**. 
+ **NiFi é WEB GUI** Ou seja, nada de código.
+ NiFi é executado sobre a JVM

## Instalar NiFi
+ 1.  Baixe o zip e extraia ele
+ 2. Tenha Java e a variável de ambiente `JAVA_HOME` devidamente instalada
+ 3. Execute um dos arquivos `run-nifi.bat ou run-nifi.sh`
+ 4. Apache NiFi estará em execuçâo se aparecer a seguinte mensagem no cmd
````
Apache NiFi now running and listening for Bootstrap requests on port 55917
````
+ 5. NiFi abre no Browser em algum dos no seguintes endereços:
  -  localhost:8080/nifi
  -  localhost:8443/nifi/login
+ 6. Para mais dúvidas sobre a inicializaçâo veja o seguinte (link)[https://nifi.apache.org/docs/nifi-docs/html/getting-started.html#i-started-nifi-now-what]
+ 7. O NiFi gera por default as credenciais inticias que estão em /logs/nif-app.logs
    - Vai gerar linhas como as seguintes
+ 8. Demora um tempo até subir esse localhost

````
Generated Username [bd65594e-3571-49e8-909f-cbfd333c73bf]
Generated Password [T/8WEaFiql19iZQz62Q1TikGkFGS5fDG]
````

## Componentes do Nifi e Terminalogias

Templates: são os arquivos com os processors do NiFi


### Erro no NIFI

**O NIFI Coloca erros nos aqruivos de log, em /log/nifi-app.log

Estava dando o segunite error:

2022-01-03 17:43:17,985 INFO [Timer-Driven Process Thread-7 <Terminated Task>] o.a.n.c.repository.FileSystemRepository Unable to write to container default due to archive file size constraints; waiting for archive cleanup

Eu consegui resovler fazendo isso

nifi.content.claim.max.appendable.size=10 MB
nifi.content.repository.archive.max.usage.percentage=98%

Acho que era porque o disco do PC estava bem cehio.

## Tempo para inicializar

O NiFi demora até subir no local host. Analisando o `nifi-app.log``` podemos estibular o quanto tempo demorá até subir.

A primeira mensagemé

2022-01-04 10:28:20,298 INFO [main] org.apache.nifi.NiFi Launching NiFi...

Ultima Mensagem

2022-01-04 10:34:56,996 INFO [main] org.apache.nifi.NiFi Started Application Controller in 77.517 seconds (77517552000 ns)

Então é cerca de 7 Minutos

## Comandos

Slavar Arquivo: No Nifi é chamado de Tempalte. Clique com o botão direito no workSpace, em 'Create Tempalte' de um nome e descriçâo na primeira vez.
  - Para voce ver, vá no menu > Tempalte. Terá todos os tempaltes, faça o download do seu temṕalte, é um arquivo XML

## Projeto Fluxos de dados

### Projeto 1 - Gerando um Rnadomlow

Vamos gerar um fluxo de dados alertaorios para testar o Nifi

Como fazer
1. Com o Nifi Aberto, selecione um processor e arrasta para o workspace
2. Selecione o GenerateFlowFile

### Projeto 4 - Compressâo de dados

Pega uma seŕie de arquivos, junta eles num zzio e coloca em outr apasta

### Porjeto 5 - Filtrando dadso

**Aula**: 73 (arquiv-treinamento 05)

Vamo fazer a ingestâo somente se satissfazer alguma condição no NiFi

O Nifi nâo é tâo bom quanto o ApACHE hOP/Pentaho para fazer isso, mas é possíve. Por causa disso, o programa ficou grnade. Além idsso, para ele buscar campops é umpouco mais dificpil que i Apache Hop

### Projeto 6 - Latenrando condeudi


### Projeto 7 - Buscamos dados do XML

**Aula:** 75

**Objetivo**: ler o arquivo `.xml` e salvar somente um campo específico para cda registro do XML.


### Projeto 8 

TailFile: vai ler os últimos registro de um arquivo

O que tem de interrssante:
+ A parte em que que faz o merge dods dados
+ o proccessor grupo, que serve como um job do pentaho (permite encapsular vários processosrs)
