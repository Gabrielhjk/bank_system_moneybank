from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine('sqlite:///moneybank.db')
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column('name', String(40))
    cpf = Column('cpf', String(11), unique=True)
    password = Column('password', String(25))
    transfer_password = Column('transfer_password', Integer)
    phone_number = Column('phone_number', String(11))
    balance = Column('balance', Float, default = 0.0)

    def __init__(self, name, cpf, password, transfer_password, phone_number, balance):
        self.name = name
        self.cpf = cpf
        self.password = password
        self.transfer_password = transfer_password
        self.phone_number = phone_number
        self.balance = balance

Base.metadata.create_all(bind=db)

