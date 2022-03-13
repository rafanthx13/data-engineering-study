

execute arquivo elasticsearch.bat

va em localhost:9200

ao fazer um get na raiz deve retornar algo como

````
{
  "name" : "CLIENTE-PC",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "1kBA9RzcSCS3qoqeX52JkQ",
  "version" : {
    "number" : "7.16.2",
    "build_flavor" : "default",
    "build_type" : "zip",
    "build_hash" : "2b937c44140b6559905130a8650c64dbd0879cfb",
    "build_date" : "2021-12-18T19:42:46.604893745Z",
    "build_snapshot" : false,
    "lucene_version" : "8.10.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
````

## o que é Elastic Search e Stack

Baseado no Apache LLucene 

Elastic Search é um método para busca e análise de NoSQL, de forma muito mais rápido que num DBRSM

**O elastic search é uma forma de aramzenamento e ao mesmo tmepo para processar e rmazenar os dados de um forma específica e única**

É o componetne princiapl da arquitetura Elastic Stack para lidar com NoSQL.

Usa API rest-full e JSON.

Para chamar sesu métodos, podemos usar: C#, Curl, Python e até SQL

**Ferramanetas**
ElasticSearch: É como o DB
Lodstah: é a parte de ETL e injestâo de ddos
Kibana: Equivale ao Power BI, para visauzliar os dados. tambem tem a funçao DEV TOOLS que iremos ver mais a frentes tambmém monitorar

Como funcionan juntos
O Logstah insere os dadso no Elastic Searchs, e dai o Kibana ler, mopnirota e gera graicos


**o que é aramzenado**
+ docuemtnos nof formato json

**Analogia das terminologias do ElasticShearch com banco de ados normal**
Elastic Search ===== Database
indice			== schema, databse
tipos			== tabelas
documnetos		== resgitros
colunas de documento == campos ad tabela

## porque o eslatic search é tao bom

Quando um documento é indexado no elastiseach, os conteudos sao separados em 'termos' de busca, conhecidos como tokesn, para facilitar o encontro dos dados. Este procesos ocorre em campos do tipo text.

As nossa buscas requer processo de filtragem para encontra o conteudo: character filtesr, tokeniizer e token filter. 


## Fazendo Load do sarquivos com Lodash

1. O lodash é executado por CMD, via aqruivo.
2. Asism, vmaos criar o arquivo `banco.conf` e temos que opbrigatoriamente por ele na pasta conf de onde está instalado o lostas.
  - Nel colocamos os dados par afazer a ingestâo no elastifcSearch, como por exemplo onde estôa os arquivos que vao carregar no dadsos no Elastic
  - Esse Arquivo 'bancocleinte.conf` fica dentro das pasta logstash/bin/config;; Por default nao é criado, mas nos vamos criar e colocar ele la

De prefecrencia nao coloque espaço no diretorio de odne está o arquivo csv
````
input {
   file {
      path => "C:/Softwares/ElasticSearchWorkSpace/Temp/BankChurners.csv"
      start_position => "beginning"
      sincedb_path => "NUL"
       }
}

filter {
   csv {
      separator => ";"
      columns => ['CLIENTNUM','Attrition_Flag','Customer_Age','Gender','Dependent_count','Education_Level','Marital_Status','Income_Category','Card_Category','Months_on_book','Total_Relationship_Count','Months_Inactive_12_mon','Contacts_Count_12_mon','Credit_Limit','Avg_Open_To_Buy','Total_Trans_Amt','Total_Trans_Ct']
      }
   mutate {
      convert => {
         "CLIENTNUM" => "string"
         "Attrition_Flag" => "string"
         "Customer_Age" => "integer"
         "Gender" => "string"
         "Dependent_count" => "integer"
         "Education_Level"  =>  "string"
         "Marital_Status" => "string"
         "Income_Category" => "string"
         "Card_Category" => "string"
         "Months_on_book" => "integer"
         "Total_Relationship_Count" => "integer"
         "Months_Inactive_12_mon" => "integer"
         "Contacts_Count_12_mon" => "integer"
         "Credit_Limit" => "float"
         "Avg_Open_To_Buy" => "float"
         "Total_Trans_Amt" => "float"
         "Total_Trans_Ct" => "float"
       }
   }
}

output {
   stdout {
      codec => rubydebug
   }
}````

3. Execute o comando 

````
logstash>bin $ logstash -f config/bancocliente.conf
````
sÓ CONSGUI EXECUTAR COM O MD DO WINDOWS 

 logstash -f config/bancocliente.conf



### Cirando o index

Substitua o arquivo anterior por esse na parte de output




output {
   elasticsearch {
      hosts => "localhost"
      index => "financeiro"
      document_type => "bancario_cliente"
   }
   stdout{}
}

## kibana

depois exccute jibana.bat em 5601

http://localhost:5601/

tambem demoar para subir
