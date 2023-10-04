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
