                                       Assignment for DevOps Traineeship

1) Pick your favourite open source project on Github,

   Github Link:-  https://github.com/gowthamshashank/myways.git

2) Create a docker for this and push to ECR,

   ->CMD:-  docker build -t myways .
   ![Screenshot 2021-12-14 at 7 24 58 PM](https://user-images.githubusercontent.com/52821412/146432932-1a9e1286-abdc-4c85-bd9d-f8d1183766df.png)

   ->CMD:-  aws configure
   
   ->CMD:-  aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 302716195582.dkr.ecr.us-east-1.amazonaws.com
   
   ->CMD:-  docker tag myways:latest public.ecr.aws/u5i8l9g5/myways:latest
   
   ->CMD:-  docker push 302716195582.ecr.aws/u5i8l9g5/myways:latest
   ![Screenshot 2021-12-14 at 7 26 19 PM](https://user-images.githubusercontent.com/52821412/146433021-4fb1b749-6b24-4713-b0bd-d285f8172610.png)


3) Make a github repo for code you select and with docker file,

   Github Link:- Doeckerfile
   link:- https://github.com/gowthamshashank/myways/blob/master/Dockerfile

4) Use AWS EC2 t2.micro for containers with ECS, create a task in ECS for this service to start the app,   

   STEPS:-

   STEP:-1 Firstly Create Cluster with Following Requirments
   ![Screenshot 2021-12-16 at 10 27 26 PM](https://user-images.githubusercontent.com/52821412/146433073-a3f315ee-25c0-4165-9965-5a111b0a232c.png)
   ![Screenshot 2021-12-16 at 10 27 42 PM](https://user-images.githubusercontent.com/52821412/146433124-83913a64-fac5-49fc-92be-5ba1574b1f9f.png)
   ![Screenshot 2021-12-16 at 10 28 22 PM](https://user-images.githubusercontent.com/52821412/146433152-f4522b6c-7a5d-4862-9fd6-d0b72d29158e.png)
   ![Screenshot 2021-12-16 at 10 29 12 PM](https://user-images.githubusercontent.com/52821412/146433176-05cd6696-fd80-4209-b987-c8154c9aa444.png)
   

   STEP:-2 Create Task Defination
   ![Screenshot 2021-12-16 at 10 29 58 PM](https://user-images.githubusercontent.com/52821412/146433222-3513b7f7-272c-46b3-974a-e6c4e87f4384.png)
   ![Screenshot 2021-12-16 at 10 34 21 PM](https://user-images.githubusercontent.com/52821412/146433244-db532000-36f9-480a-b888-bc4a1a526636.png)
   ![Screenshot 2021-12-16 at 10 34 36 PM](https://user-images.githubusercontent.com/52821412/146433267-b8f7cada-8bc1-4d7c-86f2-3e5c8a4eae66.png)

   Step:-3 Create Task in Cluster
   ![Screenshot 2021-12-16 at 10 37 59 PM](https://user-images.githubusercontent.com/52821412/146433302-6bc6a630-7ea9-4dc0-90f7-c1f336fb5d6c.png)


5) Use API Gateway and AWS Lambda to make an endpoint to start the app,

   STEPS:-

   STEP:-1 Firstly Create Lambda and Add role With ECS FULL ACCESS and ADD code
   
   Python Link:-  https://github.com/gowthamshashank/myways/blob/master/lambda_handler.py
   ![Screenshot 2021-12-16 at 10 41 36 PM](https://user-images.githubusercontent.com/52821412/146433338-93f72e8e-37bd-44ea-819f-d2d34a0555c8.png)
   ![Screenshot 2021-12-16 at 10 41 57 PM](https://user-images.githubusercontent.com/52821412/146433360-9464c820-cfb4-4cc4-9b91-901592cf725b.png)
   ![Screenshot 2021-12-16 at 11 49 59 PM](https://user-images.githubusercontent.com/52821412/146433376-7d71a65c-198b-4e8d-89e0-039949df7397.png)
   ![Screenshot 2021-12-16 at 11 50 20 PM](https://user-images.githubusercontent.com/52821412/146433402-ca4b138f-b226-4d37-ba34-bef9e00d58d2.png)

           
