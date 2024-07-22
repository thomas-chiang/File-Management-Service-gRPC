from concurrent import futures
import grpc
import file_service_proto.file_service_pb2_grpc as file_service_pb2_grpc
from service import FileService
from db import engine
from adapter import PersistentAdapter

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    adapter = PersistentAdapter(engine)
    file_service_pb2_grpc.add_FileServiceServicer_to_server(FileService(adapter), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()