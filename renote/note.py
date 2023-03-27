from dataclasses import dataclass

CREATE_NOTES_TABLE = """CREATE TABLE IF NOT EXISTS notes (
    id integer primary key,
    title text not null,
    description text,
    created datetime )"""

@dataclass
class Note:
    id: int
    title: str
    description: str | None

    def __repr__(self) -> str:
        if self.description is not None:
            return f"{self.id} [{self.title}]: {self.description}"
        else:
            return f"{self.id} [{self.title}]"
