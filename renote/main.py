import argparse
from renote.db import DB
from renote.note_repo import NoteRepository
from typing import Any

def print_notes(note_repo: NoteRepository, db: DB):
    notes = note_repo.list_notes(db.conn)
    if len(notes) > 0:
        for note in notes:
            print(note)
    else:
        print("-- NO NOTES --")


def add_note(note_repo: NoteRepository, db: DB, args: Any):
    title = None
    desc = None
    if not args.todo:
        title = input("Title: ")
        if title == "":
            print("ERROR: Title is not given!")
            exit(1)
        desc = input("Description: ")
    else:
        title = " ".join(args.todo)
    note_repo.insert_note(db.conn, title, desc)


def main() -> None:
    # Setup
    db = DB()
    note_repo = NoteRepository()
    # Do things here
    parser = argparse.ArgumentParser(
        prog="renote",
        description="ReNote Note Keeper",
        epilog="Copyright (C) 2023 Goutham Krishna K V",
    )
    parser.add_argument("-a", "--add", action="store_true")
    parser.add_argument("-d", "--delete", type=int)
    parser.add_argument("todo", nargs="*")

    args = parser.parse_args()

    # Have a UI for adding
    if args.add:
        add_note(note_repo, db, args)
    elif args.delete:
        note_repo.delete_note(db.conn, args.delete)
    else:
        print_notes(note_repo, db)
