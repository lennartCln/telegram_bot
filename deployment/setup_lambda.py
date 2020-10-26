import boto3
import os
import zipfile

import config as C

client = boto3.client('lambda')

response = client.update_function_code()


def zip_dir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def zip_dir_to(source_dir, taget_dir):
    zipf = zipfile.ZipFile(taget_dir, 'w', zipfile.ZIP_DEFLATED)
    zip_dir(source_dir, zipf)
    zipf.close()


if __name__ == '__main__':
    zip_dir_to('../lambda_function/', 'lambda_function.zip')
