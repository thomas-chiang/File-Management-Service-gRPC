from file_service_proto.file_service_pb2 import UploadResponse, RetrieveResponse, FileRecord
import file_service_proto.file_service_pb2_grpc as file_service_pb2_grpc
from adapter import PersistentAdapter


class FileService(file_service_pb2_grpc.FileServiceServicer):
    def __init__(self, persistent_adapter: PersistentAdapter):
        self.persistent_adapter = persistent_adapter

    def UploadFile(self, request, context):
        self.persistent_adapter.upload_file_to_db(
            user_name=request.user_name,
            file_name=request.file_name,
            file_path=request.file_path,
        )
        return UploadResponse(
            status="success", message="File record uploaded successfully"
        )

    def GetFiles(self, request, context):
        records = self.persistent_adapter.get_file_records_from_db(
            user_name=request.user_name
        )
        files = [
            FileRecord(file_name=rec.file_name, file_path=rec.file_path)
            for rec in records
        ]
        return RetrieveResponse(files=files)
