# **Creating Instances on AWS**

## 1) Getting Started - EC2 Dashboard

1) Log in to AWS using your credentials **(NEVER SHARE).**
2) **IMPORTANT** Make sure you are connected the Europe (Ireland) region.
3) Start by either navigating to the EC2 dashboard using either `Services` or by searching "EC2" in the search bar at the top of the screen.
4) You should now be on the EC2 dashboard.

#### What is EC2?

## 2) Launching Instances

### Launch Instance

1) On the EC2 dashboard, click the orange button called `Launch instance`.

### Names and tags

2) Name your web server with the appropriate name.
3) Nomenclature should be <organisation_yourname_typeofinstance>
4) In this case name it `tech254_alex_nginx`
5) Make sure to use all lowercase and use snakecase (not vital but good practice).

### Application and OS image

1) Make sure you're on the quick start tab.
2) Go to "Browse more AMIs"
3) Go to the "Community AMIs" tab
4) Search "18.04 lts 1e9"
5) Click on the version of Ubuntu that comes up.

### Instance type

1) Select `t2.micro`
2) Make sure its the Free tier eligible version.

### Key pair (login)

1) Select the appropriate key pair that has been generated for the exercise.
2) In this case choose `tech254` from the key pair name dropdown list.

### Network settings

1) Click on edit in the top right corner of the "Network settings" section.
2) Leave VPC as default
3) Subnet should be No preference
4) Auto-assign public IP - Enable
5) Change Security group name using a similar nomenclature to the name of the Instance being created.
6) In this case `tech254_alex_basesg`
7) Add a description which can be the same as the name if the name is already descriptive. Otherwise add a descriptive name.
8) Add Security group rule 1
- Type - SSH
- Source type - Anywhere
9) Add security group rule 2
- Type - HTTP
- Source type - Anywhere
10) Add security group rule 3
- Type - HTTPS
- Source type - Anywhere

### Configure storage
1) Leave as it is.