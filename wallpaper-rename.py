#!/usr/bin/env python3

import os
import random

path = "/home/aaron/Pictures/jpgWallpapers/"

directory = os.listdir(path)

random.shuffle(directory)

# renaming them so that i do not get clashes with names. for example, i want to name files 0, 1, 2, 3 but those names are occupied
for file in directory:
    os.rename(f"{path}{file}", f"{path}t{file}")  # t for temporary


for x in range(len(directory)):
    os.rename(f"{path}t{directory[x]}", f"{path}{len(directory) - x}.jpg")
