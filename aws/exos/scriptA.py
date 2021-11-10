import boto3

client = boto3.client('ec2')

numInstances = int(input('Nombre de VMs à instancier: '))

imageId = 'ami-0a49b025fffbbdac6' # ubuntu server 20.04 eu-central-1
sgId = 'sg-0f1731f6fd0e257ce' # sgFirst => ssh + http
keyName = 'kp-first'

userData = """#!/bin/bash
apt update
apt install -y apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" |sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt update
apt install -y docker-ce docker-ce-cli containerd.io
docker run -d --name apache -p 80:80 httpd:2.4-alpine"""


response = client.run_instances(
  ImageId=imageId,
  InstanceType='t2.micro',
  KeyName=keyName,
  MaxCount=numInstances,
  MinCount=numInstances,
  SecurityGroupIds=[sgId],
  UserData=userData,
  DryRun=False
)

# production en sortie d'un fichier texte contenant 
# les identifiants des instances générées

instanceIds = ''

for instance in response['Instances']:
  if instanceIds == '':
    instanceIds = instance['InstanceId']
  else:
    instanceIds += '\n' + instance['InstanceId']

with open("instanceIds.txt", "w") as f:
  f.write(instanceIds)




