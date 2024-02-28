from manager import FilmManager


def main():
    # I create an instance of the class FilmManager to use its methods
    obj_manager = FilmManager()
    while True:
        main = """

1. Create a movie and save the object in a list of movies.
2. Verify if the desired movie exists in the list of movies.
3. Ask the list of movies for all from a specific year.
4. Present a movie from the list.
5. Change the genre of a movie.
6. Exit.

Option: """

        opcion = input(main)
        match opcion:
            case '1':
                obj_manager.create_movie()
            case '2':
                obj_manager.verify_movie()
            case '3':
                obj_manager.ask_according_date()
            case '4':
                obj_manager.present_movie()
            case '5':
                obj_manager.change_gender()
            case '6':
                return
            case _:
                print('Incorrect option')


if __name__ == "__main__":
    main()
