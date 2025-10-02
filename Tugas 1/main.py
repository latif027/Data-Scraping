import os

def create_directory (folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

create_directory("Scraping")

def create_new_file (path):
    f = open(path,'w')
    f.write("")
    f.close()

create_new_file("Scraping/test.txt")

# MENULIS ISI FILE
def write_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

write_to_file("Scraping/test.txt")

# MENGHAPUS ISI FILE PYTHON
def clear_file (path):
    f = open(path, 'w')
    f.close()

clear_file("Scraping/test.txt")

import os

def does_file_exist(path):
    return os.path.isfile(path)

print(does_file_exist("scraping/file.txt"))

# MEMBACA ISI FILE PYTHON
def read_data(path):
    with open(path, 'r') as file:
        for line in file:
            print(line)
read_data("scraping/test.txt")

# REMOVE FILE
def remove_file(path):
    if does_file_exist(path):
        os.remove(path)
    else:
        print("File tidak ada")

remove_file("Scraping/file1.txt")