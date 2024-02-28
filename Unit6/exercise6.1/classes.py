class Persona:

    def __init__(self, name, last_name, age, residence) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age
        self.residence = residence

    def present_persona(self):
        print(
            f"""I am {self.name} {self.last_name}, I have {self.age} years old
and I live in {self.residence}""")

    def groups_by_age(self):
        if self.age <= 14:
            print("Is a kid")
        elif self.age <= 22:
            print("Is an adolescent")
        elif self.age <= 30:
            print("Is young")
        elif self.age <= 50:
            print("Is an adult")
        elif self.age <= 120:
            print("Is old")
