# imports the os functions
import os

# sets users path location for new folder


def location_gen():
    folder_location = input("Enter the path the folder will be created in: ")
    return folder_location


# sets name for new folder
def name_gen():

    project_name = input("Enter the Folder Name: ")
    return project_name


# creates the folder at the specified path
parent_dir = location_gen()
directory = name_gen()
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '%s' created" % directory)

# change to new directory
os.chdir(path)

# creates a virtual enviornment
os.system("python3 -m venv env")

# activates the virtual enviornment
os.system("env\Scripts\activate")

# installs Django to virtual enviornment
os.system("pip install django")

# verifies Djangos version installed
os.system("python -m django --version")


# inputs users name for django site
def site_name():
    name = input("What is your project name: ")
    return name


# creates the django project
os.system(f'django-admin startproject {site_name()}')


# changes directory to new project directory
site_address = site_name()
path = os.path.join(path, site_address)
os.chdir(path)

# runs new django server
os.system('python manage.py runserver')

# opens webpage of django project
os.system('start http://127.0.0.1:8000/')
