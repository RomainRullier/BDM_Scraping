import sqlalchemy as db

class DataBase():
    def init(self, name_database='database'):
        self.name = name_database
        self.url = f"sqlite:///{name_database}.db"
        self.engine = db.create_engine(self.url)
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()
        self.table = self.engine.table_names()


    def get_all_products(self):
        products = self.read_table('products')
        stmt = db.select([products])
        results = self.connection.execute(stmt).fetchall()
        return results




    def table_exists(self, name_table):
        return name_table in self.table

    def create_table(self, name_table, columns):
        table = db.Table(name_table, self.metadata, *columns)
        table.create(self.engine)

    def read_table(self, name_table, return_keys=False):
        table = db.Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)
        if return_keys:table.columns.keys()
        else : return table


    def add_row(self, name_table, kwarrgs):
        name_table = self.read_table(name_table)

        stmt = (
            db.insert(name_table).
            values(kwarrgs)
        )
        self.connection.execute(stmt)


    def delete_row_byid(self, table, id):
        name_table = self.read_table(name_table)

        stmt = (
            db.delete(nametable).
            where(students.c.id == id)
            )
        self.connection.execute(stmt)
        print(f'Row id {id} deleted')

    def select_table(self, name_table):
        name_table = self.read_table(name_table)
        stm = db.select([name_table])
        return self.connection.execute(stm).fetchall()