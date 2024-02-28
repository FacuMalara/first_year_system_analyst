import os

path = os.path.abspath(os.path.dirname(__file__))
print(path+"//file.txt")

try:
    file = open(path+"\\file.txt", 'r')
    char = file.readline(1)
    while char != "":
        print(char)
        char = file.readline(1)
    file.close()
except:
    print("file doesn´t exist")

mail = 'federico@gmail.com'
user = mail.split('@')[0]
print(f'User is {user}.')
