def ask_number(text_to_ask):
    while True:
        try:
            number1, number2 = input(text_to_ask), input()
            if number1.isnumeric() and number2.isnumeric():
                new_number1 = int(number1)
                new_number2 = int(number2)
                return new_number1, new_number2
            else:
                print("Incorrect income")
        except ValueError as e:
            print(f"Error {e}")


def show_list(base):
    for key, list in base.items():
        print(f"\n{key}:\n ")
        for element in list:
            print(f"{element}")
    print("\n")


def add_new(base):
    print("What do you disere to add?")
    option = input("film/serie: ").lower()
    if option == "film":
        base["films"].append(
            input("Enter a film: ").lower())
        return base
    elif option == "serie":
        base["series"].append(
            input("Enter a serie: ").lower())
        return base
    else:
        print("Incorrect income")
    print("If it doesn't appear updated, I didn't enter it correctly, or the movie/series already exists.")


def delete_thing(base):
    thing_to_delete = input("Enter film or serie to delete: ").lower()
    if thing_to_delete in base["films"]:
        base["films"].remove(thing_to_delete)
        return base
    elif thing_to_delete in base["series"]:
        base["series"].remove(thing_to_delete)
        return base
    else:
        print("Object wasn´t found")


def show_manualy(base):
    try:
        option = input("Choose list to see, series/films: ")
        if option == "films":
            start, end = ask_number("Enter two numbers: ")
            for film in base["films"]:
                if film == base["films"][start-1]:
                    print(base["films"][start-1:end])
        elif option == "series":
            start, end = ask_number("Enter two numbers: ")
            for serie in base["series"]:
                if serie == base["series"][start-1]:
                    print(base["series"][start-1:end])
        else:
            print("Invalid option")
    except Exception as e:
        print(f"Error: {e}")


def search_according_word(base):
    print("If the search does not give a result on screen it means the element was not found")
    option = input("Choose list to enter, films/series: ")
    if option == "films":
        word = input("Enter a word: ").lower()
        for film in base["films"]:
            if word in film.lower():
                print(f"Film: {film}")
    elif option == "series":
        word = input("Enter a word: ").lower()
        for serie in base["series"]:
            if word in serie.lower():
                print(f"Serie is: {serie}")
    else:
        print("Incorrect option, you must enter one of this two elements: films/series")
        search_according_word(base)
