from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL; using SQLite in the current
# directory with file 'blog.db'
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# Create the SQLAlchemy engine; 'check_same_thread=False' is required for
# SQLite to allow multiple threads
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Base class for creating ORM models
Base = declarative_base()

# Create a session factory to interact with the database
# - bind=engine links the session to our database engine
# - autocommit=False ensures changes are committed manually
# - autoflush=False prevents automatic flushing of changes before queries
sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
