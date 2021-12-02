# Please note, because we are running this on our local machine
# we are using the LocalDaskExecutor. There is also a DaskExecutor 
# that can be used to distribute the tasks across multiple
# machines. This is a more advanced use case that is beyond
# the scope of this blog post.

import prefect
from prefect import task, Flow
import datetime
import random
from time import sleep
from prefect.triggers import manual_only
from prefect.engine.executors import LocalDaskExecutor
from prefect.run_configs import LocalRun


@task
def inc(x):
  sleep(random.random() / 10)
  return x + 1


@task
def dec(x):
  sleep(random.random() / 10)
  return x - 1


@task
def add(x, y):
  sleep(random.random() / 10)
  return x + y


@task(name="sum")
def list_sum(arr):
  logger = prefect.context.get("logger")
  logger.info(f"total sum : {sum(arr)}")  
  return sum(arr)



with Flow("getting-started-example", 
           executor=LocalDaskExecutor(), 
           run_config=LocalRun()) as flow:

  incs = inc.map(x=range(10))
  decs = dec.map(x=range(10))
  adds = add.map(incs, decs)
  total = list_sum(adds)

flow.register(project_name = "FirstProject")
