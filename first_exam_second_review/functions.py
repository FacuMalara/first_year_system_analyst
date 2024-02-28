def ask_number(text_to_ask):
    while True:
        number = input(text_to_ask)
        if number.isnumeric():
            new_number = int(number)
            return new_number
        else:
            print("You did not enter numbers")


def add_game(video_games, categories):
    new_game = input("Enter name of the game: ")
    new_game_categorie = input("Enter categorie: ").capitalize()
    year_of_realese = ask_number("Enter year of the game: ")
    if new_game not in video_games and new_game_categorie in categories and 1990 <= year_of_realese <= 2021:
        video_games[0].append(new_game)
        video_games[1].append(new_game_categorie)
        video_games[2].append(year_of_realese)
    else:
        print("Entered game already exists or does not match parameters")
    return video_games


def show_list_of_games(video_games):
    print("\n---BASE VIDEOGAMES---\nName--Categorie--Year\n")
    for i in range(len(video_games[0])):
        print(
            f"{video_games[0][i]}--{video_games[1][i]}--{video_games[2][i]}")


# def ver_video_juegos():
#    print('-- nombre -- año -- categoria')
#    for i in range(len(video_juegos[0])):
#        print(
#            f'{video_juegos[0][i]}-{video_juegos[1][i]}-{video_juegos[2][i]}')


def edit_game_categorie(video_games, categorias):
    video_game_to_edit = input("Enter video game to edit: ")
    if video_game_to_edit in video_games[0]:
        new_categorie = input("Enter new categorie: ").capitalize()
        if new_categorie in categorias:
            index = video_games[0].index(video_game_to_edit)
            video_games[1].pop(index)
            video_games[1].insert(index, new_categorie)
            return video_games
        else:
            print("Specified categorie does not exist in the list")
    else:
        print("Specified video game does not belong to the list")


def add_categories(categories):
    new_categorie = input("Enter new categorie: ").capitalize()
    if new_categorie not in categories:
        categories.append(new_categorie)
    else:
        print("Categorie already exists")
    print("\n", categories)
    return categories


def delete_categories(categories):
    categorie_to_delete = input("Enter categorie to remove: ").capitalize()
    if categorie_to_delete in categories:
        categories.remove(categorie_to_delete)
    else:
        print("\nCategorie does not exist")
    print("\n", categories)
    return categories


def delete_game(video_games):
    game_to_delete = input("Enter game to delete: ")
    if game_to_delete in video_games[0]:
        index = video_games[0].index(game_to_delete)
        video_games[0].pop(index)
    else:
        print("Enter game does not exist in the list")
    return video_games
