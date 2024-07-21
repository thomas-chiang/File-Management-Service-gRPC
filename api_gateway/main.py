from fastapi import FastAPI, HTTPException
import grpc
from file_service_pb2 import UploadRequest, RetrieveRequest
from file_service_pb2_grpc import FileServiceStub

app = FastAPI()

# Connect to gRPC server
channel = grpc.insecure_channel('grpc_service:50051')
stub = FileServiceStub(channel)

@app.post("/api/files")
def upload_file(record: dict):
    request = UploadRequest(user_name=record['user_name'], file_name=record['file_name'], file_path=record['file_path'])
    response = stub.UploadFile(request)
    if response.status == "success":
        return {"status": "success", "message": response.message}
    else:
        raise HTTPException(status_code=400, detail=response.message)

@app.get("/api/files")
def get_files(user_name: str):
    request = RetrieveRequest(user_name=user_name)
    response = stub.GetFiles(request)
    return {"files": [{"name": file.file_name, "path": file.file_path} for file in response.files]}
