# Ml e Docker - Kubernetes e GCP (Google Cloud Platform)

## Resumo do nosso projeto

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-01.png)

**Etapas**

1 - Configurar Docker (já fizemos isso, mas vamos fazer do zero, como se nunca tivéssemos configurado)

2 - Obter o modelo de ML: Isso já temos, que é o arquivo pronto

3 - Criar Container Docker: Até a etapa 3 já fizemos isso

4 - Configurar o GCP em cloud

5 - Deploys com Kubernetes (orquestrador de container)

## PARTE 1 - Configurar Docker e Container (etapas 1,2 3)

### Como configurar sua própria infraestrutura do zero

Vamos criar outra máquina Ubuntu no VirtualBox, instale ele. Use o Ubuntu 18 pois é mais estável (deve dar menos problemas do que na versão mais nova do ubuntu)

Atualizar

```shell
$ sudo apt-get update

$ sudo apt-get upgrade
```

### Instalar Docker

Vamos por nosso container na nuvem 'DockerHub' e daí vamos mandar para o GCP (Semelhante ao Git)

````shell
# Se não tiver o curl
sudo apt install curl

# Instala o Docker Community Edition (CE - COmmunity Edition)
# Vai baixar na versão mais nova e estável
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce


# Ajusta o acesso de sudo necessário para o docker
$ sudo groupadd docker
$ sudo gpasswd -a $USER docker

# CRIE uma conta no dockerHub, e aqui, vai pôr seu login:senha
# Precisaremos de uma conta Docker Hub para que mais tarde possamos enviar nossa imagem docker. Crie uma conta, se ainda não tiver uma.
# Assim que sua conta Docker Hub estiver configurada, faça login no docker:
docker login
````

### Trabalhando com TensorFlow Serving

O TensorFlow Serving é compatível apenas com o formato SavedModel, portanto, precisaremos converter qualquer modelo TensorFlow ou modelo Keras para o formato SavedModel. Aqui tem mais detalhes sobre isso: https://www.tensorflow.org/guide/saved_model

Para simplificar, faremos o download de um modelo Tensorflow pré-treinado com arquitetura ResNet.

```shell
# Crie uma pasta para gravar o modelo

mkdir /tmp/modelo

# Download do modelo ResNet pré-treinado e outras configurações pelo pip '|'
curl -s https://storage.googleapis.com/download.tensorflow.org/models/official/20181001_resnet/savedmodels/resnet_v2_fp32_savedmodel_NHWC_jpg.tar.gz | tar --strip-components=2 -C /tmp/modelo -xvz
````
### Baixar TensorFLowServing

Vamos usar um modelo já treinado e disponibilizado pela TensorFlow
````shell
# Download do Container TensorFlow para CPU
#### temos então a imagem mais nova do tensorflow-serving
docker pull tensorflow/serving:2.3.0

# Download do Container TensorFlow para GPU
# NÃO vamos usar pois na nossa máquina não vai ter GPU
# docker pull tensorflow/serving:2.3.0-gpu

# ====================
# Obs: Use APENAS uma opção ou outra acima!
# ====================


# O ponto de entrada padrão para a imagem do contêiner ‘tensorflow/serving: 2.3.0’ ou qualquer outra imagem do TF é ‘/usr/bin/tf_serving_entrypoint.sh’. 

# Estaremos criando nosso próprio tf_serving_entrypoint.sh.

# A instrução abaixo executa o Tensorflow Serving e carrega o modelo de ‘/models/resnet/’, abre a porta 8500 para gRPC e a porta 8501 para REST-API.

# Abra um editor de texto e digite:

#!/bin/bash
tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=resnet --model_base_path=/models/resnet

# Salve e então ajuste os privilégios:
chmod +x tf_serving_entrypoint.sh

# Execute o container tf/serving 
docker run -d --name=servingbase tensorflow/serving:2.3.0

# Copia o modelo para o container
docker cp /tmp/modelo/1538687457/ servingbase:/models/resnet
docker cp /tmp/modelo/1538687457/ servingbase:/models/resnet/1

# Copia o script de execução tf_serving_script.sh
docker cp tf_serving_entrypoint.sh servingbase:/usr/bin/tf_serving_entrypoint.sh

# Commit (gerar nova imagem de container: que tenha o nosso modelo já pronto)
docker commit servingbase modelo_cls_dsa:latest

# Finaliza o container (pois é o antigo, que só serviu de modelo para criar um novo container)
docker kill servingbase

# Executa a nova imagem criada
docker run -d --name=modelo_cls_dsa -p 8500:8500 -p 8501:8501 modelo_cls_dsa:latest

# Verifica se o container está em execução
docker ps

````

### Outras configurações e testar nossos container

Vamos fazer isso a partir da execução do arquivo ` cliente_cls.py`

```shell
# Teste usando GRPC
python cliente_cls.py -p 8500 -ip localhost

