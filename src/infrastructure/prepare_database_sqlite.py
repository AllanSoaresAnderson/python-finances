from src.infrastructure.interfaces import PrepareDataBaseSqlLite, DatabaseConnectionSqlLite

CREATE_BAGGINS = """
CREATE TABLE IF NOT EXISTS baggins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    type TEXT NOT NULL DEFAULT 'M',
    amount_time INTEGER,
    date_created TEXT,
    deletion_date TEXT
)
"""

CREATE_ENTITY = """
CREATE TABLE IF NOT EXISTS entity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    is_person INTEGER NOT NULL CHECK (is_person IN (0, 1)),
    id_baggin INTEGER NOT NULL,

    id_parent INTEGER,
    date_created TEXT,
    date_updated TEXT,
    deletion_date TEXT,

    FOREIGN KEY (id_parent) REFERENCES entity(id),
    FOREIGN KEY (id_baggin) REFERENCES baggins(id)
)
"""

CREATE_TRANSACTION = """
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    start_date TEXT NOT NULL,
    value NUMERIC NOT NULL,

    frequency TEXT,
    variable_frequency TEXT,
    variable_range INTEGER,

    date_created TEXT,
    date_updated TEXT,
    deletion_date TEXT,

    id_baggin INTEGER,
    id_entity INTEGER,

    FOREIGN KEY (id_baggin) REFERENCES baggins(id),
    FOREIGN KEY (id_entity) REFERENCES entity(id)
)
"""


CREATE_INSTALLMENT = """
CREATE TABLE IF NOT EXISTS installment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    value NUMERIC NOT NULL,
    id_transaction INTEGER,

    FOREIGN KEY (id_transaction) REFERENCES transactions(id)
)
"""


CREATE_PAYMENT = """
CREATE TABLE IF NOT EXISTS payment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    value NUMERIC NOT NULL,
    reference_date TEXT NOT NULL,

    id_baggin INTEGER NOT NULL,
    id_transaction INTEGER,
    id_installment INTEGER,

    FOREIGN KEY (id_baggin) REFERENCES baggins(id),
    FOREIGN KEY (id_transaction) REFERENCES transactions(id),
    FOREIGN KEY (id_installment) REFERENCES installment(id)
)
"""


class PrepareDataBaseSqlLiteImpl(PrepareDataBaseSqlLite):

    def __init__(self, database: DatabaseConnectionSqlLite):
        self.database = database

    def prepare(self):
        with self.database.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(CREATE_BAGGINS)
            cursor.execute(CREATE_ENTITY)
            cursor.execute(CREATE_TRANSACTION)
            cursor.execute(CREATE_INSTALLMENT)
            cursor.execute(CREATE_PAYMENT)
            conn.commit()