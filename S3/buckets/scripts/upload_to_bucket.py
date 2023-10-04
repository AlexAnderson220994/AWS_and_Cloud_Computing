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
