# Autoscaling and Load Balancing steps on AWS

## AWS Auto Scaling Group - Deploy app with HA + SC (High Availability + Scalability)

- Provision your instance to run an app
- Make an AMI of this instance
- Use a launch template to pre fill all the boxes on the launch instance page

### Auto scaling group

- Choose the group size (minimum, maximum, desired number of VMs to be made)
- Create the VMs
- Each VM can be in a different Availability Zone (e.g. AZ1a, AZ1b, AZ1c)
- Scaling policy - Sets the threshold (in this case 50%) to monitor the CPU usage

## Autoscaling steps

**1) Go to the EC2 console on AWS.**
**2) On the left hand pane, scroll down to `Auto Scaling Groups` and click on it.**
**3) Click on `Create Auto Scaling group`.**
**4) STEP 1 - Choose launch template or configuration.**
- Name the autoscaling group using the proper naming conventions (use hyphens)
````
tech254-alex-app-first-asg
````
- Select the launch template you made earlier.
- Click `Next`.
**5) STEP 2 - Choose instance launch options.**
- Under "Network", keep VPC the same
- Under "Network", add the 3 default subnets (DevOps student default (1a, 1b, 1c))
- Leave Instance type requirements the same
- Click `Next`.
**6) STEP 3 - Configure advanced options.**
- Under "Load balancing", select `Attach to a new load balancer`.
- Select `Application Load Balancer`.
- Give the load balancer a name using normal naming conventions e.g. `tech254-alex-app-first-asg-lb`.
- Change "Load balancer scheme" to `Internet-facing`.
- 

## Load Balancing steps

## Deletion