from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy import Integer, String, DateTime
from database import DataBase


class MyDB(DataBase):

    def __init__(self, db_path):
        engine_name = "sqlite:///" + db_path
        self.engine = create_engine(engine_name, echo=True)
        self.metadata = MetaData(bind=None)
        # Table demo
        self.table_demo = Table('table_demo', self.metadata,
                                Column('id', Integer, primary_key=True),
                                Column('name', String, nullable=False),
                                Column('created_at', DateTime, nullable=False),
                                Column('updated_at', DateTime, nullable=True),
                                Column('deleted_at', DateTime))
        # Init base class data
        DataBase.__init__(self, self.metadata, self.engine)

    # TODO: Add new methods here for personalized queries
