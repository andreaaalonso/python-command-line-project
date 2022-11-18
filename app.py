from datetime import datetime
from peewee import *

database = PostgresqlDatabase('notes', user='johndoe',
                              password='12345', host='localhost', port=5433)


class BaseModel(Model):
    class Meta:
        database = database


class Note(BaseModel):
    title = CharField()
    content = CharField()
    create_date = DateTimeField()

# simple utility function to create tables


def Connect():
    print("connecting to Notes database")
    database.connect()
    print("Successfully connected to Notes database")


Connect()


def create_tables():
    with database:
        database.create_tables([Note])


def createNote(noteTitle, noteContent):
    print("creating new note")
    newNote = Note.create(
        title=noteTitle,
        content=noteContent,
        create_date=datetime.now())
    newNote.save()
    print("Successfully created new note")


def viewAllNotes():
    print("Below are all the created Notes:")
    for currentNote in Note.select():
        print(currentNote.title + ": " + currentNote.content)


def viewSpecificnote(noteTitle):
    query = Note.select().where(Note.title == noteTitle)
    for currentNote in query:
        print(currentNote.title + ": " + currentNote.content)


def main():
    create_tables()
    finished = False

    while not finished:
        userRequest = input(
            "Would you like to create a new Note or View all notes? (Create/View/Exit)")
        if userRequest.lower() == "create":
            userRequest = input("Would you like to create a new Note? (Y/N)")
            if userRequest.lower() == "n":
                finished = True
            elif userRequest.lower() == "y":
                noteTitle = input(
                    "What would you like the new Note Title to be: ")
                noteContent = input("Please enter the content of your note: ")
                createNote(noteTitle, noteContent)
        elif userRequest.lower() == "view":
            userRequest = input(
                "Would you like to view all notes or a specific one? (All/Specific)")
            if userRequest.lower() == "all":
                viewAllNotes()
            elif userRequest.lower() == "specific":
                userRequest = input("Please enter the Note Title:")
                viewSpecificnote(userRequest.lower())
        elif userRequest.lower() == "exit":
            finished = True


main()