# Teste usando REST API
python cliente_cls.py -p 8501 -ip localhost

# Veremos que GRPC tem tempo de resposta mais rápido do que REST API.
# Uma vez implantado na nuvem, a diferença é muito maior.
# Finaliza o container
docker stop modelo_cls_dsa

# Push imagem para o Docker Hub
docker tag modelo_cls_dsa:latest DOCKERHUB_USERNAME/modelo_cls_dsa:latest
docker push DOCKERHUB_USERNAME/modelo_cls_dsa:latest
```


O arquivo `cliente_cls.py` é o seguinte:

````python
# Script para testar conexão ao TensorFlow Serving

# Imports
import grpc
import base64
import argparse
import requests
import tensorflow as tf
from datetime import datetime
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc

# Verifica a versão do TF
tf_v = 2
if tf.__version__.startswith('2'):
  import tensorflow.compat.v1 as tf
  tf.disable_v2_behavior()
else:
  tf_v = 1

# Leitura e parse dos argumentos
parser = argparse.ArgumntParser(description = '')
parser.add_argumnt('-p','--port', help = 'Porta de conexão', default = '8500')
parser.add_argumnt('-ip','--ipaddress', help = 'Endereço ip', default = 'localhost')
args = vars(parser.parse_args())

# Variáveis
SERVER_URL = 'http://ipaddress:port/v1/models/resnet:predict'
IMAGE_URL = 'https://tensorflow.org/images/blogs/serving/cat.jpg'

# Leitura da imagem de teste do modelo
dl_request = requests.get(IMAGE_URL, stream = True)
dl_request.raise_for_status()
data = dl_request.content
jpeg_bytes = base64.b64encode(data).decode('utf-8')

# Função para chamada REST-API
def restapi_call(ip_address):
  server_url = SERVER_URL.replace('ipaddress', str(ip_address))
  server_url = server_url.replace('port', '8501')

  predict_request = '{"instances" : [{"b64": "%s"}]}' % jpeg_bytes

  for _ in range(2):
    response = requests.post(server_url, data=predict_request)
    response.raise_for_status()

  num_requests = 10
  time_taken_list = []
  print("*"*30)
  print("Chamada REST API: ")
  print("*"*30)

  # Loop por 10 requisições para calcular o tempo médio
  for i in range(num_requests):
    start = datetime.now()
    response = requests.post(server_url, data = predict_request)
    time_taken = (datetime.now() - start).total_seconds()
    print(f"{i}. Tempo Gasto: {time_taken}")
    time_taken_list.append(time_taken)
  total_time = sum(time_taken_list)
  avg_time = total_time / len(time_taken_list)
  print('Tempo Médio de Processamento: ', avg_time)

# Função para chamada gRPC
def grpc_call(ip_address):
  channel = grpc.insecure_channel(f'{ip_address}:8500')
  stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
  request = predict_pb2.PredictRequest()
  request.model_spec.name = 'resnet'
  request.model_spec.signature_name = 'serving_default'
  if tf_v == 1:
    request.inputs['image_bytes'].CopyFrom(
        tf.contrib.util.make_tensor_proto(data, shape=[1]))
  if tf_v == 2:
    request.inputs['image_bytes'].CopyFrom(
        tf.make_tensor_proto(data, shape=[1]))

  for i in range(2):
    result = stub.Predict(request, 10.0)  

  num_requests = 10
  time_taken_list = []
  print("*"*30)
  print('Chamada GRPC:')
  print("*"*30)
  for i in range(num_requests):
    start = datetime.now()
    result = stub.Predict(request, 10.0) 
    time_taken = (datetime.now() - start).total_seconds()
    print(f"{i}. Tempo Gasto: {time_taken}")
    time_taken_list.append(time_taken)
  total_time = sum(time_taken_list)
  avg_time = total_time / len(time_taken_list)
  print('Tempo Médio de Processamento: ', avg_time)

# Execução do programa
if __name__ == '__main__':
  ip_address = args['ipaddress']
  port = args['port']

  if port == '8500':
    grpc_call(ip_address)
  else:
    restapi_call(ip_address)
````

Ele instala o mini anaconda e executa

+ `source .baschrc` que é para usar as variáveis de ambiente desse arquivo. É necessário fazer isso pois instalamos o python, mas as coisas de variáveis de ambiente só seriam executadas após reiniciar o PC, então, para não precisar fazer isso usamos esse comando.

Executando o códigos em python vai dar alguns problema,s pois o grpc não vem com o mini-conda

```shell
pip install grpcio
pip install tensorflow
pip install tensorflow-serving-api
```

tudo isso é para executar o arquivo no seu loca, tudo isso já está no container docker

Por fim, 10 requisições gRPC custara 0.0883437 em média para chamada de gRPC

Agora executando via PAI

0.0915725, a diferença é pouca mas é menor

## PARTE 2 - Kubernetes e GCP (Etapa 4 e 5)

Essas configurações podem ser feitas em qualquer máquina. GPC e kubernetes poderia ser em qualquer máquina e não no linux

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-02.png)
### O que é Kubernetes

Relembrando:
+ O que é um container: Uma máquina virtual super leve

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-03.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-04.png)
O que é o Kubernetes
+ Ele é como um resolvedor de tetris, ele gerencia os container e aloca os seus recursos em cada aplicação em cada container
+ O que é: Ferramenta para gerenciar os n-container de forma  otimizada em uma máquina ou mais de uma

Porque existiu kubernetes

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-05.png)
### Funcionamento do kubernetes

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-06.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-07.png)
Kubernetes permite fazer Load Balance facilmente com containers

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-08.png)
Um node pode ser tanto uma máquina física quanto um container docker

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-09.png)
**O KUBERNETES É PARA TRABALHAR COM MAIS DE UM NÓ**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-10.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-11.png)
O kubernetes foi criado uma uma REST API, então , tudo que vamos fazer para criar o cluster kubernetes são chamadas de API **EM TEMPO REAL**.



### Instalando GCP

VAMOS USAR ALGO QUE É PAGO, MAS SERÁ POUCO (Google Kubernetes Engine)

Vamos usar CLI do GCP, pois permite fazer  mais coisa (concatenar comandos) e além disso, nem sempre podemos fazer as coisa com uma UI

Para fazer isso, tem que instalar a Google CLoud SDK. Essa é a parte de configuração do GCP e criação do nosso projeto no GCP

````shell
# Instalação do Google Cloud SDK

echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

sudo apt-get install apt-transport-https ca-certificates gnupg

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

sudo apt-get update && sudo apt-get install google-cloud-sdk

gcloud init

gcloud auth login

gcloud projects create proj-deploy-tfserving

gcloud config set project proj-deploy-tfserving
````

### Instalando Kubernetes e KubeCTL

Instalando o Google SDK para entrar no GC.

AGORA VAMOS BAIXAR O kubectl para gerenciar o cluster de container

```shell
# baixar kube-ctl (linha de comando do kubernets)
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"

