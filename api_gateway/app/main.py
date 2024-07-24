from fastapi import FastAPI, HTTPException
import grpc
from file_service_proto.file_service_pb2 import UploadRequest, RetrieveRequest
from file_service_proto.file_service_pb2_grpc import FileServiceStub
from api_model import UploadFileResponse, UploadFileRequest, FileResponse
from fastapi.responses import JSONResponse
from typing import Optional
import os

app = FastAPI()

# Connect to gRPC server
if os.getenv("FILE_SERVICE_HOST") == "file_service":
    channel = grpc.insecure_channel(f'{os.getenv("FILE_SERVICE_HOST")}:50051')
else:
    channel = grpc.secure_channel(f'{os.getenv("FILE_SERVICE_HOST")}:443', grpc.ssl_channel_credentials())
stub = FileServiceStub(channel)

@app.post("/api/files", response_model=UploadFileResponse)
def upload_file(record: UploadFileRequest):
    request = UploadRequest(user_name=record.user_name, file_name=record.file_name, file_path=record.file_path)
    response = stub.UploadFile(request)
    if response.status == "success":
        return JSONResponse(
            content={"status": "success", "message": response.message},
            status_code=201  # Set status code to 201 Created
        )
    else:
        raise HTTPException(status_code=400, detail=response.message)

@app.get("/api/files", response_model=list[FileResponse])
def get_files(user_name: Optional[str] = None):
    request = RetrieveRequest(user_name=user_name or "")  # Provide an empty string if user_name is None
    response = stub.GetFiles(request)
    return [{"name": file.file_name, "path": file.file_path} for file in response.files]
