import unittest
from unittest.mock import Mock
from app.file_service_proto.file_service_pb2 import UploadResponse, RetrieveResponse, FileRecord
from app.adapter import PersistentAdapter
from app.service import FileService  # Assuming the class is in a file named file_service.py

class TestFileService(unittest.TestCase):
    
    def setUp(self):
        # Create a mock PersistentAdapter
        self.mock_adapter = Mock(spec=PersistentAdapter)
        
        # Instantiate the FileService with the mock adapter
        self.service = FileService(persistent_adapter=self.mock_adapter)

    def test_upload_file_success(self):
        # Create a mock request
        mock_request = Mock()
        mock_request.user_name = "test_user"
        mock_request.file_name = "test_file.txt"
        mock_request.file_path = "/path/to/test_file.txt"

        # Create a mock context (can be an empty Mock)
        mock_context = Mock()

        # Call the UploadFile method
        response = self.service.UploadFile(mock_request, mock_context)

        # Assert the response
        self.assertIsInstance(response, UploadResponse)
        self.assertEqual(response.status, "success")
        self.assertEqual(response.message, "File record uploaded successfully")

        # Verify that the upload_file_to_db method was called with correct parameters
        self.mock_adapter.upload_file_to_db.assert_called_once_with(
            user_name="test_user",
            file_name="test_file.txt",
            file_path="/path/to/test_file.txt",
        )

    def test_get_files_with_user_name(self):
        # Setup mock return value for get_file_records_from_db
        mock_records = [
            Mock(file_name="file1.txt", file_path="/path/to/file1.txt"),
            Mock(file_name="file2.txt", file_path="/path/to/file2.txt")
        ]
        self.mock_adapter.get_file_records_from_db.return_value = mock_records

        # Create a mock request
        mock_request = Mock()
        mock_request.user_name = "test_user"

        # Create a mock context
        mock_context = Mock()

        # Call the GetFiles method
        response = self.service.GetFiles(mock_request, mock_context)

        # Assert the response
        self.assertIsInstance(response, RetrieveResponse)
        self.assertEqual(len(response.files), 2)
        self.assertEqual(response.files[0].file_name, "file1.txt")
        self.assertEqual(response.files[0].file_path, "/path/to/file1.txt")
        self.assertEqual(response.files[1].file_name, "file2.txt")
        self.assertEqual(response.files[1].file_path, "/path/to/file2.txt")

        # Verify that the get_file_records_from_db method was called with correct parameters
        self.mock_adapter.get_file_records_from_db.assert_called_once_with(
            user_name="test_user"
        )

    def test_get_files_without_user_name(self):
        # Setup mock return value for get_all_file_records_from_db
        mock_records = [
            Mock(file_name="file3.txt", file_path="/path/to/file3.txt"),
            Mock(file_name="file4.txt", file_path="/path/to/file4.txt")
        ]
        self.mock_adapter.get_all_file_records_from_db.return_value = mock_records

        # Create a mock request with no user_name
        mock_request = Mock()
        mock_request.user_name = None

        # Create a mock context
        mock_context = Mock()

        # Call the GetFiles method
        response = self.service.GetFiles(mock_request, mock_context)

        # Assert the response
        self.assertIsInstance(response, RetrieveResponse)
        self.assertEqual(len(response.files), 2)
        self.assertEqual(response.files[0].file_name, "file3.txt")
        self.assertEqual(response.files[0].file_path, "/path/to/file3.txt")
        self.assertEqual(response.files[1].file_name, "file4.txt")
        self.assertEqual(response.files[1].file_path, "/path/to/file4.txt")

        # Verify that the get_all_file_records_from_db method was called
        self.mock_adapter.get_all_file_records_from_db.assert_called_once()

    def test_get_files_with_no_records(self):
        # Setup mock return value for get_file_records_from_db with no records
        self.mock_adapter.get_file_records_from_db.return_value = []

        # Create a mock request
        mock_request = Mock()
        mock_request.user_name = "test_user"

        # Create a mock context
        mock_context = Mock()

        # Call the GetFiles method
        response = self.service.GetFiles(mock_request, mock_context)

        # Assert the response
        self.assertIsInstance(response, RetrieveResponse)
        self.assertEqual(len(response.files), 0)

        # Verify that the get_file_records_from_db method was called with correct parameters
        self.mock_adapter.get_file_records_from_db.assert_called_once_with(
            user_name="test_user"
        )

if __name__ == '__main__':
    unittest.main()
