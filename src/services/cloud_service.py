import boto3
import json
import os

class CloudService:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.bucket_name = os.getenv("S3_BUCKET_NAME")
        self.file_name = 'lighting_system_data.json'

    def upload_data(self, data):
        try:
            # Converte os dados em JSON
            json_data = json.dumps(data)
            # Envia os dados para o bucket S3
            self.s3_client.put_object(Body=json_data, Bucket=self.bucket_name, Key=self.file_name)
            print(f"Dados enviados para o bucket S3: {self.bucket_name}")
        except Exception as e:
            print(f"Erro ao enviar dados para a nuvem: {e}")