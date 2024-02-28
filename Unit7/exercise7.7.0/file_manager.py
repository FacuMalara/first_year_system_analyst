"""

Exercise 7.7
Create a program with four options:

Create a blank file, with the name the user desires
Write data to the file without overwriting existing content
Delete the data from the file
Read the file line by line
"""
import os


class FileManager:
    def create_blanc_file(self, path):
        try:
            file_name = input(
                'Enter file´s name with it´s extension: ')
            path_file = f"{path}\\{file_name}"
            file = open(path_file, 'w')
            file.close()
        except Exception as e:
            print(e)

    def write_data(self, path):
        try:
            file_name = input(
                'Enter file´s name with it´s extension: ')
            path_archivo = f"{path}\\{file_name}"
            file = open(path_archivo, 'a+')
            new_data = input('Enter the text to update: ')
            file.write(new_data)
            file.close()
        except Exception as e:
            print(e)

    def truncate_file(self, path):
        try:
            file_name = input(
                'Enter file´s name with it´s extension: ')
            path_archivo = f"{path}\\{file_name}"
            file = open(path_archivo, 'a')
            file.truncate(0)
            file.close()
        except Exception as e:
            print(e)

    def read_line_to_line(self, path):
        try:
            file_name = input(
                'Enter file´s name with it´s extension: ')
            path_archivo = f"{path}\\{file_name}"
            file = open(path_archivo, 'r')
            line = file.readline()
            while line != '':
                print(line, end='')
                input('Keep reading...')
                line = file.readline()
            file.close()
        except Exception as e:
            print(e)
