# ====================================================================

#        CryptPaste
# The open-source Pastebin alternative
# Under the GPL v3 license

# ====================================================================

from sqlalchemy import create_engine, Column, Integer, Text, String, text
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time

import shared

engine = create_engine(shared.config_json["database"]["url"])#, isolation_level='READ COMMITTED', query_cache_size=1145728, pool_recycle=8, pool_pre_ping=True, pool_reset_on_return='rollback', pool_size=15, max_overflow=20

Base = declarative_base()  

print("DB shema loaded")
class Paste(Base):
        __tablename__ = 'cryptpaste_paste'
        pid = Column(String(55), primary_key=True)
        content = Column(Text)

        is_password_protected = Column(Integer, default=0)
        date = Column(Integer, default=(lambda: int(time.time())))
Base.metadata.create_all(engine)

Session = scoped_session(sessionmaker(bind=engine))

def get_session():
    return Session()