# dar privilégio (+x priveligeio de executável)
chmod +x ./kubectl

# mover arquivo para um local adequado
sudo mv ./kubectl /usr/local/bin/kubectl

# testar
kubectl version --client

# Ativa o Kubernetes Engine API (no GCP)
# É feito no browser. Clique enable. Será 0.10 USD por hora. COnfigura cartão de crédito
https://console.cloud.google.com/apis/api/container.googleapis.com/overview?project=proj-deploy-tfserving
```





Deverá aparecer essa tela: Coloque alerta de limite para gasto)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-11-12.png)

### Criando cluster kubernetes

Crie o cluster no site-web e dê next até está ativado. NO script a seguir está configurado para uma determinada cloud, se fizer, será outra

````shell
# Configuração do Cluster Kubernetes

# Crie o cluster no GCP conforme mostrado na aula

// logar
gcloud auth login

// buscar credenciais do nosso cluster kubernetes e por na home/.kube
gcloud container clusters get-credentials cluster-dsa --zone=us-central1-c

// buscar informações sobre o nosso cluster kubernetes. Vai informar doso os end-points necessários
kubectl cluster-info

// ATÉ AQUI, NOS NÃO DEFINISO NADA SOBRE DOCKER/CONTAINER/OU QUALQUER COISA QUE FIZEMOS ANTES, ATÉ AGORA
````

### Deployment do kubernetes

Arquivo `deployment.yaml` para deploy no docker

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: modeloclsdsa-deployment
  name: modeloclsdsa-deployment
spec:
  progressDeadlineSeconds: 2147483647
  replicas: 2
  revisionHistoryLimit: 2147483647
  selector:
    matchLabels:
      app: modeloclsdsa-deployment
  strategy:
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: modeloclsdsa-deployment
    spec:
      containers:
      - image: DOCKERHUB-USERNAME/modelo_cls_dsa:latest
        imagePullPolicy: Always
        name: modeloclsdsa-deployment
        ports:
        - containerPort: 8501
          name: restapi
          protocol: TCP
        - containerPort: 8500
          name: grpc
          protocol: TCP
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
```

