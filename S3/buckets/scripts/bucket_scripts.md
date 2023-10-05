# Python Scripts using Boto3 on AWS S3

## Notes for creation

1) These scripts assume that the AWS CLI has already been configured with the necessary credentials and default region. 
2) Be careful **never** to share AWS login credentials.

## Creating a bucket

````
import boto3

# stores connection to AWS
s3 = boto3.client('s3')

# creates the bucket
s3.create_bucket(Bucket='tech254-alex-bucket', CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})

print("Creation of bucket was successful")
````

# Uploading to a bucket


````
import boto3

s3 = boto3.client('s3')

bucket_name = 'tech254-alex-bucket'
local_file = 'hello.txt'
s3_file_name = 'hello1.txt'

s3.upload_file(local_file, bucket_name, s3_file_name)
````

## Downloading from a bucket


````
import boto3

s3 = boto3.client('s3')

bucket_name = 'tech254-alex-bucket'
s3_file_name = 'uploaded-file.txt'
local_file = 'downloaded-file.txt'

s3.download_file(bucket_name, s3_file_name, local_file)
````

## Deleting a bucket

````
import boto3

s3 = boto3.client('s3')

bucket_name = 'tech254-alex-bucket'

s3.delete_bucket(Bucket=bucket_name)
````

- Make sure the bucket is empty first.