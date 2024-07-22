from pydantic import BaseModel

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