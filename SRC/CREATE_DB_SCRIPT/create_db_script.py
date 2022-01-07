
from SRC import db_connector
from . import tables



def create_database_script():
    db_connector.try_create_db()

    for table_name in tables.TABLES:
        table_description = tables.TABLES[table_name]
        db_connector.create_table(table_name, table_description)
