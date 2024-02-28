

class GeometricFigure():

    def __init__(self, type_of_figure, colour, size="little") -> None:
        self.type_of_figure = type_of_figure
        self.colour = colour
        self.size = size

    def define_figure(self):
        print("""
Define the characteristics of the figure: type, color, 
              the size is set by default but can be changed.""")
        self.type_of_figure = input("Enter type: ")
        self.colour = input("Enter colour: ")

    def present_figure(self):
        print(
            f"""Figure is {self.type_of_figure}, of colour {self.colour} and 
has default size {self.size}""")

    def change_colour(self):
        self.colour = input("Enter new colour: ")
        print(f"New colour is {self.colour}")

    def change_size(self):
        if self.size == "little":
            self.size = "big"
            print(f"New size is {self.size}")
