# ML e Docker - Parte 2 - Deploy em Docker e Flask

## Resumo do que será

+ 1 - Criar modelo de ML; Criar servidor Flask e executar os dois juntos localmente
+ 2 - Executar o servidor Flask no Docker localmente

## O que será feito nesse e no próximo cap

Deploys de uma app em micro-serviços de um modelo ML de tensor flow, tanto localmente com docker, como também em nuvem com kubernetes. Será um projeto inteiro.

SERÃO VÁRIOS COMANDOS PARA DIVERSAS PLATAFORMAS DIFERENTES. Há todos os scripts já separados

**Projeto**
+  Solução para prever o tipo de planta com base em características da planta 
  - Vai haver um modelo de ML (Tensor Flow)


![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-10-01.png)
**Conceitos docker**
+ DockerFIle: Série de comandos para criar Imagem
+ Imagem: Pense em imagem como o formato ISO de um CD
+ Container: A imagem em execução (instância de uma imagem) e pode fazer em portas diferentes

## Frameworks de ML e DL

ML: Machine Learning; DL: Deep Learning

Frameworks: Software que facilita a nossa vida, no caso criar um modelo.

+ Tensor Flow: É praticamente um padrão de mercado
+ scikit-learn: Foco em Machine Learning, modelos mais simples
+ PyTroch: foco maior em pesquisa. É mais recente e carece de algumas ferramentas para deploy

### Treinar e Salvar modelo

Vamos usar tensor flow, e será algo simples mesmo que seja usando o tensor Flow.

De preferência, não atualize o avançado, delete ele e instalei de volta depois

Em primeiro lugar,baixe as versões específicas do vídeo

O nosso modelo é um arquivo de extensão '.h5' que tem os pesos

### Código para treinar e gerar modelo

````python
# Modelo de Deep Learning

# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada:', python_version())

# Para atualizar um pacote, execute o comando abaixo no terminal ou prompt de comando:
# pip install -U nome_pacote

# Para instalar a versão exata de um pacote, execute o comando abaixo no terminal ou prompt de comando:
# pip install nome_pacote==versão_desejada

# Imports
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Nomes das colunas
nomes_colunas = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

# Dataset
# https://archive.ics.uci.edu/ml/datasets/Iris
dados = pd.read_csv('https://raw.githubusercontent.com/dsacademybr/Datasets/master/dataset3.csv', names = nomes_colunas, header = 0)

# Separa as variáveis de entrada e saída
saida = dados["Species"].astype("category")
entrada = dados.drop("Species", axis = 1)

# Encoding da variável target (conversão de texto para número)
dataEncoder = LabelEncoder()
saida_num = dataEncoder.fit_transform(saida)

# Divide os dados em treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(entrada, saida_num, test_size = 0.3, random_state = 42)

# Converte a variável de saída em tipo categórico
y_treino = to_categorical(y_treino)
y_teste = to_categorical(y_teste)

# Modelo de Deep Learning
modelo = Sequential()
modelo.add(Dense(10, input_dim = 4, activation = 'relu'))
modelo.add(Dense(10, activation = 'relu'))
modelo.add(Dense(3, activation = 'softmax'))

# Compilação do modelo
modelo.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# Treinamento do modelo
modelo.fit(X_treino, y_treino, epochs = 300, batch_size = 10)

# Avalia o modelo
scores = modelo.evaluate(X_teste, y_teste)
print("\nAcurácia: %.2f%%" % (scores[1]*100))

# Salva o modelo
modelo.save('modelos/modelo1.h5')
````

Você como engenheiro de dados deve receber esse arquivo .h5

### Servir Modelo via APP WEB

Vamos usar REST API. Não é muito ideal para escalabilidade, mas como é algo pequeno serve.

Utilizaremos Flaks para subir um WebServer e REST API

Neste caso, tanto o back-end quanto o front-end estão no flask. Assim, há uma página de front-end que é fornecida pelo Flask

````python
#app.py do flask

# Aplicação Web e API REST

# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada:', python_version())

# Para atualizar um pacote, execute o comando abaixo no terminal ou prompt de comando:
# pip install -U nome_pacote

# Para instalar a versão exata de um pacote, execute o comando abaixo no terminal ou prompt de comando:
# pip install nome_pacote==versão_desejada

# Imports
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template
from tensorflow.keras import backend
from tensorflow.keras.models import load_model

# Cria o objeto da app
app = Flask(__name__)

# Carrega o modelo treinado
@app.before_first_request
def load_model_to_app():
    app.predictor = load_model('./static/model/modelo1.h5')
    
# Responde às requisições para o diretório raiz (/) com index.html
@app.route("/")
def index():
    return render_template('index.html', pred = " ")

