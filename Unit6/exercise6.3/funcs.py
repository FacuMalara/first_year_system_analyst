from classes import Film
from menu import *


def create_film(list_of_films):
    film = Film.create_films()
    list_of_films.append(film)


def present_movie(list_of_films):
    film_to_present = input("Enter film to present: ").lower()
    for film in list_of_films:
        if film.name.lower() == film_to_present:
            Film.present_film(film)
    else:
        print("Film was not found")


def print_list_movies(list_of_films):
    for film in list_of_films:
        print(film.name)


def ask_by_year(list_of_films):
    choosen_year = input("Enter the year you want to search by: ")
    print(f"From {choosen_year}:")
    for film in list_of_films:
        if film.year == choosen_year:
            print(film.name)
    else:
        print("There were no movies")


def change_of_gender(list_of_films):
    movie = input("Enter movie you need to change gender: ").lower()
    for film in list_of_films:
        if film == movie:
            Film.change_gender(film)
        else:
            print("Film was not found")
