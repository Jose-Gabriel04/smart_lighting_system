import unittest
from unittest.mock import patch, MagicMock
from services.cloud_service import CloudService

class TestCloudService(unittest.TestCase):
    @patch('services.cloud_service.boto3.client')
    def test_upload_data(self, mock_boto_client):
        mock_s3 = MagicMock()
        mock_boto_client.return_value = mock_s3

        cloud_service = CloudService()
        data = {"luminosity": 300, "presence": 1, "lights_on": True}
        cloud_service.upload_data(data)

        # Verifica se a função 'put_object' foi chamada com os parâmetros corretos
        mock_s3.put_object.assert_called_once_with(
            Body='{"luminosity": 300, "presence": 1, "lights_on": true}', 
            Bucket=cloud_service.bucket_name, 
            Key='lighting_system_data.json'
        )

if __name__ == '__main__':
    unittest.main()