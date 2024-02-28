"""
Exercise 6.3
Create a class called Movie:

Its constructor should initialize the attributes name, year, genre, nationality, score.

Four methods should be created in the class:

Present the movie: The movie {name} of {gender} from {year} obtained a score of {score} and was filmed in {nationality}.
Return if the movie's year is greater than, equal to, or less than the one passed as a parameter.
Change the gender of a movie.
Modify the score of the movie (between 1 and 10).

The program should:

Have a menu with 4 options: (MovieManager)

Create a movie and save its name in a list of movies.
Verify if the desired movie exists in the list of movies.
Ask the list of movies for all from a year.
Present a movie from the list.
Change the gender of a movie."""

from classes import Film
from funcs import *


def main():

    list_of_films = [Film]

    while True:
        option = input("""
Welcome to the movie manager:

1. Create Movie
2. Print list of movies
3. Ask the list of movies for all those from a year
4. Present a movie from the list
5. Change the gender of a movie
6. Exit
    
Enter an option: """)

        match option:
            case "1":
                create_film(list_of_films)
            case "2":
                print_list_movies(list_of_films)
            case "3":
                ask_by_year(list_of_films)
            case "4":
                present_movie(list_of_films)
            case "5":
                change_of_gender(list_of_films)
            case "6":
                print("Ending process")
                return
            case _:
                print("Invalid")


if __name__ == "__main__":
    main()
