import json
from classes.note import Note

#требуется получить количество записей и (или) номер последней !!!

def read(param):
    with open("db/myNotes.json", "r") as read_file:
       data = json.load(read_file) #список объектов Note
    if param.date:
        #получаем список note по дате
        data
    elif param.all:
        #получаем весь список note
        data
    elif param.number:
        #получаем список note по номеру
        data
    else:
        return -1
    return data

def write(data):
    note = Note(data.title, data.message)
    with open("db/myNotes.json", "a") as write_file:
        json.dump(note, write_file)
    return note.id

def edit(id, newNote):
    if readFile(id):
        note = newNote
        return 0
    else:
        return -1

def delete(id):
    if readFile(id):
        deleteNote(id)
        return 0
    else:
        return -1



