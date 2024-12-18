from database import get_connection

class Developer:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    @classmethod
    def create_table(cls):
        with get_connection() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS developers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
                """
            )

    def save(self):
        with get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO developers (name) VALUES (?)", (self.name,)
            )
            self.id = cursor.lastrowid

    @classmethod
    def get_all(cls):
        with get_connection() as conn:
            return conn.execute("SELECT * FROM developers").fetchall()

    @classmethod
    def find_by_id(cls, developer_id):
        with get_connection() as conn:
            return conn.execute(
                "SELECT * FROM developers WHERE id = ?", (developer_id,)
            ).fetchone()

    @classmethod
    def delete(cls, developer_id):
        with get_connection() as conn:
            conn.execute("DELETE FROM developers WHERE id = ?", (developer_id,))
