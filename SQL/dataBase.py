import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData

class DataBaseComponet:
    pass

if __name__ == "__main__":
    metadata = MetaData()
    engine = create_engine('sqlite:///bookstore.db')
    metadata.create_all(engine)