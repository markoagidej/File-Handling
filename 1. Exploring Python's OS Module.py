# Task 1: Directory Inspector:

import os

def list_directory_contents(path):
    try:
        if path:
            print(os.listdir(path))
        else:
            print(os.listdir("/"))
    except:
        print("Enter a valid file path!")


list_directory_contents(input("Type a path on your computer to list (or leave blank for project directory): "))


# Task 2: File Size Reporter:

def report_file_sizes(directory):
    try:
        path = "/"
        if directory:
            path = directory

        for item in os.listdir(path):
            file_path = os.path.join(path, item)
            if os.path.isfile(file_path):
                print(f"{item} - {os.path.getsize(file_path)}")
        
    except:
        print("Enter a valid file path!")


report_file_sizes(input("Type a path on your computer to see file sizes (or leave blank for project directory): "))


# Task 3: File Extension Counter:


def count_file_extensions(directory):

    file_ext_dict = {}
    
    try:
        path = "/"
        if directory:
            path = directory

        for item in os.listdir(path):
            file_path = os.path.join(path, item)
            if os.path.isfile(file_path):
                extension = os.path.splitext(item)[-1][1:].upper()
                if extension in file_ext_dict:
                    file_ext_dict[extension] += 1
                else:
                    file_ext_dict[extension] = 1

        print(file_ext_dict)
        
    except:
        print("Enter a valid file path!")


count_file_extensions(input("Type a path on your computer to count file extensions (or leave blank for project directory): "))