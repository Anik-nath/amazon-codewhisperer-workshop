import os
import json
import boto3
import requests
import botocore.exceptions

s3_client = boto3.client("s3")
S3_BUCKET = os.getenv('BUCKET_NAME')

# 1.) Function to get a file from url
def get_file_from_url(url):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)
# 2.) Function to upload image to S3
def upload_file_to_s3(file, bucket_name, key):
    try:
        s3_client.put_object(Body=file, Bucket=bucket_name, Key=key)
        return True
    except botocore.exceptions.ClientError as e:
        print(e)
        return False
# <<Amazon CodeWhisperer generated code goes here>>


def handler(event, context):
    url = event["queryStringParameters"]["url"]
    name = event["queryStringParameters"]["name"]

    # pass the output of method #1 as input to method #2
    file = get_file_from_url(url)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully Uploaded Img!')
    }
