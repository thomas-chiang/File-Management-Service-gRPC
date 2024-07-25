# File Management Service

## Objective

The goal of this assignment is to implement a file management service using both RESTful APIs and a gRPC service. The service will handle the uploading and retrieval of records, with each record containing the following fields:

- User name
- File name
- File path (note: the actual file is not required)

## Requirements

### RESTful APIs

1. **Upload a Record**
   - **Endpoint:** `/api/files`
   - **Method:** `POST`
   - **Request Body:**
     ```json
     {
       "user_name": "string",
       "file_name": "string",
       "file_path": "string"
     }
     ```
   - **Response:**
     ```json
     {
       "status": "success" | "fail",
       "message": "string"
     }
     ```

2. **Get a Record**
   - **Endpoint:** `/api/files/?username={user_name}`
   - **Method:** `GET`
   - **Response:**
     ```json
     {
       "files": [
         {
           "name": "string1",
           "path": "string1"
         },
         {
           "name": "string2",
           "path": "string2"
         }
       ]
     }
     ```

### gRPC Service

- Implement a gRPC service to manage the business logic for uploading and retrieving records.

### Docker Container

- Deploy your services in Docker containers. Use a `docker-compose` file for orchestration.

## Technologies

- **API Gateway:** FastAPI
- **gRPC Service:** gRPC framework using Python
- **Database:** PostgreSQL
- **Docker:** Use `docker-compose` to launch services
- **Testing:** pytest

## Run
```
docker-compose up --build
```

## GUI to operate these APIs
- http://127.0.0.1:8000/docs or
- https://api-gateway-av6v7gaioq-de.a.run.app/docs

## Test
```
make install-deps
```
```
pytest
```


