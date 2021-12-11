pip install prefect -U

API key até 31/12
w98qAoZuh4bXlrIk38Lc2A

registrar

$ prefect auth login --key w98qAoZuh4bXlrIk38Lc2A

Criar projeto com prefect LI

$ prefect create project "Hello, World!"

Vai criar o proeto na cloud

Esse código degistra esse dataWorkflow no meu cloud, em 1FirstProject' que ja deve está criado

````
import prefect
from prefect import task, Flow

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

flow = Flow("hello-flow", tasks=[hello_task])

flow.register(project_name="FirstProject")


````

Your flow is now registered with Prefect Cloud.


Before running the server for the first time, run prefect backend server to configure Prefect for local orchestration. Please note the server requires Docker and Docker Compose to be running.

To start the server, UI, and all required infrastructure, run:

prefect server start
