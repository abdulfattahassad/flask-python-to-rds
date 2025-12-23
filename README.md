# flask-python-to-rds

to access rds from ec2. .. require to install mysql client


# Amazon Linux / RHEL
sudo yum install mysql -y

# Ubuntu / Debian
sudo apt-get update
sudo apt-get install mysql-client -y



-  then choose the databse

use db;

-- then access it via

mysql -h db.c18m8comuyav.us-east-1.rds.amazonaws.com -u admin -p 


- show tables;

- select * from customer;


---- when we deploy python on ubtunt you need virual enviroment which you can find it 

