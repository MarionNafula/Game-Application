from database import get_connection

class Game:
    def __init__(self, id=None, name=None, genre=None, developer_id=None):
        self.id = id
        self.name = name
        self.genre = genre
        self.developer_id = developer_id

    @classmethod
    def create_table(cls):
        with get_connection() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    developer_id INTEGER NOT NULL,
                    FOREIGN KEY (developer_id) REFERENCES developers (id)
                )
                """
            )

    def save(self):
        with get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO games (name, genre, developer_id) VALUES (?, ?, ?)",
                (self.name, self.genre, self.developer_id),
            )
            self.id = cursor.lastrowid

    @classmethod
    def get_all(cls):
        with get_connection() as conn:
            return conn.execute("SELECT * FROM games").fetchall()

    @classmethod
    def find_by_id(cls, game_id):
        with get_connection() as conn:
            return conn.execute(
                "SELECT * FROM games WHERE id = ?", (game_id,)
            ).fetchone()

    @classmethod
    def delete(cls, game_id):
        with get_connection() as conn:
            conn.execute("DELETE FROM games WHERE id = ?", (game_id,))
