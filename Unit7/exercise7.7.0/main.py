from file_manager import *


def menu():
    # instancio un objeto de gestor de computadoras para usar sus metodos
    manager = FileManager()
    path = os.path.abspath(os.path.dirname(__file__))
    while True:
        menu = """

1. Create a blank file, with the name the user desires
2. Write data to the file without overwriting existing content
3. Delete the data from the file
4. Read the file line by line
5. Exit

Option:"""
        option = input(menu)
        match option:
            case '1':
                manager.create_blanc_file(path)
            case '2':
                manager.write_data(path)
            case '3':
                manager.truncate_file(path)
            case '4':
                manager.read_line_to_line(path)
            case '5':
                return
            case _:
                print('Incorrect income')


if __name__ == "__main__":
    menu()
