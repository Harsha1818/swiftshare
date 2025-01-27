import boto3
from botocore.exceptions import NoCredentialsError

class S3Service:
    def __init__(self, bucket_name):
        self.s3 = boto3.client("s3")
        self.bucket_name = bucket_name

    def upload_file(self, file_path, object_name):
        try:
            self.s3.upload_file(file_path, self.bucket_name, object_name)
            return f"https://{self.bucket_name}.s3.amazonaws.com/{object_name}"
        except NoCredentialsError:
            return "Error: AWS credentials not found"

# Usage:
# s3_service = S3Service(bucket_name="your-bucket-name")
# s3_service.upload_file("local_path", "s3_key")
