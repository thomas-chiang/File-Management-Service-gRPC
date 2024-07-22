from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import grpc
from file_service_pb2 import UploadRequest, RetrieveRequest
from file_service_pb2_grpc import FileServiceStub

app = FastAPI()

# Connect to gRPC server
channel = grpc.insecure_channel('grpc_service:50051')
stub = FileServiceStub(channel)

class UploadFileRequest(BaseModel):
    user_name: str
    file_name: str
    file_path: str

class FileResponse(BaseModel):
    name: str
    path: str

class UploadFileResponse(BaseModel):
    status: str
    message: str

@app.post("/api/files", response_model=UploadFileResponse)
def upload_file(record: UploadFileRequest):
    request = UploadRequest(user_name=record.user_name, file_name=record.file_name, file_path=record.file_path)
    response = stub.UploadFile(request)
    if response.status == "success":
        return {"status": "success", "message": response.message}
    else:
        raise HTTPException(status_code=400, detail=response.message)

@app.get("/api/files", response_model=list[FileResponse])
def get_files(user_name: str):
    request = RetrieveRequest(user_name=user_name)
    response = stub.GetFiles(request)
    return [{"name": file.file_name, "path": file.file_path} for file in response.files]
