from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///my_db.sqlite3', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), unique=True)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        # self.fullname = fullname
        # self.password = password

    def __repr__(self):
        return "User: {self.name}"


Base.metadata.create_all(engine)