OBS:
DOCKERHUB-USERNAME => Faz o replace pelo seu username no docker hub
type: RollingUpdate => Para que, ao fazer atualizações, não derrubar tudo

```shell
# executar deploy
$ kubectl apply -f deployment.yaml
```

```shell
# ver o que já está no deploy
# deve mostrar que está subido nosso cluster kubernetes
$ kubectl get deployment
```

VAI LER O ARQUIVO, BUSCAR A IMAGEM NO DOCKER-HUB E Criar o cluster kubernetes na GCP

### Configurando o cluster Kubernetes

O NOSSO CLUSTER ESTÁ SUBINDO, MAS NINGUÉM PODE ACESSÁ-LO NA INTERNET.

Vamos configurar o kubernetes , o Ingress e o Load Balance

```shell
# executar
$ kubectl apply -f service.yaml
```

Arquivo `service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    run: modeloclsdsa-service
  name: modeloclsdsa-service
spec:
  ports:
    - port: 8501
      targetPort: 8501
      name: restapi
        - port: 8500
      targetPort: 8500
      name: grpc
      selector:
            app: modeloclsdsa-deployment
      type: LoadBalancer
```

```shell
# verificar o serviço
# vamos obter o IP EndPoint para nossa aplicação, antes era o endpoint do cluster kubernetes. Demora um pouco para aparecer EXTERNAL-IP. Use ness nos IP dos trechos de código a seguir
$ kubectl get service
```



### Testando o cluster kubernetes

Vamos testar o cluster de containers gerenciados com kubernetes. Usamos `EXTERNAL-IP` do ` kubectl get service
`

Agora, já estamos executando e realmente o gRPC deu 0.3 e o API rest 0.8 de velocidade

```shell
# Teste usando GRPC (seu ip externo pode ser diferente)

python cliente_cls.py -p 8500 -ip 34.66.7.69

# Teste usando RESTAPI (seu ip externo pode ser diferente)

python cliente_cls.py -p 8501 -ip 34.66.7.69
```


## Conclusão

Por fim, construimos um Cluster com 2 containers juntos da nossa app de ML usando Kubernetes, TensorFlow Serving.

Não se esqueça de parar a máquina no GCP após terminar todo o processo.