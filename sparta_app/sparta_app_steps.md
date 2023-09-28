# Sparta Application deployment on AWS

## Create instance and set up nginx

1) Follow all the steps to creating an instance and setting up nginx on the attached MD.
2) https://github.com/AlexAnderson220994/AWS_and_Cloud_Computing/blob/main/AWS_instance_creation.md

## Base folder for application

1) Make sure an unzipped/extracted folder with all the `app` files and data is saved within your file structure.

## Adding the `app` folder to your instance

### Method 1 - scp

1) Input the following command into GitBash using your main computer OS (in this case windows).
2) Type the following command:
````
scp -i "<filepath to .pem file>" -r <filepath to your local app folder> Ubuntu@<public IP>:<remote filepath>
````
````
e.g. scp -i "C:/Users/Alex (Sparta)/.ssh/tech254.pem" -r app ubuntu@ec2-34-242-237-25.eu-west-1.compute.amazonaws.com:~
````
3) It is useful to already be located in the local app folder on GitBash so you only need to type the folder name and not the file path.
4) Remember the `:~` at the end.

### Method 2 - Cloning repo from Github

1) Do a `git add`, `git commit` and `git push -u origin main` to push the app folder onto a new repository on GitHub.
2) Make sure the repository only contains that folder and no other files/folders.
3) Connect to your instance on GitBash
4) Type the following:
````
git clone <http link of repository url>
````
5) Use `cd` to navigate to the specific folder with all the app files if not already there.

## Deploying the app using Nodejs

1) To run this application, an older version of Nodejs is needed (Version 12.x).
2) Attempting to install Nodejs will bring up the latest version which isn't suitable for this app.
3) Run the following command to install the required version of Nodejs:
````
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
````
4) Let this command run.
5) Run the following command:
````
sudo apt install nodejs -y
````
6) Run the following command:
````
sudo npm install pm2 -g
````
7) `npm` means Node Package Manager (similar to pip on Python) and `pm2` means Process Manager 2.
8) Double check you're located in the correct folder.
9) Run the command:
````
npm install
````
10) All packages are installed in order to run the app

## Check security permissions

1) Navigate to your instance page on the EC2 dashboard on AWS.
2) Open your instance.
3) Navigate to the security tab.
4) Click the link under "security groups".
5) Click "Edit inbound rules". Make sure you use inbound and not outbound.
6) Click "Add rule".
7) Add the following rule:
````
Type --- Custom TCP
Port --- 3000
Source --- Anywhere IPv4 OR 0.0.0.0/0
````

## Test the link

1) Copy the public IP address of your instance into the search engine search bar.
2) Add `:3000` to the end so it connects to Port 3000 where your app is running.
3) Hit refresh.