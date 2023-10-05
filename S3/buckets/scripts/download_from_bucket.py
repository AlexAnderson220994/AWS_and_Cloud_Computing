import boto3

s3 = boto3.client('s3')

bucket_name = 'tech254-alex-bucket'
s3_file_name = 'uploaded-file.txt'
local_file = 'downloaded-file.txt'

s3.download_file(bucket_name, s3_file_name, local_file)