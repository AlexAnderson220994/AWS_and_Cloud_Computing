import boto3

s3 = boto3.client('s3')

bucket_name = 'tech254-alex-bucket'
local_file = 'hello.txt'
s3_file_name = 'hello1.txt'

s3.upload_file(local_file, bucket_name, s3_file_name)
