import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app, stub


client = TestClient(app)

# Mock the gRPC stub
stub.UploadFile = MagicMock()
stub.GetFiles = MagicMock()

def test_upload_file_success():
    # Arrange
    stub.UploadFile.return_value = MagicMock(status="success", message="File uploaded successfully")
    payload = {
        "user_name": "testuser",
        "file_name": "testfile.txt",
        "file_path": "/path/to/testfile.txt"
    }

    # Act
    response = client.post("/api/files", json=payload)

    # Assert
    assert response.status_code == 201
    assert response.json() == {"status": "success", "message": "File uploaded successfully"}

def test_upload_file_failure():
    # Arrange
    stub.UploadFile.return_value = MagicMock(status="failure", message="File upload failed")
    payload = {
        "user_name": "testuser",
        "file_name": "testfile.txt",
        "file_path": "/path/to/testfile.txt"
    }

    # Act
    response = client.post("/api/files", json=payload)

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "File upload failed"}

def test_get_files():
    # Arrange
    stub.GetFiles.return_value = MagicMock(files=[
        MagicMock(file_name="file1.txt", file_path="/path/to/file1.txt"),
        MagicMock(file_name="file2.txt", file_path="/path/to/file2.txt")
    ])
    user_name = "testuser"
    params = {"user_name": user_name}

    # Act
    response = client.get("/api/files", params=params)

    # Assert
    assert response.status_code == 200
    assert response.json() == [
        {"name": "file1.txt", "path": "/path/to/file1.txt"},
        {"name": "file2.txt", "path": "/path/to/file2.txt"}
    ]

if __name__ == "__main__":
    pytest.main()
