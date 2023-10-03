# Connecting Databases (MongoDB) to your App Instance

## 1) Create your App Instance using your AMI

1) Go to "Launce Instance"
2) Scroll down to My AMIs.
3) Click on owned by me and choose your previously created App AMI. e.g.
````
tech254_alex_app_ami
````
4) Use same SSH key and network groups used for usual App instance creation.
5) Launch instance.
6) Open GitBash and connect to the App instance. (NOTE: make sure you change "root" to "ubuntu" in the Public DNS used to connect)
7) Also make sure you use `cd` to navigate to the .ssh folder first.

## 2) Setting up Database Instance

1) Open a new GitBash window (right click and go to options to change colour if you want to differentiate Gitbash windows).
2) Go to "Launch Instance" on the EC2 Dashboard on AWS.
3) Name the instance using the correct nomenclature to differentiate from the App Instance you made earlier. e.g.
````
tech254_alex_db
````
4) Use the Ubuntu 18.04 lts 1e9 AMI from the community AMIs tab.
5) Create a new security group to allow only the SSH and database connections (click the edit button in the top right corner).
````
tech254_alex_db_sg
````
6) The SSH security configuration is pre populated (Port 22)
7) Configure the database connection for a Custom TCP (Port `27017` for databases)
8) Make sure both allow all traffic (0.0.0.0/0).
9) Keep all other settings the same as normal and launch instance.

## 3) Setting up the database on Gitbash

1) Connect to your Database EC2 instance on the second Gitbash terminal you opened using the normal procedure.
2) Input the following commands:
````
sudo apt update
````
````
sudo apt upgrade -y
````
3) Install the version of MongoDB (3.2) required using the following command:
````
wget -qO - https://www.mongodb.org/static/pgp/server-3.2.asc | sudo apt-key add -
````
4) Then do the following command:
````
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
````
5) Do sudo apt update again.
````
sudo apt update
````
6) Specify the components of MongoDB to be installed using the following command:
````
sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20
````
7) Input the following command to alter the IP address for who can connect in the mongodb config:
````
sudo nano /etc/mongod.conf
````
8) Scroll down to "# network interfaces" and change "bindIp:" from 127.0.0.1 TO 0.0.0.0. Then do ctrl + x, then hit yes, then hit enter.
9) Enter the command to start mongod:
````
sudo systemctl start mongod
````
10) Enter the command to enable mongod at startup:
````
sudo systemctl enable mongod
````
11) Do `sudo systemctl status mongod` and check it says "active running".

## 4) Connect App to Database

1) Go back to the Gitbash terminal for the App instance.
2) Create an environment variable using the following command;
````
export DB_HOST=mongodb://<public_IP_of_DB_instance>27017/posts
````
3) Verify its worked using `printenv` or `printenv DB_HOST`.
4) Navigate to the correct folder in the terminal where `app.js` is located.
````
cd sparta_test_app
cd app
````
5) Run the node package manager install command:
````
npm install
````
6) If you scroll back it should say `Database cleared` and `Database seeded`. Connection has been established.
7) Run the node command.
````
node app.js
````

## 5) Open the webpage

1) Go to App instance summary on AWS.
2) Copy public IP into URL search bar.
3) Add the following to the end of the ip address in the URL search bar:
````
:3000/posts
````
4) The page should be up and running.


