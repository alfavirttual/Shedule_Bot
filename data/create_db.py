from model import PostgreSQL
from config import name_users_table, name_schedule_table

def create_db():
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

    db.create_table(name_users_table, first_table_structure)
    db.create_table(name_schedule_table, second_table_structure)