# Para as previsões usamos o método POST para enviar as variáveis de entrada ao modelo
@app.route('/predict', methods = ['POST'])
def predict():

    # Objeto com as variáveis de entrada que vieram a através do formulário
    data = [request.form['sepal_length'],
            request.form['sepal_width'],
            request.form['petal_length'], 
            request.form['petal_width']]

    # Converte para o tipo array
    data = np.array([np.asarray(data, dtype = float)])

    # Coleta as previsões
    predictions = app.predictor.predict(data)
    print('\nPrevisões de Probabilidades: {}'.format(predictions))

    # Como são retornadas probabilidades, extraímos a maior, que indica a categoria da planta
    tipo = np.where(predictions == np.amax(predictions, axis = 1))[1][0]
    print('\nPrevisão de Classe:', tipo)

    if tipo == 0:
        pred_planta = 'Setosa'

    if tipo == 1:
        pred_planta = 'Versicolor'

    if tipo == 2:
        pred_planta = 'Virginica'

    # Entrega na página web as previsões
    return render_template('index.html', pred = pred_planta)

# Função main para execução do programa
def main():
    app.run(host = '0.0.0.0', port = 8080, debug = False)  


# Execução do programa
if __name__ == '__main__':
    main()
````

## Usando Docker

Flask nem de longe é escalável. Podemos usar Docker e TensorFlowServing 

**VAMOS USAR OUTRA ARQUITETURA**


![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-10-02.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-10-03.png)
O TensorFlowServing faz uma política e gerenciamento já altomático.

Além do mais, os modelos tem versões. Ex: A amazon refaz seu modelo todo dia de noite.

O tensorFLow serving serve para orquestrar isso.

### Porque usamos tensorFLow Serving

```
Servir modelos de aprendizado de máquina de maneira rápida e fácil é um dos principais
desafios ao passar da experimentação para a produção. Servir modelos de aprendizado de
máquina é o processo de pegar um modelo treinado e disponibilizá-lo para atender a
solicitações de previsão. Ao servir na produção, você deseja garantir que seu ambiente seja
reproduzível, imponha isolamento e seja seguro. Para esse fim, uma das maneiras mais fáceis
de servir os modelos de aprendizado de máquina usando o TensorFlow Serving com o Docker.
O Docker é uma ferramenta que empacota o software em unidades chamadas contêineres que
incluem tudo o que é necessário para executar o software.

O TensorFlow Serving é um sistema de alto desempenho para “servir” (públicar)

modelos de aprendizado de máquina, projetado para ambientes de produção. O TensorFlow
Serving facilita a implantação de novos algoritmos e experimentos, mantendo a mesma
arquitetura de servidor e APIs.

O TensorFlow Serving fornece integração pronta para uso com os modelos TensorFlow,

mas pode ser estendido para atender outros tipos de modelos e dados.
```



### DockerFiles

Usaremos 3 containers Docker

+ 1 - Só onde vai ter a app web
+ 2 - Vai ter o TensorFlow para treinar e gerar o modelo
+ 3 - TensorFlowServing

Baixar imagem do ubuntu

```
$ docker pull ubuntu
```


```
$ docker pull tensorflow/tensorflow
```


+ vai baixar e gerar uma imagem já pronta para ser subida

```
$ docker pull tensorflow/serving
```



### Arquivos para o docker

`requirements.txt`: tem a lista de pacotes necessaŕias

`dockerfile`: Arquivo template para criar imagem Docker

````shell
# Inicia imagem do Ubuntu 18.04
FROM ubuntu:18.04

# Install pipenv
RUN apt-get update
RUN apt-get install -y build-essential python3.7 python3.7-dev python3-pip python3.7-venv

# Cria a pasta de trabalho
RUN set -ex && mkdir /app
WORKDIR /app

# Copia a pasta com a app
COPY . /app

# Instala as dependências
RUN set -ex && pip3 install -r requirements.txt

# Executa o servidor web
EXPOSE 8080
ENV PYTHONPATH /app
CMD python3 app.py

````


Sequência de comandos (build.txt)

````shell
# Cria a imagem:
sudo docker build -t appweb  -f Dockerfile .

# Executa o container mantendo o log de execução (boa opção para debug):
docker run -p 80:8080 appweb

# Executa o container em modo interativo:
docker run --name appweb1 -it appweb

# Executa o container em background:
docker run -d -p 80:8080 appweb

########### Comandos auxiliares ####################

# Visualiza container em execução: sudo docker ps -a
# Remove container: sudo docker rm -f <id-container>

# Visualizar imagens criadas: sudo docker images
# Remove imagem: sudo docker rmi <id-imagem>
## Executar container docker e ver a aplicação
````




















