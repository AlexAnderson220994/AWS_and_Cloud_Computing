#!/bin/bash

# clone app folder from GitHub
git clone https://github.com/LSF970/sparta_test_app.git

# move to folder
cd sparta_test_app

# move to folder
cd app

# get correct version of Nodejs
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

# install nodejs
sudo apt install nodejs -y

# install pm2
sudo npm install pm2 -g

# install node package manager
npm install

# launch app
node app.js