from concurrent import futures
import grpc
import psycopg2
from file_service_pb2 import UploadResponse, RetrieveResponse, FileRecord
import file_service_pb2_grpc

class FileService(file_service_pb2_grpc.FileServiceServicer):
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="yourdbname",
            user="yourdbuser",
            password="yourdbpassword",
            host="db"
        )

    def UploadFile(self, request, context):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO files (user_name, file_name, file_path) VALUES (%s, %s, %s)",
                    (request.user_name, request.file_name, request.file_path))
        self.conn.commit()
        return UploadResponse(status="success", message="File record uploaded successfully")

    def GetFiles(self, request, context):
        cur = self.conn.cursor()
        cur.execute("SELECT file_name, file_path FROM files WHERE user_name = %s", (request.user_name,))
        records = cur.fetchall()
        files = [FileRecord(file_name=rec[0], file_path=rec[1]) for rec in records]
        return RetrieveResponse(files=files)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_service_pb2_grpc.add_FileServiceServicer_to_server(FileService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
