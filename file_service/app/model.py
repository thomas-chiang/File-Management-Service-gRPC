from sqlmodel import Field, SQLModel

class File(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_name: str
    file_name: str
    file_path: str
