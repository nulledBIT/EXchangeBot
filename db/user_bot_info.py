
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.settings_db import *


Base = declarative_base()
class UserBotInfo(Base):
    __tablename__ = 'userbotinfo'
    id = Column(Integer, autoincrement=True, primary_key=True)
    keyqiwi = Column(String)
    id_telegram = Column(Integer, unique=True)



    def __init__(self, keyqiwi, id_telegram):
        self.keyqiwi = keyqiwi
        self.id_telegram = id_telegram


    '''
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.count_coins, self.sum_deal, self.telephone, self.id_telegram, self.text)
    '''


Base.metadata.create_all(db)