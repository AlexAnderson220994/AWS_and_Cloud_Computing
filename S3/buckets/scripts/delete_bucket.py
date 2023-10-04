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
