# Machine Learning em e Docker

## O que estudaremos

Nesse e  nos próximos capítulos. Estudaremos além do Docker, Kubernete e GCP
+ Será praticamente um curso em Docker
+ Estudaremos a diferença entre Containers e Dockers
+ Estudaremos Kubernetes para orquestrar vários Dockers
+ E por fim, estudar ML e IA implantado ao Docker



## PARTE 1 - Conceito Docker

### O que é um Container

Em um dado momento, as empresa usavam uma máquina para cada software. Em larga escala, n-softwares, n-maquinas. Isso se mostrou inviável pois não havia dinheiro nem espaço físico.

Então um dia alguém pensou 

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-09-01.png)
Aí surgiu o conceito de máquina virtual: uma máquina que simula outros SistemaOperacional, assim daria para rodar 6 sistemas numa máquina só.

Mas a máquina virtual consome uma fatia do hardware, limitando a quantidade de VMs que podemos criar. Outro detalhe, ao criar uma VM podemos desperdiçar recursos se as VMs não forem bem dimensionadas. Será que na prática, você é capaz mesmo de estimular o quanto de recurso vai custar sua aplicação.
+ Ex: se rodo 4 VM e eu divido ela em 25% de ram/cpu para cada,será que estou utilizando de forma otimizada.

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-09-02.png)
Sim, o que vamos chamar de container.

**AGORA NÃO VAMOS SIMULAR N SOS DIFERENTES. VAMOS FATIAR O PRÓPRIO SO. ASSIM OS N CONTAINER COMPARTILHAM O MESMO MEMORY/CPU/STORAGE, ENQUANTO QUE NA VIRTUALIZAÇÃO ISSO É DIVIDIDO**

Dessa forma, eu tenho uma alocação de recursos mais eficaz. Pois agora não requer fatiar o hardware

**O que é container**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-09-03.png)
Na prática é uma máquina virtual, mas de forma mais inteligente

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-09-04.png)
Cada container é isolado. Além disso: O CONTAINER [É MAIS LEVE QUE A MÁQUINA VIRTUAL

### O que é o Docker

LEIA ATENTAMENTE A DEFINIÇÃO DO Docker A SEGUIR

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-09-05.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-09-06.png)
### Benefícios do Docker

Vamos diferenciar algumas coisas. Há a empresa Docker e o Software Docker

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-09-07.png)
![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-09-08.png)

## PARTE 2 - Instalar e Executar Docker

### Instalar Docker

**INFELIZMENTE, TANTO NO MAC-OS QUANTO NO WINDOWS É NECESSÁRIO FAZER CONFIGURAÇÕES MAIS PROFUNDAS PARA O Docker FUNCIONAR**

NO CURSO FAREMOS SOBRE UMA VM DO UBUNTU.

Boa parte da infra estrutura hoje em 2021 é tudo feita para linux

### Hello World com Docker

Checar se o Docker está funcionando:
````
$ sudo systemctl status Docker
````

Fazer o pull de uma imagem docker
````
$ Docker pull hello-world
````
+ Ele verifica se já existe essa imagem localmente. Se não existir, vai até o Docker Hub e faz o download do template

````
$ Docker run hello-world
````
+ A imagem foi baixada e pode ser executada com o código acima
+ Deve então aparecer uma mensagem indicando que o Docker foi instalado com sucesso

### Definir alguns conceitos

A arquitetura do Docker é como na imagem a seguir:

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-09-09.png)
**Docker engine**

+ o motor de execução no Docker. É o Docker Daemon. Ele roda no modelo cliente-servidor via terminal ou API

**Docker Image**

+ É como se fosse o código fonte dos containers

**Docker Registries**

+ É onde fica armazenado as imagens
+ Ex de Docker Registre Público: Docker hub

**Docker Containers**

+ unidades organizacionais do Docker. É a execução da imagem

**Volumes**

+ Diretório fora do container Docker (não entendi, aula 165) nos 4 min
+ é a persistência do Docker.. Nem sempre utilizamos

Como é então na realidade o funcionamento do Docker

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-09-10.png)
### Comandos

Ver as imagens  na minha maquinas

```
$ sudo Docker image ls
```

ver os container em execução

```
$ sudo Docker container ls
```

ou `Docker ps`

ver os container Docker que foram criados antes

