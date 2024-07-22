from pydantic import BaseModel
from typing import Literal


class UploadFileRequest(BaseModel):
    user_name: str
    file_name: str
    file_path: str

class FileResponse(BaseModel):
    name: str
    path: str

class UploadFileResponse(BaseModel):
    status: Literal['success', 'fail']
    message: str