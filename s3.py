import boto3

from config import AWS_BUCKET_KEY, AWS_BUCKET_SECRET_KEY, AWS_REGION, AWS_BUCKET_NAME


class S3Manager:
    def __init__(self):
        # Instantiate a session
        session = boto3.Session(
            aws_access_key_id=AWS_BUCKET_KEY,
            aws_secret_access_key=AWS_BUCKET_SECRET_KEY,
            region_name=AWS_REGION
        )

        # Create a resource object for S3
        self.s3 = session.resource('s3')

        # Specify your bucket
        self.bucket = self.s3.Bucket(AWS_BUCKET_NAME)

    # Get the list of all files in the S3 configured bucket
    def get_all_objects(self):
        return list(self.bucket.objects.all())

    # Upload a file to a S3 configured bucket
    def upload_file(self, filename):
        with open(filename, 'rb') as data:
            self.bucket.put_object(Key=filename, Body=data)
        print("File uploaded successfully.")

    # Download a file from a S3 configured bucket
    def download_file(self, s3_key, target_filename):
        self.bucket.download_file(s3_key, target_filename)
        print("File downloaded successfully.")

    # Delete a file from the S3 configured bucket
    def delete_file(self, s3_key):
        self.s3.Object(AWS_BUCKET_NAME, s3_key).delete()
        print("File deleted successfully.")
