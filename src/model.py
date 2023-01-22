import psycopg2
from config import host, user, password, db_name, port

class PostgreSQL:
    "Класс взаимодействия с базой данных PostgresSQL"

    __host = None
    __port = None
    __user = None
    __password = None
    __database = None
    __connection = None
    __instance = None
    __cursor = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance or not cls.__database:
            cls.__instance = super(PostgreSQL, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, host=host, user=user, password=password,
                 port=port, database=db_name):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port
        self.__database = database

    def __connect(self):
        try:
            self.__connection = \
                psycopg2.connect(host=self.__host,
                                port=self.__port,
                                user=self.__user,
                                password=self.__password,
                                database=self.__database)
            self.__cursor = self.__connection.cursor()

        except Exception as ex:
            if self.__connection:
                self.__connection.rollback()
                print("[INFO] Error while working with PostgreSQL", _ex)

    def __close(self):
        self.__connection.close()
        print("[INFO] PostgreSQL connection closed")


    def create_table(self, table_name, table_structure):
        query = "CREATE TABLE " + table_name + table_structure
        self.__connect()
        self.__cursor.execute("DROP TABLE IF EXISTS {0}".format(table_name))
        self.__cursor.execute(query)
        self.__connection.commit()
        self.__close()

    def paste(self, table_name, *args, **kwargs):
        values = None
        query = 'INSERT INTO {0} '.format(table_name)
        if kwargs:
            keys = kwargs.keys()
            values = tuple(kwargs.values())
            query += "(" + ",".join(["%s"]*len(values)) % tuple(keys) + \
                     ") VALUES (" + ",".join(["%s"]*len(values)) + ")"

        elif args:
            values = args
            query += " VALUES(" + ",".join(["%s"]*len(values)) + ")"

        self.__connect()
        self.__cursor.execute(query, values)
        self.__connection.commit()
        self.__close()

    def select(self, table_name, where=None, *args, **kwargs):
        query = 'SELECT '
        keys = args
        values = tuple(kwargs.values())
        l = len(keys) - 1

        for i, key in enumerate(keys):
            query += key + ' '
            if i < l:
                query += ","

        query += 'FROM %s' % table_name

        if where:
            query += " WHERE {0}".format(where)

        self.__connect()
        self.__cursor.execute(query, values)
        rows = self.__cursor.fetchall()
        self.__connection.commit()
        self.__close()

        return rows

    def select_all(self, table_name):
        self.__connect()
        self.__cursor.execute("SELECT * FROM {0}".format(table_name))
        rows = self.__cursor.fetchall()
        self.__connection.commit()
        self.__close()

        return rows

    def delete(self, table_name, where=None, *args):
        query = "DELETE FROM {0}".format(table_name)
        if where:
            query += ' WHERE %s' % where

        values = tuple(args)

        self.__connect()
        self.__cursor.execute(query, values)
        self.__connection.commit()
        self.__close()

    def update(self, table_name, where=None, *args, **kwargs):
        query = "UPDATE %s SET " % table_name
        keys = kwargs.keys()
        values = tuple(kwargs.values()) + tuple(args)
        l = len(keys) - 1
        for i, key in enumerate(keys):
            query += key+" = %s"
            if i < l:
                query += ","

        query += " WHERE %s" % where

        self.__connect()
        self.__cursor.execute(query, values)
        self.__connection.commit()
        self.__close()

    def return_schedule(self, table_name, day, week, groupp):
        if day == "all":
            query = "SELECT watch[:], discipline[:], classroom[:], teacher[:]" \
                    "FROM {0} " \
                    "WHERE week={1} AND groupp='{2}'"\
                .format(table_name, week, groupp)
        else:
            query = "SELECT watch[:], discipline[:], classroom[:], teacher[:] " \
                    "FROM {0} " \
                    "WHERE week_day = {1} AND week={2} AND groupp='{3}'"\
                .format(table_name, day, week, groupp)

        self.__connect()
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        self.__connection.commit()
        self.__close()

        return(rows)

'''
db = PostgreSQL()
first_table_structure = "(id serial PRIMARY KEY," \
                  "user_name varchar(20) NOT NULL," \
                  "groupp varchar(20) NOT NULL," \
                  "admin bool DEFAULT False)"

second_table_structure = "(id serial PRIMARY KEY," \
                         "groupp varchar(20) NOT NULL," \
                         "week bool NOT NULL," \
                         "week_day smallint NOT NULL," \
                         "watch smallint[] NOT NULL," \
                         "discipline varchar(30)[] NOT NULL," \
                         "classroom varchar(10)[] NOT NULL," \
                         "teacher varchar(20)[] NOT NULL)"



db.create_table("users", first_table_structure)
#db.create_table("sсhedule", second_table_structure)
a = db.return_schedule("sсhedule", "all", True, "'ЭВМ'")
b = db.select_all("sсhedule")
print(a)
print(a[0])
print(a[2][2])
print(a[2][2][1])
print(len(a))
'''
'''
db.paste("test", id='1', first_name="lolishe", name='ata')
a = db.select_all("test")
b = db.select("test", "id=1", "first_name")
db.update("test", 'id=1', first_name='lol', name='attata')
c = db.select_all("test")
print(a)
print(b)
print(c)
'''