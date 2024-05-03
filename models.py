from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Test(Base):
    __tablename__ = "USERS"
    USER_ID = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    SETTOP_NUM = Column(INT, nullable=False)
    USER_NAME = Column(TEXT, nullable=False)
    GENDER = Column(TEXT, nullable=True)
    AGE = Column(INT, nullable=True)
    SPOTIFY = Column(INT, nullable=True)

    def to_dict(self):
        return {
            "USER_ID": self.USER_ID,
            "SETTOP_NUM": self.SETTOP_NUM,
            "USER_NAME": self.USER_NAME,
            "GENDER": self.GENDER,
            "AGE": self.AGE,
            "SPOTIFY": self.SPOTIFY
        }
