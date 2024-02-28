
class Film:
    def __init__(self, name, year, gender, nationality, score) -> None:
        self.name = name
        self.year = year
        self.gender = gender
        self.nationality = nationality
        self.score = score

    @staticmethod
    def create_films():
        name = input("Enter film´s name: ")
        year = input("Enter year: ")
        gender = input("Enter gender: ")
        nationality = input("Enter nationality: ")
        score = input("Enter score: ")
        film = Film(name, year, gender, nationality, score)
        return film

    def present_film(self):
        print(f"""Film is {self.name}, of gender {self.gender},
of year {self.year}, and got the score of {self.score}, and was shot in {self.nationality}""")

    def return_year(self, year):
        if self.year < year:
            return "Is lower than passed by parameter"
        elif self.year == year:
            return "Is equal to passed by parameter"
        elif self.year > year:
            return "Is higher than passed by parameter"
        else:
            return "Something failed"

    def change_gender(self):
        self.gender = input("Enter new gender: ")

    def change_score(self):
        self.score = input("Enter new score: ")
