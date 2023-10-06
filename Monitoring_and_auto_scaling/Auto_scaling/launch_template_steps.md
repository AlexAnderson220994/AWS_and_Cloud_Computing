# Launch template

## Making a launch template

1) Click on "Launch template" on the left hand pane of the EC2 console.
2) Click on `Create launch template`.
3) Give the template an appropriate name. e.g. `tech254_alex_for_asg_app_first_lt`
4) Choose your app AMI.
5) Choose t2 micro for "Instance type".
6) Choose tech254 as the key pair.
7) Use existing security group.
8) Put in the User data required to run the app:
````
#!/bin/bash

cd /home/ubuntu/repo/app
sudo systemctl restart nginx
npm install
sudo npm install pm2 -g
pm2 kill
pm2 start app.js
````
9) Click on `create launch template`.

## Launching instance from template

9) Open up the template you made.
10) Go to "Actions" in the top right corner and click `Launch instance from template`.
11) Before you click `launch instance`, add the instance name:
12) Go to "Resource tags" and click `add new tag`.
13) Do "key" as NAME, and "value" as the name you want to give the instance.