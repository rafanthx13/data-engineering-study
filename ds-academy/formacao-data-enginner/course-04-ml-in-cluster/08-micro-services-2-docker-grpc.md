# Micro serviços 2 - Docker

## Resumo

**O que vamos fazer**

+ Estudar o Docker para o deploy
  - Dentro dele vai ter um modelo de ML: Python e Scikit-learning
  - O modelo deve receber requisçoes e responder com gRPC

+ Parte de ML
  - Treinar modelo de ML
  - Gravar modelo de ML em um arquivo (persistência)
  - Definir protocolo de comunicação (gRPC)
  - Criar códigos GRPC em python e implementar servidor gRPC
  - Implementar cliente gRPC
  - Criar imagem Docker
  - Executar container docker
  - Testar a aplicação
  - Usar a aplicação

+ Tudo será feito em Linux. Boa parte disso e do IA funciona só no ambiente Windows nem MacOS

## O nosso problema de negócio

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-08-01.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-08-02.png)
Vamos usar o UBUNTU

## PARTE 1 - Docker

### Instalação e configurar ubuntu



````shell
# Atualizar pacotes Ubuntu
$  sudo apt-get update

# Instalar Docker
$ sudo apt-get install Docker.io

# Executar
$ sudo systemctl start Docker

# Com esse comando, toda vez que reiniciar sua máquina já vai subir o Docker
$ sudo systemctl enable Docker

# Ver versão do Docker
$ sudo Docker version
````

### Criando modelo

usamos a lib `joblib` para salvar em formato `.pickle`. Treinamos e salvamos em arquivo

```python
# file: cria_modelo_ml.py
# Criação do Modelo de Machine Learning

# Imports
import joblib
from sklearn import datasets
from sklearn import svm

# Carrega o dataset
iris = datasets.load_iris()

# Divide os dados em entrada e saída para aprendizagem supervisionada
X, y = iris.data, iris.target

# Cria e treina o modelo
modelo = svm.LinearSVC(max_iter=10000)
modelo.fit(X, y)

# Grava o modelo
joblib.dump(modelo, 'modeloml1.pickle')
```




### Porque usar gRPC ao invés do REST

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-08-03.png)
O JSON acaba sendo mais lento do que outros protocolos, além de que o REST fica muito exposto.

**USAMOS GRPC QUANDO ENTRE DE MICRO-SERVIÇO PARA MICRO-SERVIÇO, SE ENVOLVER ALGO EXTERNO, O REST É MELHOR. A saída do REST é melhor para quando se consome numa página web. Agora se for de um  back-end java para um micro-serviços e IA, ai usamos gRPC por exemplo**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-08-04.png)
Em suma: por causa

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-08-05.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-08-07.png)
O que é gRPC: XML mais rápido e simples do google

### gRPC e protocol Buffers


![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-08-09.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-08-10.png)
Ou seja: definimos um arquivo `.proto` 	que vai ter o template do que manda e recebe de dados pelo gRPC.

o gRPC é mais binário, por isso mais rápido mas pior para ser lido por humanos. Então não é recomendado para ser um api de front-end

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-08-11.png)
### arquivo proto

Estrutura para realizar a comunicação entre serviços

````python
%# file: iris.proto

%# tudo e default
syntax = "proto3";

option java_multiple_files = true;
option java_package = "io.grpc.examples.ml";
option java_outer_classname = "IrisProto";
option objc_class_prefix = "HLW";

package ml;

%# defino serviço
service IrisPredictor {
  rpc PredictIrisSpecies (IrisPredictRequest) returns (IrisPredictReply) {}
}

%# defino a request
message IrisPredictRequest {
  double sepal_length = 1;
  double sepal_width = 2;
  double petal_length = 3;
  double petal_width = 4;
}

%# defino response (convertermos clases para valore como 0/1/2 das 3 classes de íris)
message IrisPredictReply {
  int32 species = 1;
}
````

### Gerando classes grpc em Python 

**COMPILAR**

````shell
pip install grpcio
pip install grpcio.tools
````

Depois executa o `codegen.py`

````python
# file: codegen.py
from grpc.tools import protoc

protoc.main(
    (
        '',
        '-I.',
        '--python_out=.',
        '--grpc_python_out=.',
        './iris.proto',
    )
)
````

e vai gera 2 arquivos `iris_pb2.py` `iris_pb2_grpc.py`

