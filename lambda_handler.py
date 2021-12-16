import boto3
def handler(event,context):
  client = boto3.client('ecs')
  response = client.run_task(
  cluster='fargatecluster', # name of the cluster
  launchType = 'FARGATE',
  taskDefinition='my-batch-job:1', # replace with your task definition name and revision
  count = 1,
  platformVersion='LATEST',
  networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': [
                'subnet-2ec3a94a', # replace with your public subnet or a private with NAT
                'subnet-413a9c6e' # Second is optional, but good idea to have two
            ],
            'assignPublicIp': 'DISABLED'
        }
    })
  return str(response)
