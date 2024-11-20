import sqlalchemy as sqla
import database

CONNECTION_STRING = "mysql+pymysql://root@192.168.3.111/is61-3/agt2ge8r"

class Database():
    def __init__(self):
        self.engine = sqla.create_engine(CONNECTION_STRING)
        self.connaction = self.engine.connect()
