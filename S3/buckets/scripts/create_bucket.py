import boto3

# stores connection to AWS
s3 = boto3.client('s3')

# creates the bucket
s3.create_bucket(Bucket='tech254-alex-bucket', CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})

print("Creation of bucket was successful")

