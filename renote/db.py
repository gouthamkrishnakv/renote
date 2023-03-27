import sqlite3

from renote import note

DB_NAME = "renote.db"

CHECK_DB_EXISTS = "SELECT name FROM sqlite_master WHERE type = 'table' AND NAME='{}'"


class DB:
    conn: sqlite3.Connection

    def __init__(self) -> None:
        self.conn = sqlite3.connect(DB_NAME)
        self.setup()

    def _table_exists(self, table_name: str) -> bool:
        val = self.conn.cursor().execute(CHECK_DB_EXISTS.format(table_name))
        return val.fetchone() != None

    def _create_tables(self):
        self.conn.cursor().execute(note.CREATE_NOTES_TABLE)

    def setup(self):
        if not self._table_exists("notes"):
            print("Table 'notes' does not exist, creating.")
            self._create_tables()

    # def list_notes(self) -> list[note.Note]:
    #     notes = self.conn.cursor().execute(note.SELECT_ALL_NOTES).fetchall()
    #     if len(notes) > 0:
    #         return list(map(lambda n: note.Note(*n), notes))
    #     else:
    #         return []

    # def insert_note(self, title, desc):
    #     self.conn.cursor().execute(note.INSERT_NOTE, [title, desc])
    #     self.conn.commit()

    # def delete_note(self, note_id: int):
    #     self.conn.cursor().execute(note.DELETE_NOTE, [note_id])
    #     self.conn.commit()

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()
