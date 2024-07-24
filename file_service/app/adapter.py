from sqlmodel import Session, select
from model import File


class PersistentAdapter:
    def __init__(self, engine):
        self.engine = engine

    def upload_file_to_db(self, user_name, file_name, file_path):
        with Session(self.engine) as session:
            file_record = File(
                user_name=user_name,
                file_name=file_name,
                file_path=file_path
            )
            session.add(file_record)
            session.commit()

    def get_file_records_from_db(self, user_name):
        with Session(self.engine) as session:
            statement = select(File).where(File.user_name == user_name)
            return session.exec(statement).all()
        
    def get_all_file_records_from_db(self):
        with Session(self.engine) as session:
            statement = select(File)
            return session.exec(statement).all()