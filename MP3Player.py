import os
from tkinter.filedialog import askdirectory
import pygame #player
from mutagen.id3 import ID3 #metadata
from tkinter import *

root = Tk()
root.minsize(400,400)

index = 0
songList = []

#Prompt user to select directory
#Fetch 'mp3' files from directory
#Play music using pygame
def selectDirectory():
	directory = askdirectory()
	os.chdir(directory)

	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			songList.append(files)
			print(files)

    #uncomment below to play file in index[1]
	#pygame.mixer.init()
	#pygame.mixer.music.load(songList[1]) #plays mp3 on this index
	#pygame.mixer.music.play()

selectDirectory()
root.mainloop()