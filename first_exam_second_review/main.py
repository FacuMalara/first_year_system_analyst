from functions import *


def main():
    categories = ["Action", "Sports", "Strategy", "Simulation"]
    video_games = [['fifa'], ['Sports'], [2021]]

    while True:
        menu = """\n\n--
Agenda Program--
1. Add a new video game
2. View list of video games (Format: Name - Year - Category)
3. Edit the category of a video game verifying that the category exists, it is edited by name.
4. Add categories to the system, automatically capitalizing the first letter (verifying that it does not already exist).
5. Delete a category from the system, verifying its existence beforehand
6. Delete a game from the list
7. Exit
Enter an option:"""
        option = input(menu)
        if (option == "1"):
            video_games = add_game(video_games, categories)
        elif (option == "2"):
            show_list_of_games(video_games)
        elif (option == "3"):
            video_games = edit_game_categorie(video_games, categories)
        elif (option == "4"):
            categories = add_categories(categories)
        elif (option == "5"):
            categories = delete_categories(categories)
        elif (option == "6"):
            video_games = delete_game(video_games)
        elif (option == "7"):
            print("Finishing process")
            return
        else:
            print('Incorrect option')


if __name__ == "__main__":
    main()
