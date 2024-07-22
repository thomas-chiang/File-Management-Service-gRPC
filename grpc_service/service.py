from concurrent import futures
import grpc
from sqlmodel import Field, Session, SQLModel, create_engine, select
from file_service_pb2 import UploadResponse, RetrieveResponse, FileRecord
import file_service_pb2_grpc

# Define the File model
class File(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_name: str
    file_name: str
    file_path: str

# Create the database engine
DATABASE_URL = "postgresql://yourdbuser:yourdbpassword@db/yourdbname"
engine = create_engine(DATABASE_URL)

# Create the database tables
SQLModel.metadata.create_all(engine)

class FileService(file_service_pb2_grpc.FileServiceServicer):
    def __init__(self):
        self.engine = engine

    def UploadFile(self, request, context):
        with Session(self.engine) as session:
            file_record = File(
                user_name=request.user_name,
                file_name=request.file_name,
                file_path=request.file_path
            )
            session.add(file_record)
            session.commit()
            return UploadResponse(status="success", message="File record uploaded successfully")

    def GetFiles(self, request, context):
        with Session(self.engine) as session:
            statement = select(File).where(File.user_name == request.user_name)
            records = session.exec(statement).all()
            files = [FileRecord(file_name=rec.file_name, file_path=rec.file_path) for rec in records]
            return RetrieveResponse(files=files)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_service_pb2_grpc.add_FileServiceServicer_to_server(FileService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
