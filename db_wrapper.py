from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base


class DBWrapper:
    def __init__(self, db_host, db_port, database, db_user, db_password):
        # postgres
        self.engine = create_engine(f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{database}")

        # sqlite
        # self.engine = create_engine('sqlite:///flaskdemo.db')
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()
