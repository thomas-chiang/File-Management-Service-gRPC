```
python -m grpc_tools.protoc -I./grpc_service/protobufs --python_out=. --grpc_python_out=. ./grpc_service/protobufs/file_service.proto --pyi_out=.
```