

def printNotes(notes):
    for note in notes:
        print(f"{note.id}. {note.date}\t{note.title}\n{note.message}")

def printNote(notes):
    print(f"{notes.id}. {notes.date}\t{notes.title}\n{notes.message}")

def printStatus(status):
    if status == 0:
        print("OK")
    else:
        print("Запись не найдена!")

def printAdd(number):
    if (isinstance(number, int)):
        print(f"Запись номер {number} добавлена!")
    else:
        print("Возникла ошибка!")


