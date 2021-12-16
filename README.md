                            Assignment for DevOps Traineeship

1) Pick your favourite open source project on Github,

   Github Link:-  https://github.com/gowthamshashank/myways.git

2) Create a docker for this and push to ECR,

   CMD:-  docker build -t myways .
   CMD:-  aws configure
   CMD:-  aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 302716195582.dkr.ecr.us-east-1.amazonaws.com
   CMD:-  docker tag myways:latest public.ecr.aws/u5i8l9g5/myways:latest
   CMD:-  docker push 302716195582.ecr.aws/u5i8l9g5/myways:latest

3) Make a github repo for code you select and with docker file,

   Github Link:- Doeckerfile
   link:- https://github.com/gowthamshashank/myways/blob/master/Dockerfile

4) Use AWS EC2 t2.micro for containers with ECS, create a task in ECS for this service to start the app,   

   STEPS:-

   STEP:-1 Firstly Create Cluster with Following Requirments
   STEP:-2 Create Task Defination
   Step:-3 Create Task in Cluster

5) Use API Gateway and AWS Lambda to make an endpoint to start the app,

   STEPS:-

   STEP:-1 Firstly Create Lambda and Add role With ECS FULL ACCESS and ADD code

   Python:-
           
