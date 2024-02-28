import os
list1 = ["1234567"]
# list1.split(sep="")
print(list1)

string = "Hello-how-are-you"
list1 = string.split(sep="-")
print(list1)

list1 = list("Hello how are you")
print(list1)

text = [2, 3, 4, 6, 1, 9]
text.append(9)
print(text)
text.sort()

print(text)


def get_path():
    return os.path.abspath(os.path.dirname(__file__))


with open(f"{get_path()}//text.txt", "r") as file:
    print(file.read())
    file.close()
