import os
from dotenv import load_dotenv

from google.cloud import storage
from typing import Union

load_dotenv()

class GCPClient:

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance._initialize()
        return cls.instance

    def _initialize(self):
        self.storage_client = storage.Client(project=os.getenv('GCP_PROJECT_NAME'))
        self.bucket = self.storage_client.bucket(os.getenv('GCP_BUCKET_NAME'))
    
    def download(self, filepath: str) -> bytes:
        blob = self.bucket.blob(filepath)
        return blob.download_as_bytes()

    def upload(self, filepath: str, bytes: Union[str, bytes]) -> None:
        blob = self.bucket.blob(filepath)
        blob.upload_from_string(bytes)