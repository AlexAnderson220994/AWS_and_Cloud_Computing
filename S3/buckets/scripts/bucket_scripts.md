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

# Specify the AWS region and bucket name
region_name = 'eu-west-1'  # Change to your desired region
bucket_name = 'tech254-alex-bucket'  # Change to your bucket name

# Specify the local file path to upload
local_file_path = 'path/to/local/file.txt'  # Change to the path of your local file
s3_key = 'folder/subfolder/file.txt'  # The desired key in the S3 bucket

# Initialize the S3 client without specifying credentials (uses AWS CLI credentials)
s3 = boto3.client('s3', region_name=region_name)

try:
    # Upload the file to S3
    s3.upload_file(local_file_path, bucket_name, s3_key)
    print(f"File '{local_file_path}' uploaded to '{bucket_name}/{s3_key}'")
except Exception as e:
    print(f"Error uploading file: {e}")
````

## Downloading from a bucket


````
import boto3

# Specify the AWS region and bucket name
region_name = 'eu-west-1'  # Change to your desired region
bucket_name = 'tech254-alex-bucket'  # Change to your bucket name

# Specify the S3 key (object key) for the file to download
s3_key = 'folder/subfolder/file.txt'  # The key of the file in the S3 bucket
local_file_path = 'path/to/save/downloaded/file.txt'  # The local file path to save the downloaded file

# Initialize the S3 client without specifying credentials (uses AWS CLI credentials)
s3 = boto3.client('s3', region_name=region_name)

try:
    # Download the file from S3
    s3.download_file(bucket_name, s3_key, local_file_path)
    print(f"File '{s3_key}' downloaded to '{local_file_path}'")
except Exception as e:
    print(f"Error downloading file: {e}")
````

## Deleting a bucket

````
import boto3

# Specify the AWS region and bucket name
region_name = 'eu-west-1'  # Change to your desired region
bucket_name = 'tech254-alex-bucket'  # Change to the name of the bucket you want to delete

# Initialize the S3 client without specifying credentials (uses AWS CLI credentials)
s3 = boto3.client('s3', region_name=region_name)

try:
    # Delete the S3 bucket (bucket must be empty)
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' deleted successfully.")
except Exception as e:
    print(f"Error deleting bucket: {e}")
````