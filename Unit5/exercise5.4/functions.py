
def ask_str(text_to_ask):
    while True:
        try:
            varaible_str = input(text_to_ask)
            varaible_str_ns = no_space(varaible_str)
            if varaible_str_ns.isalpha():
                return varaible_str
            else:
                print("Invalid data")
        except ValueError as e:
            print(f'Enter string value {e}')


def no_space(varaible_str):
    varaible_str_ns = ""
    for char in varaible_str:
        if char != " ":
            varaible_str_ns += char
    return varaible_str_ns


def list():
    subjects = 5
    list_ = []
    for subject in range(subjects):
        subjects = ask_str("Enter subject: ")
        list_.append(subjects)
    list_.sort()
    print(list_)
    return
