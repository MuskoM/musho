from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_engine = create_engine("sqlite://database.db")
Session = sessionmaker(db_engine)

