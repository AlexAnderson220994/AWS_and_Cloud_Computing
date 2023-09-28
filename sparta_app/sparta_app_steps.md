# Sparta Application deployment on AWS

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

1) Do a `git add``, `git commit` and `git push -u origin main` to push the app folder onto a new repository on GitHub.
2) Make sure the repository only contains that folder and no other files/folders.
3) Connect to your instance on GitBash
4) Type the following:
````
git clone <http link of repository url>
````