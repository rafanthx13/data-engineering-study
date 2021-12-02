# Micro serviços 2 - DOcker

## Resumo

**O que vamos fazer**

+ Estudar o DOcker par ao deply
  - Dentor dele vai ter um modelo de ML: Python e Scikit-learning
  - O modelo deve receber requisçoes e responder com gRPC

+ Parte de ML
  - Teriner modelo de ML
  - Gravar modelo de ML em um arquivo (persistesncia)
  - Definir protocolo de comunicaç (gRPC)
  - Criar codigo GRPC em pytohn e implementar servidor gRPC
  - Implementarcliente gRPC
  - Criar imagem Dcker
  - Executar conteinr dokcer
  - Tetsar a aplicaçao
  - Usar a aplicaçao

+ Tudo será feito em Linux. Boa parte disso e do IA funciona só no ambiente WIndows nem MacOS

## O nosso problema de negoicio

img-c4-08-01

img-c4-08-02

Vamos usar o UNBUNTU

## PARTE 1 - Docker

### Instalr e confi lubunut

````
$ 
````

````
$  sudo apt-get update

### Instalar DOcker


Instalar
````
$ sudo apt-get install docker.io
````

Executar
````
$ sudo systemctl start docker
````

Com esse comando, toda ve z que reiniciar sua maquina ja'vai subir o docker
````
$ sudo systemctl enable docker
````

Ver versao do docker
````
$ sudo docker version

## Criando modelo

usamos a lib `joblib` para salvar em formato `.pickle`. Treniamos e salvamos em arquvio
````

### Porque usar gRPC ao invez do REST

img-c4-08-03

O JSON acaba sendo mais lento do que outros protoclos, alem de quem, REST fica mutio exposto.

**USAMOS GRPC QUANDO ENTRE DE MICRO-SERVIÇO PARA MICRO-SERVIÇO, SE ENVOLVER ALGO EXTERNO, O REST É EMHLO. A saida do REST é melhor para quanse se consome numa pagina web. Agora se for de um  bacnk-end java para um micro-seviçod e IA, ai usamos gRPC por exmeplo**

img-c4-08-04

Em suma: por causa

img-c4-08-05

img-c4-08-07

O que é gRPC: XML mais rapido e simples do google

### gRPC e protocol Buffers


img-c4-08-09

img-c4-08-10

Ou seja: definsmo um arquiv `.proto` 	que vai ter o template do que manda e recebe de dados pelo gRPC.

o gRPC é manis binario, por isos mais rapido mas piro paara ser lido por humanos. ENtao nao é recomanedado para ser um api de front-end

img-c4-08-11

### arquivo proto

Estrutura para realizar a comunicaçao entre serviços

````
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

%# defino response (oconvertermos calses para valore snueriso 0/1/2das 3 clases de iris)
message IrisPredictReply {
  int32 species = 1;
}
````

### Geranco clsses grpc em Pthon 

**COMPILAR**

````
pip install grpcio
pip install grpcio.tools
````

Depois executa o codegen.py

````
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

grpc_server.py

````# Cria o servidor gRPC

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
## Extendo da clase gerado do arquivo .proto
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
    server.add_insecure_port('[::]:50052') # quero nessa porta, esse numero eh aleartorio
    server.start() 
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS) # fique ligado por 24horas
    except KeyboardInterrupt: # se voce der CTRL+C para tudo
        server.stop(0)

# Execução do programa
if __name__ == '__main__':
    serve()

````

### IMplementando cliente gRPC

Ele envia um request passando 4 variavei preditoras

````
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

    # Envia a request e obtém a previsão
    response = stub.PredictIrisSpecies(request)
    print("Número da previsão da classe prevista para a flor: " + str(response.species))

# Executa
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help='Nome da máquina', default='localhost', type=str)
    parser.add_argument('--port', help='Porta', default=50052, type=int)
    args = parser.parse_args()
    run(args.host, args.port)
````

### Tetando

$ grpc_serve.py

crie outra tab e execute o client em outro temrinal

## PARTE 2 - Docker para gRPC

DOckerFIle: COnjunto de instruçôes do docker para criar um continaer

````
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

Cria a imagem com o comando a seguir. Vai pegar o conteud do DOckerfile no pwd de ons estiver e fazer o build

````
$ sudo docker build . -t iris-predictor
````

````
$ sudo docker images
````

**REVER MAIS AS ULTIMAS 4 AULAS QUE EELE USTILIZA O DOKCER. VAI GERA RUM ARQUIVO GRANDE PRA MINHA MAQUINA, TENHOQ UE EESPCIFICAR OUTRO LOCAL PAR ANAO FICAR PESADO**
