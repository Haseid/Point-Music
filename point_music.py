from os import listdir		#get file names
from pygame import mixer	#package to play mp3 files
import random				#rng
import tkinter
songsDir = "Music/"			#music directory
songs = listdir(songsDir)	#fetching song-file names
ant = len(songs)			#amount of songs
random_numbers = []			#array with random numbers
history = []				#array to keep track of the songs in the random order
history_index = -1			#index to keep track of history
mixer.init()

def Next_song():
	global random_numbers
	global history
	global history_index
	history_index += 1
	while (len(history) <= history_index):
		if random_numbers == []:
			random_numbers = random.sample(range(ant), ant)
		random_number = random_numbers.pop()
		history.append (random_number)
	label_3.config(text=songs[history[history_index]][:-4])

def Previous_song():
	global history_index
	if history_index > 0:
		history_index -= 1
		label_3.config(text=songs[history[history_index]][:-4])

def Start_music():
	mixer.music.load(songsDir+songs[history[history_index]])	#loads a new song
	mixer.music.play()
	label_1.config(text=songs[history[history_index]][:-4])
	button_1.config(text="Fade out", command=Stop_music)
	Next_song()

def Stop_music():
	mixer.music.fadeout(1500)									#fadeout over milliseconds
	button_1.config(text="Play next", command=Start_music)

graphic = tkinter.Tk()
graphic.title("Point Music")
frame_main = tkinter.Frame(graphic, width=500, height=150)		#main frame
frame_center_outer = tkinter.Frame(frame_main)					#centred frame
frame_center_left = tkinter.Frame(frame_center_outer)
frame_center_right = tkinter.Frame(frame_center_outer)
frame_text_upper_1 = tkinter.Frame(frame_center_left)
frame_buttons_lower_1 = tkinter.Frame(frame_center_left)
frame_text_upper_2 = tkinter.Frame(frame_center_right)		
frame_buttons_lower_2 = tkinter.Frame(frame_center_right)

frame_main.pack(fill="both")
frame_center_outer.place(in_=frame_main, anchor="c", relx=.5, rely=.5)
frame_center_left.pack(side=tkinter.LEFT, anchor="w")
frame_center_right.pack(side=tkinter.RIGHT, anchor="e")
#left side
frame_text_upper_1.pack(side=tkinter.TOP)
frame_buttons_lower_1.pack(side=tkinter.BOTTOM)
#right side
frame_text_upper_2.pack(side=tkinter.TOP)
frame_buttons_lower_2.pack(side=tkinter.BOTTOM)

#left side
label_0 = tkinter.Label(frame_text_upper_1, text="Playing now:")
label_1 = tkinter.Label(frame_text_upper_1, text="Nothing")
button_1 = tkinter.Button(frame_buttons_lower_1, text="Start music", command=Start_music)
button_2 = tkinter.Button(frame_buttons_lower_1, text="Exit", command=graphic.quit)
#right side
label_2 = tkinter.Label(frame_text_upper_2, text="Next song:")
label_3 = tkinter.Label(frame_text_upper_2, text="")
button_3 = tkinter.Button(frame_buttons_lower_2, text="Previous", command=Previous_song)
button_4 = tkinter.Button(frame_buttons_lower_2, text="Next", command=Next_song)

label_0.pack(side=tkinter.TOP)
label_1.pack()
button_1.pack(side=tkinter.LEFT)
button_2.pack(side=tkinter.LEFT)

label_2.pack(side=tkinter.TOP)
label_3.pack()
button_3.pack(side=tkinter.LEFT)
button_4.pack(side=tkinter.LEFT)

Next_song()
graphic.mainloop()