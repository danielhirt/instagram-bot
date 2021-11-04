import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI



username = "USERNAME" # Your Instagram username
password = "PASSWORD" # Your Instagram password
IG_API = InstagramAPI(username, password) # Variable to store IG API connection

caption = "CAPTION" # Your desired caption

imageDirectory = "DIRECTORY" # Set your directory that contains images to be posted

os.chdir(imageDirectory)
files = sorted([f for f in listdir(files) if isfile(join(files, f))]) # Image files in current directory
print("Amount of files in folder: " + str(len(files)))

IG_API.login() # Login to Instagram

for index, _ in enumerate(files):
    photo = files[index]
    print("Processing file: " + str([index + 1]) + " of " + str(len(files)))
    print("Uploading photo: " + photo + " to Instragram...")
    IG_API.uploadPhoto(photo, caption = caption, upload_id = None) # Upload to Instagram via API
    os.remove(photo) 
    time.sleep(randint(200,300)) # Pause briefly between uploads


