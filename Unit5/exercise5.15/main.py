"""
Exercise 5.15 (Movie Database)
The program should:

Simulate a database of movies and series with the ability to add, search, delete, and filter movies and series. It should start with the following movies and series in a dictionary:

python
Copy code
base = {
"movies": ["Spider-Man", "The Avengers", "The Avengers 2"],
"series": ["Prison Break", "Money Heist", "The Simpsons"]
}
Have 5 functions available in the menu:

Display the list of movies or series available vertically on the screen.
Add new movies or series (that are not already in the database).
Delete movies or series from the database.
Display, as required by the user, the list of movies from one point to another
(for example, the user wants to see from the 2nd to the 4th in a list).
Search for movies or series containing a word requested by the user
(for example, input("el"), list the movies that contain the word "el").
"""

from functions import *


def menu():

    base = {
        "films": ["Spider-Man", "The Avengers", "The Avengers 2"],
        "series": ["Prison Break", "Money Heist", "The Simpsons"]
    }
    while True:
        option = input("""
Welcome to the menu:

1. View list of movies and series.
2. Add new movies or series.
3. Remove movies or series.
4. Show the list of movies according to the user's request.
5. Search for movies or series containing a word requested by the user.
6. Exit
                       
Enter option: """)

        match option:
            case "1":
                show_list(base)
            case "2":
                base = add_new(base)
            case "3":
                base = delete_thing(base)
            case "4":
                show_manualy(base)
            case "5":
                search_according_word(base)
            case "6":
                print("Ending process")
                return


if __name__ == "__main__":
    menu()
