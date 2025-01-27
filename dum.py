import boto3
from botocore.exceptions import ClientError

def upload_to_s3(file_path, bucket_name, object_name):
    s3 = boto3.client("s3")
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File uploaded successfully to {bucket_name}/{object_name}")
    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    bucket_name = "swiftsharecloud"
    file_path = "test_file.txt"
    object_name = "uploads/test_file.txt"
    upload_to_s3(file_path, bucket_name, object_name)
