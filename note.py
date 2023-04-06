import sys
import argparse
import model
import view


def createParser ():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers (dest='command')

    add = subparsers.add_parser ('add')
    add.add_argument ('-m', '--message', default='Запись')
    add.add_argument ('-t', '--title', default='Заголовок')

    get = subparsers.add_parser('get')
    get.add_argument ('-d', '--date', default=False)
    get.add_argument ('-n', '--number', type=int, default=1)
    get.add_argument ('-a', '--all', action='store_const', const=True, default=False)

    delete = subparsers.add_parser('delete')
    delete.add_argument ('-d', '--date', default=False)
    get.add_argument ('-n', '--number', type=int, default=1)
    get.add_argument ('-a', '--all', action='store_const', const=True, default=False)

    edit = subparsers.add_parser('edit')
    edit.add_argument ('-n', '--number', type=int, default=1)
    
 
    return parser

def main():
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    print (namespace)
    #note = Note(namespace.title, namespace.message)
    if namespace.comand == "add":
        response = model.write(namespace)
        view.printStatus(response)
    elif namespace.command == "get":
        notes = model.read(namespace)
        view.printNotes(notes)
    elif namespace.command == "delete":
        response = model.delete(namespace)
        view.printStatus(response)
    elif namespace.command == "edit":
        response = model.edit(namespace)
        view.printStatus(response)
    else:
        print ("Что-то пошло не так...")



if __name__ == '__main__':
    main()



