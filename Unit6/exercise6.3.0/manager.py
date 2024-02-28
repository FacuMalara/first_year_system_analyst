"""
*   Tener un menu con 4 opciones: (GestorPeliculas)
    1. Crear una pelicula y guardar el objeto en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas.
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula
"""
from film import Film


class FilmManager:
    def __init__(self):
        self.list_of_movies: list[Film] = []
        # self.list_of_movies = []

    def create_movie(self):
        name = input('Enter name: ')
        year = input('Enter year: ')
        gender = input('Enter gender: ')
        nationality = input('Enter nationality: ')
        score = input('Enter score: ')
        film = Film(name, year, gender, nationality, score)
        self.list_of_movies.append(film)

    def verify_movie(self):
        name = input('Enter name of the movie you want to verify: ')
        for film in self.list_of_movies:
            if name == film.name:
                print(f'The film {name} exist in the list!!!')

    def ask_according_date(self):
        year = input('Enter year of the movie: ')
        for film in self.list_of_movies:
            if year == film.year:
                print(film.name)

    def present_movie(self):
        name = input('Enter name of the movie you want to check: ')
        for film in self.list_of_movies:
            if name == film.name:
                film.present_film()

    def change_gender(self):
        name = input(
            'Enter the film you want to change gender: ')
        for film in self.list_of_movies:
            if name == film.name:
                new_gender = input('Enter new gender: ')
                film.change_gender(new_gender)
