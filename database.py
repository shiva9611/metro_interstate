from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from logger import lg

class DB_Operation:
    def __init__(self):
        self.cloud_config= {
        'secure_connect_bundle': 'D:\Jupyter_notebooks\secure-connect-metro-interstate.zip'
    }
        self.auth_provider = PlainTextAuthProvider('rkuTgTxSuAEKEmTQMymUxooc', 'Z,0q-2mZXL8e9m7,coLn+Mb9zUhxKywISc_63tC-oe9TDefCwUH7nko0qYhbeeBZZ8rKB.qn.3eCFgD.1CixZhp39cq-OiwvD5g.s2wgyqbFbAp,AyJUG,JFIaEgjdbK')
        self.cluster = Cluster(cloud=self.cloud_config, auth_provider=self.auth_provider)
        self.session = self.cluster.connect()

        self.row = self.session.execute("select release_version from system.local").one()
    if self.row:
        lg.info(f'Conncted to the casandra {self.row[0]}')
    else:
        lg.error("An error occurred in connecting cassandra")

    def create_table(self,table_name):
        pass

    def insert_data (self,string):
        pass

    def insert_data_many(self,string):
        pass

