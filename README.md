# cs643_wineprediction
The purpose of this individual assignment is to learn how to develop parallel machine learning (ML) applications in Amazon AWS cloud platform. Specifically, you will learn: (1) how to use Apache Spark to train an ML model in parallel on multiple EC2 instances; (2) how to use Spark’s MLlib to develop and use an ML model in the cloud; (3) How to use Docker to create a container for your ML model to simplify model deployment.
 
AIM: 

The purpose of this individual assignment is to learn how to develop parallel machine learning (ML) applications in Amazon AWS cloud platform. Specifically, you will learn: (1) how to use Apache Spark to train an ML model in parallel on multiple EC2 instances; (2) how to use Spark’s MLlib to develop and use an ML model in the cloud; (3) How to use Docker to create a container for your ML model to simplify model deployment. 

DESCRIPTION: 

Firstly, I created my spark cluster with Hadoop on AWS EMR. Using python as my Programming Language I trained the model with the Input Dataset provided by the professor TrainingDataset.csv which is the file having the data for the Wine. I stored my training dataset on AWS S3 Bucket. Having tried various Machine learning approaches I found Random Forest having better accuracy than any other algorithm. Thus, I implemented Random Forest in my model.py file for the creation of the model using the MLLIB library. I stored my output for the program on my S3 bucket as a randomforestmodel.model. Now comes the prediction step. We must fetch the model from the S3 bucket and also fetch the dataset ValidationSet.csv which was also uploaded to the S3 bucket. The output of this program will be the Model Accuracy and its F1 Score.

IMPORTANT LINKS: 
GitHub : https://github.com/komaldeep97/cs643_wineprediction

DockerHub : https://hub.docker.com/r/komaldeep/wineprediction 

STEPS ON HOW TO SET THE ENVIRONMENT FOR MODEL CREATION AND TRAINING USING AWS EMR.

1.	Login into AWS Account.
2.	Search for EMR in service > Open EMR.
3.	Click on the Create Cluster Button.
4.	Add Cluster Name. Here as we are using Spark we will Select Spark in Software Configuration. We need to run our program in 4 parallel EC2 instances so I created 5 instances 1 master and 4 slave. Select the keypair from the existing or you can also create one at that time and store at your local machine.
 
5.	Click the button below to create the cluster.
 
6.	After that your cluster will be in the Starting Stage and you will see the screen as below.
 
7.	Click ssh to get login details for Master node of our EMR cluster > Save it.
8.	In the security and access summary click on the security group for master to change inbound rules for traffic as below.
 
 

After successful creation of AWS EMR Spark cluster, we can login into the cluster using terminal with the following Command.
Command :  ssh -i key.pem hadoop@user

Copy your Model file to the EWR cluster and run the file using the spark-submit command.
Command : spark-submit ./model.py

Output for this program is stored in my S3 bucket after the model is created we can run the Prediction program which gives us the Accuracy of the model same way using the Spark-Submit command.
 
STEPS TO RUN THE MODEL PREDICTION ON SINGLE EC2 INSTANCE WITHOUT DOCKER

1.	Create an EC2 instance.
2.	Ssh into your ec2 instance. 
3.	Configure Spark in to your instance. 
4.	Pull the GitHub repository in your instance. 
5.	Create a Directory named testdata by running the below command and put your test data set into that directory.
Command : /mkdir testdata
6.	Now for the model prediction run the below command.
Command : 
spark-submit --packages org.apache.hadoop:hadoop-aws:2.7.7 final.py
 

STEPS TO RUN THE MODEL PREDICTION ON SINGLE EC2 INSTANCE WITH DOCKER

1.	Create an EC2 instance.
2.	Ssh into your ec2 instance.
3.	Install the docker into your EC2 instance if it is not there using the https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html
4.	Add your test data file in your EC2 instance.
5.	Run the Command : docker pull komaldeep/wineprediction:latest
6.	By running the above command the user will get the Docker image.
7.	Now run the below command in the directory where your test data file is there.
8.	Run the Command : 
sudo docker run -it -v "$(pwd)":/testdata komaldeep/wineprediction:latest
9.	This will give the output of Model Accuracy and F1 score as shown below. 
