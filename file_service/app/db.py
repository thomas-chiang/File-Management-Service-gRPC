from sqlmodel import Field, SQLModel, create_engine, Session, select

# Create the database engine
DATABASE_URL = "postgresql://yourdbuser:yourdbpassword@db/yourdbname"
engine = create_engine(DATABASE_URL)

