from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadRequest(_message.Message):
    __slots__ = ("user_name", "file_name", "file_path")
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    file_name: str
    file_path: str
    def __init__(self, user_name: _Optional[str] = ..., file_name: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class UploadResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class RetrieveRequest(_message.Message):
    __slots__ = ("user_name",)
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    user_name: str
    def __init__(self, user_name: _Optional[str] = ...) -> None: ...

class FileRecord(_message.Message):
    __slots__ = ("file_name", "file_path")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    file_path: str
    def __init__(self, file_name: _Optional[str] = ..., file_path: _Optional[str] = ...) -> None: ...

class RetrieveResponse(_message.Message):
    __slots__ = ("files",)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[FileRecord]
    def __init__(self, files: _Optional[_Iterable[_Union[FileRecord, _Mapping]]] = ...) -> None: ...
