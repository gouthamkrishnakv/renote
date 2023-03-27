import sqlite3

from renote.note import Note

SELECT_ALL_NOTES = "SELECT * FROM notes"
INSERT_NOTE = "INSERT INTO notes (title, description) VALUES (?, ?)"
DELETE_NOTE = "DELETE FROM notes WHERE id = ?"


class NoteRepository:
    def __init__(self):
        pass

    def list_notes(self, conn: sqlite3.Connection) -> list[Note]:
        notes = conn.cursor().execute(SELECT_ALL_NOTES).fetchall()
        if len(notes) > 0:
            return list(map(lambda n: Note(*n), notes))
        else:
            return []
        

    def insert_note(self, conn: sqlite3.Connection, title: str, desc: str | None):
        conn.cursor().execute(INSERT_NOTE, [title, desc])
        conn.commit()

    def delete_note(self, conn: sqlite3.Connection, note_id: int):
        conn.cursor().execute(DELETE_NOTE, [note_id])
        conn.commit()
