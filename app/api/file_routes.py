from fastapi import APIRouter, UploadFile, HTTPException
import boto3
from botocore.exceptions import ClientError

router = APIRouter()

# Initialize S3 client
s3 = boto3.client("s3")
bucket_name = "swiftsharecloud"

@router.post("/upload")
async def upload_file(file: UploadFile):
    """
    Upload a file directly to S3.
    """
    object_name = f"uploads/{file.filename}"  # S3 key
    try:
        # Upload file to S3
        s3.upload_fileobj(file.file, bucket_name, object_name)
        return {"message": f"File uploaded successfully to S3: {bucket_name}/{object_name}"}
    except ClientError as e:
        raise HTTPException(status_code=500, detail=f"S3 Client Error: {e.response['Error']['Message']}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected Error: {str(e)}")

@router.get("/download/{filename}")
async def download_file(filename: str):
    """
    Generate a pre-signed URL for downloading a file from S3.
    """
    object_name = f"uploads/{filename}"  # S3 key
    try:
        # Generate a pre-signed URL
        presigned_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=3600  # URL valid for 1 hour
        )
        return {"url": presigned_url}
    except ClientError as e:
        raise HTTPException(status_code=500, detail=f"S3 Client Error: {e.response['Error']['Message']}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected Error: {str(e)}")

from celery_app import process_file

@router.post("/upload")
async def upload_file(file: UploadFile):
    # Upload logic
    process_file.delay(file.filename)
    return {"message": "File uploaded and processing started."}