```
$ sudo Docker container ls -a
```



### Provando que o docker é volátil

```
$ sudo Docker container run -it centos
```

Vamos executar o container Docker no modo interativos para o sistema Operacional CentoOS

Ao executar, ele não vai encontrar a imagem localmente, então ele vai e baixa ela

Vai abrir um terminal. se você executar `Docker container ls` você vai ver que o centOS está funcionando.

No modo interativo, crie um arquivo e sai com o comando `exit`.Se executar de novo, não vai aparecer o arquivo.

Para persistência há duas coisa que pode ser feita
+ adicionar VOLUMES
+ Fazer um commit de um container (você vai substituir sua imagem original pela  nova versão)

### Docker no daemon (background)

Antes executamos o Docker no modo interativo, mas na prática. Vamos mais executar ele no modo de background.

Há duas formas

```
CTRL+P+Q
```

Para entrar de volta no modo interativo: 

`sudo Docker container attach id_do_Docker`

ou executar como `Docker

### Checar consumo do container

```
$ Docker container stats
```

Vai inicializar um painel (parecido com o comando 'top' do linux'



### Para inicializar e remover containers

Para um container em execução (stop)

```
$ sudo Docker container stop id+do_container_Docker
```



+ obs: quando você para um container Docker, é como se ele fosse no modo pausado. Você pode voltar a executar o container a qualquer momentos

Inicialização (start)

```
$ sudo Docker container start  id+do_container_Docker
```

Remover completamente o container/imagem Docker (rm)

```
$ sudo Docker container rm  id+do_container_Docker
```


+ Isso remove o container do status de pausados, do tatus em que aparece em sudo Docker ps -a
+ A imagem não é deletado, então, a qualquer momento posso subir de novo

### Configurando CPU e Memória para Containers Docker

Se você não mudar as configurações, o Docker pode consumir toda a Memory/CPU da máquina em que se está


Executar comando Docker e lhe dar um nome
````
$ Docker container run -it --name teste1 debian
````
+ ONDE: debian é a imagem e teste1 o nome que vamos dá-lo.
+ A imagem e o nome são coisas diferente, consulte o comando `sudo Docker ps` que mostra essa diferença
+ Por default, o Docker atribui  nomes aleatórios

````
$ Docker container inspect teste1
````
+ Vou inspecionar o container em execução.
+ Acontece que isso mostra muita coisa, e eu quero procurar algumas só então vamos usar o comando a seguir

````
$ Docker container inspect teste1 | grep -i mem
````
+ Vai buscar o `inpsect` para memória. DEverá retornar tudo zero, indicando que não há limite para o uso de memória

Para limitar basta executar de forma diferente


````
$ Docker container run -it -m 512M --name teste2 debian
````
+ Vai mostrar uma mensagem de Warning, falando da memória swap. Na verdade há mais alguns passos para configurar 100% a memória mas não vamos ver. Só isso já é mais do que o suficiente
+ Se chegar ao limite, você pode usar  `Docker update` para mudar o uso de memória durante execução e em tempo real

**LIMITAR USO DE CPU**

````
$ Docker container run -it --cpus=0.5 --name teste3 debian
````

+ Utilize metade da capacidade de CPU

ver essa mudança do limite de uso da cpu

````
$ Docker container inspect teste3 | grep -i cpu
````
+ vai aparecer em "NanoCpu"

### Construir Imagens com Docker File

A imagem Docker é um template para construir um container.

Ex: criar uma imagem de OS ubuntu, com servidor web e já um modelo de mal treinado

**Assim, para usar a aplicação, basta subir o container**

O Dockerfile tem uma série de comandos de shell Script 

Crie o arquivo `Dockerfile`. Ele não tem extensão.

````dockerfile
FROM ubuntu % Vai buscar a imagem base com o sistema do ubuntu

RUN apt-get update % vai rodar esse comandos, ou seja, atualizar as dependências

RUN apt-get install -y ngix % colocamos a flag -y, pois vai perguntar se quer confirmar a instalação do pacotes. Ai diz que yes
````

**COMO CONSTRUIR A imagem**

Executamos no mesmo diretório de onde está o Dockerfile, por isso utilizamos `.`

````
$ Docker build -t name-of-web-server .
````

### Configurar host e subir nginx

Vamos executar o container Docker no modo daemon/background

```
$ Docker run -d -p 8080:80 name-of-web-server /usr/sbin/nginx -g "deamon off"
```


+ Na minha máquina local, que está usando o Docker, ele vai subir o container  Docker na porta 8080,  e será redirecionada para a porta 80 de dentro do container.
+ Dividindo assim em pequenas partes
  - Docker run : executar container
  - -d = modo daemons/backgroun
  - name-of-web-sever = qual imagem vou executar
  - -p 8080:80 = mapeia da mina porta 808- para a porta 80 de dentro do container
  - /usr/sbin/nginx = executa o nginx
  - -g "daemon off;" = não quero o nginx no modo de comando

aí, basta então executar localhost:8080 na sua máquina local que vai levar ao nginx do Docker

**tentando curl**

curl significa cliente URL

Serve para testar api / container docker

na máquina local 

````
$ curl -IL http://localhost:8080
````

Se retorna status=200, significa que está funcionando

### Mapear a porta pelo Dockerfile

Vamos especificar que será na porta 80 internamente do container, mas que o Docker escolha a porta aleatório na máquina local

Vamos por no Dockerfile (Adicionando)

````
EXPOSE 80
````

Como você alterou o Dockerfile, é necessário fazer um rebuild. Isso é feito com

````
$ Docker build -t web-serve .
````

Qualquer container gerado agora nessa imagem já vai está com essas modificações

Assim o comando deverá ser diferente

````
$ Docker run -d -P name-of-web-server /usr/sbin/nginx -g "deamon off;
````
+ Usamos -P maiúsculo para que O Docker ESCOLHA UMA PORTA ALEATÓRIAS
+ Aí para ver qual porta foi, busco pela parte de PORTS no comando `Docker ps`

### Configurando acesso direto ao container

Como o usuário acessa o servidor no container.

**ELE VAI FAZER DO SEU MAC-OS, pois o Docker está rodando numa VM do ubuntu**

Para fazer isso, preciso saber o IP do server onde está o Docker

````
$ ifconfig
````

Procure o IP da primeira que não seja do Docker

Exemplo: 
````
$ curl -IL http://10.211.55.7:32768
````

A aplicação está disponível mesmo na web.

Só que, dessa forma, estou acessando a máquina host do Docker, e dela, para o Docker em si. **COMO FAZER PRA ACESSAR DIRETAMENTE O Docker**

Quando fez ifconfig até apareceu um endereço do Docker, você pode tentar usá-lo mas não vai dar certo, porque NÃO CONFIGUROU PARA USAR IP DO Docker PARA PERMITIR ACESSO DIRETAMENTE.

AJUSTES NA IMAGEM:

Vou indicar uma diretiva para um arquivo de configurações.

No Dockerfile, vamos adicionar o trecho a seguir antes de EXPOSE 80

````
ADD servidor /etc/nginx/sites-enabled/default
````

O que faz:
+ Quando fizer o build, vai mandar o arquivo `servidor` da minha máquina host para o diretório a seguir do Docker. E seu nome será `default` que é a ultima parte do diretório
  - de nome servidor vai virar default dentro do docker
+ O arquivo `servidor` não precisa de extensão. E ele será um arquivo no mesmo diretório que o DockerFile

Abrir um arquivo `servidor` e vamos configurar acesso a IP

````
server {
	listen 80 default_server;
	server_name localhost;
	root /usr/share/nginx/html;
	index index.html index.htm;
}
````

Assim, quando subir o nginx, ele vai ler esse arquivo por default.

Dessa forma não preciso usar `-P`, pois não vai fazer mapeamento de portas, pois já fiz no arquivo de configuração

````
$ Docker run -d name-of-web-server /usr/sbin/nginx -g "deamon off;
````

Agora podemos acessar o Docker de forma direto, via IP.

Buscando o IP.

````
$ Docker ps
````

Buscamos primeiro o ID e depois

````
$ Docker inspect id_bizarro
````

```` 
$ Docker ps | grep IPAddress
````

agora testo (tanto no ubuntu (VM) quanto no MacOS)

```` 
$ curl -IL http://172.17.0.3
````

**INFELIZMENTE NÃO VAI DAR CERTO, POIS HÁ IP PÚBLICO E PRIVADO, E NÃO CONFIGURAMOS ESSAS COISA**

IP Público: se comunica com o mundo todo
IP Privado: que se comunica no mesmo modem.

O Docker vai criar um Ip privado, que não permite acesso de forma.

Devemos conectar nosso container a rede Docker, que é do tipo que permite acesso externo. Por default, a network que o Docker pega é o 'bridge', por isso, vamos explicitar para pegar o 'host'

````
$ Docker run --network host -d name-of-web-server /usr/sbin/nginx -g "daemon off;
````

Eu estou tornando meu Docker público e usando o IP da máquina host (UBUNTU). Esse processo é chamado de bind. Dessa forma vou poder acessar do MacOS

Então eu acesos usando o IP da máquina host (ubuntu)

```` 
$ curl -IL http://172.17.0.3
````

Não precisa dizer porta 80 pois é o padrão. 

### Usando Volumes

O Docker é volátil,  mas podemos trabalhar com volume para persistência.

volumes são **UM DIRETÓRIO COMPARTILHADO ENTRE A MAQUINA HOST E O CONTAINER Docker.**pode ser até mesmo para mais de um container Docker.

Isso é interessante para quando se trabalha em cluster.

**COMO ADICIONAR UM VOLUMES**

Cria um diretório, em qualquer lugar.

Nosso servidor nginx pega os arquivos html do seguinte códigos do `servidor` `root /urs/share/nginx/html`. **AO INVÉS DE BUSCAR DAÍ, VAMOS FAZER COM QUE PEGUE DE UM VOLUME**

Isso é super simples

````
$ Docker run --network host -d -v /home/dnpm/appweb:/usr/share/nginx/html:ro webserver /usr/sbin/nginx -g "daemon off;
````

Estou especificando para que o Docker `/home/dnpm/appweb`  quando acessar `/usr/share/nginx/html`, e para ser READ-ONLY (por isso o :ro)

Assim usa o `curl` sem o `-IL` (o IL serve pra ver o códigos status 200) e assim, ao acessar o nginx, vai ler o arquivo html que está lá

**ASSIM,ASSOCIEI UM DIRETÓRIO LOCAL AO Docker, E ELE É CAPAZ DE LER**. Posso subir mais de um container para mapear o mesmo diretorio


## PARTE 3 - Conceitos do ambiente Docker

### Orquestração de Containers

Abstração: Imagine que você tem 3 banco de dados, 1 front, 1 back, 1 banco de dados utilizando micro-serviços.
+ O usuário se conecta ao front e dai, o front se liga com o back e com o banco

Acontece que preciso me preocupar com o deploy: cuidar da operação de modo geral. A cada atualização em cada um desses componentes tenho que subir o Docker denovo

Escalabilidade: se precisar então de mais containers para suportar o tráfego, então precisaria, de por exemplo, mais 3 instâncias desse 3 containers Dockers.

E ainda vou ter que me preocupar com volumes

Balanceamento de carga: E se precisar de balanceamento de carga, vou ter que ligar a 4 containers (round-balance)

Monitoramento: Tenho que olhar ainda o monitoramento.

**ORQUESTRAÇÃO: GERENCIAR TUDO ISSO DE UMA ÚNICA FORMA**

![](/home/rhavel/Documentos/STUDY-PROJECTS/data-engineering-study/ds-academy/formacao-data-enginner/course-04-ml-in-cluster/imgs/img-c4-09-11.png)
Ferramentas
+ Kubernetes (google)
+ Docker Swarm (da Docker)

+ **Docker Compose**: subir e gerenciar mais de um container ao mesmo tempo

### Kubernetes

A solução mais utilizada. foi desenvolvido pela mesma equipe do TensorFlow

Serve para: automatizar o deploy

### Docker Swarm

Solução da empresa Docker.

Não é exatamente como os kubernetes, mas fazem as mesmas coisas.

### Docker Compose

Não é uma plataforma para fazer o mesmo que o kubernetes/Docker Swarm mas ajuda a gerenciar containers.

Serve para centralizar a criação de imagens.

**EXECUTAR APLICAÇÕES Dockers QUE USAM MAIS DE UM CONTAINER**

Serve para subir e desce N containers ao mesmo tempo. É como se fosse um super-Dockerfile que vai subir mais de um container ao mesmo tempo.;




