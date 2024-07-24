import os

from sqlmodel import create_engine

# Update with your actual username, password, and database name
USERNAME = 'yourdbuser'
PASSWORD = 'yourdbpassword'
DATABASE_NAME = 'yourdbname'
HOST = os.getenv('POSTGRES_DB')
PORT = '5432'  # Default PostgreSQL port, adjust if needed

# Create the database engine
DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
engine = create_engine(DATABASE_URL)
