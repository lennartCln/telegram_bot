import boto3
import os
import io
import zipfile

import config as C

client = boto3.client('lambda')

def files_to_zip(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            full_path = os.path.join(root, f)
            print(full_path)
            archive_name = full_path[len(path) + len(os.sep):]
            yield full_path, archive_name

def make_zip_file_bytes(path):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as z:
        for full_path, archive_name in files_to_zip(path=path):
            z.write(full_path, archive_name)
    return buf.getvalue()

if __name__ == '__main__':
    lambda_code = '../lambda_function/'

    response = client.update_function_code(
        FunctionName= C.AWS['function_name'],
        ZipFile= make_zip_file_bytes(lambda_code))

    print(response)


