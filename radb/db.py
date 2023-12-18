import sqlite3


class SQLiteConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # An exception occurred, rolling back transaction
            self.conn.rollback()
        else:
            # No exception, commit the transaction
            self.conn.commit()
        self.conn.close()


db_path = None


def set_db_path(db_loc):
    global db_path
    db_path = db_loc


def maybe_create_table():
    with SQLiteConnection(db_path) as conn:
        cursor = conn.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS abbrevs (
            idx INTEGER PRIMARY KEY,
            abbrev TEXT,
            expanded TEXT,
            category TEXT
        );
        '''
        cursor.execute(create_table_query)


def upsert_item(idx: int, abbrev: str, expand: str, category: str):
    with SQLiteConnection(db_path) as conn:
        cursor = conn.cursor()
        query = '''INSERT OR REPLACE INTO abbrevs (idx, abbrev, expanded, category)
             VALUES (?, ?, ?, ?);
        '''
        cursor.execute(query, (idx, abbrev, expand, category))
