import boto3

client = boto3.client('lambda')

response = client.update_function_code()
