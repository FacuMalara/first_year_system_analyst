'''

Create a Movie class:

Whose constructor must initialize the attributes name, year, genre, nationality, and score
4 methods must be created in the class:

1. Present the movie: The movie {name} of {genre} from {year} obtained a score of {score} and was filmed in {nationality}
2. Return whether the movie's year is greater than, equal to, or less than the one passed as a parameter
3. Change the genre of a movie
4. Modify the movie's score (between 1 and 10)'''


class Film:
    def __init__(self, name, year, gender, nationality, score):
        self.name = name
        self.year = year
        self.gender = gender
        self.nationality = nationality
        self.score = score

    def present_film(self):
        print(f"""Film´s name is {self.name}, of gender {self.gender},
year {self.year}, got {self.score} in the score, and was
shooted in {self.nationality}""")

    def return_year(self, year):
        if self.year < year:
            return "Lower than the one passed by parameter"
        elif self.year == year:
            return "Equal to the one passed by parameter"
        elif self.year > year:
            return "Higher than the one passed by parameter"
        else:
            return "Something failed"

    def change_gender(self, new_gender):
        self.gender = new_gender

    def change_score(self, new_score):
        self.score = new_score
