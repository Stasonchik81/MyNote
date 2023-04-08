

def printNotes(notes):
    for note in notes:
        print(f"{note.id}. {note.date} - {note.time}\t{note.title}\n{note.message}")

def printNote(notes):
    print(f"{notes.id}. {notes.date} - {notes.time}\t{notes.title}\n{notes.message}")

def printStatus(status):
    if status == 0:
        print("OK")
    elif status < -1:
        print("Неверный формат даты!")
    else:
        print("Запись не найдена!")

def printAdd(number):
    if (isinstance(number, int)):
        print(f"Запись номер {number} добавлена!")
    else:
        print("Возникла ошибка!")


