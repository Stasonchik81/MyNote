import classes.note as note

test = note.Note("title", "message")
test2 = note.Note("title2", "message2")
all = [test, test2]

def printNotes(notes):
    for note in notes:
        date = note.date.strftime("%d/%m/%Y, %H:%M:%S")
        print(f"{date}\t{note.title}\n{note.message}")

def printStatus(status):
    if status == 0:
        print("OK")
    else:
        print("Запись не найдена!")

def main():
    printNotes(all)



if __name__ == '__main__':
    main()