### implementar servidor rpc

`grpc_server.py`

````python
# file: grpc_server.py
# Cria o servidor gRPC

# Imports
import os
import grpc
import time
import joblib
from concurrent import futures
from pprint import pprint

# Import dos módulos gerados a partir da compilação do arquivo proto
import iris_pb2
import iris_pb2_grpc

# Variável para definir o número de segundos por dia
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# Cria uma classe carregar o modelo
## Estendo da classe gerado do arquivo .proto
class IrisPredictor(iris_pb2_grpc.IrisPredictorServicer):
    _model = None

    @classmethod
    
    # Obtém o modelo de ML
    def get_model(cls):
        if cls._model is None:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modeloml1.pickle')
            cls._model = joblib.load(path)
        return cls._model
    
    # Função para fazer as previsões
    def PredictIrisSpecies(self, request):
        model = self.__class__.get_model()
        sepal_length = request.sepal_length
        sepal_width = request.sepal_width
        petal_length = request.petal_length
        petal_width = request.petal_width
        
        # Previsão do modelo
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        
        return iris_pb2.IrisPredictReply(species=result[0])

# Função para servir o modelo na porta 50052
def serve():
	# Envolve Infra e Theads
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    iris_pb2_grpc.add_IrisPredictorServicer_to_server(IrisPredictor(), server)
    server.add_insecure_port('[::]:50052') # quero nessa porta, esse número é aleatório
    server.start() 
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS) # fique ligado por 24 horas
    except KeyboardInterrupt: # se você der CTRL+C para tudo
        server.stop(0)

# Execução do programa
if __name__ == '__main__':
    serve()

````

### Implementando cliente gRPC

Ele envia um request passando 4 variável preditoras

````python
# file: grpc_client.py
# Cria o cliente gRPC

# Imports
import grpc
import argparse

# Import do módulo gerado a partir da compilação do arquivo proto
import iris_pb2

# Import to grcp_server
import grpc_server

# Executa o cliente
def run(host, port):

    # Define a classe de previsão
    stub = grpc_server.IrisPredictor()
    
    # Prepara uma request
    request = iris_pb2.IrisPredictRequest(
        sepal_length = 5.0,
        sepal_width = 3.6,
        petal_length = 1.3,
        petal_width = 0.25
    )
    
    # Enviar a request e obtém a previsão
    response = stub.PredictIrisSpecies(request)
    print("Número da previsão da classe prevista para a flor: " + str(response.species))

# Executa
if __name__ == '__main__':
    parser = argparse.ArgumntParser()
    parser.add_argumnt('--host', help='Nome da máquina', default='localhost', type=str)
    parser.add_argumnt('--port', help='Porta', default=50052, type=int)
    args = parser.parse_args()
    run(args.host, args.port)
````

### Testando

```shell
$ python grpc_serve.py
```

crie outra tab e execute o cliente em outro terminal

## PARTE 2 - Docker para gRPC

DockerFile: Conjunto de instruções do Docker para criar um container

````dockerfile
FROM ubuntu:16.04

WORKDIR /root

# Obtém a imagem do Ubuntu e as dependências
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        pkg-config \
        rsync \
        software-properties-common \
        unzip \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala o miniconda
RUN curl -LO https://repo.continuum.io/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh \
      && bash Miniconda3-4.7.12.1-Linux-x86_64.sh -p /miniconda -b \
      && rm Miniconda3-4.7.12.1-Linux-x86_64.sh
ENV PATH /miniconda/bin:$PATH

# Limpa tudo que foi executado e remove arquivos usados apenas na instalação
RUN conda clean -tp -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 50052

COPY . /root/
CMD ["python", "grpc_server.py"]

````

Cria a imagem com o comando a seguir. Vai pegar o conteúdo do Dockerfile no pwd de ons estiver e fazer o build

````
$ sudo Docker build . -t iris-predictor
````

````
$ sudo Docker images
````



### Executar Docker

```sh
# Cria a imagem docker
sudo docker build . -t iris-predictor

# Executa o container docker
sudo docker run --rm -d -p 50052:50052 --name iris-predictor iris-predictor
sudo docker run -it iris-predictor bash

# Verificando ip do container
sudo docker inspect id-container

# Executa a chamada cliente
python grpc_client.py --host 172.17.0.2 --port 50052
```

Assim, o nosso client deve conseguir se conectar com o server gRPC e entregar a resposta