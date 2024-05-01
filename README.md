# <img src="./images/twitter-logo.png" alt="Twitter logo" style="width: 5%"/> Twitter Data Pipeline with Airflow

### Main Objective

<p>Automating the process of collecting, processing, and storing twitter clean data into Amazon S3 bucket, in order to use it for data analysis. We will be using Apache Airflow management tool to create and manage data pipeline.</p>

#### Data Pipeline Architecture

<img src="./images/Objective.png" alt="ETL Process"/>


#### Process in completing Airflow Project

<p>1- Launching AWS EC2 instance. By configuring the type of operating system we are going to use, Ubuntu, selecting the instance type (T2.small), and by setting up key pair to be able to login through instance from local machine.</p>

<img src="./images/EC2_instance.png" alt="EC2 Instance"/>

<p>2- After installing packages and dependencies required for Apache Airflow.</p>

<p><i><b>One Notice</b>: Try setting up local environment so that it doesn't interfere with the root packages which it might break the EC2 instance, if some how there are any conflicts between packages.</i></p>

<img src="./images/airflow_ui_login" alt="Airflow UI Login"/>

<p>3- With a successful Laucnhing the Airflow UI we can see a the first twitter_DAG.</p>

<img src="./images/first_dag_airflow" alt="First DAG"/>

<p>4- By running the workflow, we can see that it completed successfully.</p>

<img src="./images/Schedule_complete" alt="Schedule Completed"/>

<p>5- Since the workflow has ran successfully, this means that it created the file in the AWS S3 Bucket</p>

<img src="./images/S3_Imported_Successfully" alt="Imported Successfully"/>



#### Skills Developed
<ul>
<li>Reading file from S3 Bucket</li>
<li>Automating tasks with Airflow</li>
<li>Writing and automating ETL scripts<li>
<li>Loading Clean data to S3 Bucket<li>
</ul>

#### Tech Stack:
<ul>
<li>Python<li>
<li>Cloud AWS: EC2, S3, IAM Role</li>
<li>Ubuntu: bash script</li>
<li>Airflow</li>
<li>Version Control: Git</li>