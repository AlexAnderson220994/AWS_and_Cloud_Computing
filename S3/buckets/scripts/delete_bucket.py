import boto3

s3 = boto3.client('s3')

bucket_name = 'tech254-alex-bucket'

s3.delete_bucket(Bucket=bucket_name)
