from tkinter import *
from os import listdir			# package to get file names
from pygame import mixer		# package to play mp3 files
from random import sample		# package to randomize numbers

class Gui(object):
	songs = listdir("Music/")	# fetching song-file names
	ant = len(songs)			# amount of songs

	history = []				# array to keep track of the songs in the random order
	history_index = -1			# index to keep track of history
	random_numbers = []			# array with random numbers
	
	color = "SteelBlue4"		# background color
	font_1 = "Arial 11 bold"	# font for static label
	font_2 = "Arial 11"			# font for label

	def __init__(self, master):
		# setting up master frame
		master.title("Point Music")
		master.resizable(width=FALSE, height=FALSE)

		# creating frames
		self.frame_left = Frame(master, bg=self.color, width=350, height=250)
		self.frame_right = Frame(master, bg=self.color, width=350, height=250)
		self.frame_inner_left = Frame(self.frame_left, bg=self.color)
		self.frame_inner_right = Frame(self.frame_right, bg=self.color)
		self.frame_inner_right_2 = Frame(self.frame_inner_right)

		# layout for frames
		self.frame_left.grid(row=0, column=0)
		self.frame_right.grid(row=0, column=1)
		self.frame_inner_left.place(in_=self.frame_left, anchor="c", relx=.5, rely=.5)
		self.frame_inner_right.place(in_=self.frame_right, anchor="c", relx=.5, rely=.5)

		# creating widgets in left frame
		self.label_static_1 = Label(self.frame_inner_left, text="Playing now", bg=self.color, font=self.font_1)
		self.label_playing_song = Label(self.frame_inner_left, text="Nothing", bg=self.color, font=self.font_2)
		self.button_play = Button(self.frame_inner_left, text="Play next", command=self.start_music)

		# layout for widgets in left frame
		self.label_static_1.grid(row= 0)
		self.label_playing_song.grid(row= 1)
		self.button_play.grid(row= 2)

		# creating widgets in right frame
		self.label_static_2 = Label(self.frame_inner_right, text="Playing next", bg=self.color, font=self.font_1)
		self.label_next_song = Label(self.frame_inner_right, text="", bg=self.color, font=self.font_2)
		self.button_next = Button(self.frame_inner_right_2, text="Next", command=self.next_song)
		self.button_previous = Button(self.frame_inner_right_2, text="Previous", command=self.previous_song)

		# layout for widgets in right frame
		self.label_static_2.grid(row=0)
		self.label_next_song.grid(row=1)
		self.frame_inner_right_2.grid(row=2)
		self.button_previous.pack(side=LEFT)
		self.button_next.pack(side=LEFT)

		# start up
		mixer.init()
		self.next_song()

	def start_music(self):
		mixer.music.load("Music/"+self.songs[self.history[self.history_index]])
		mixer.music.play()
		self.label_playing_song.config(text=self.songs[self.history[self.history_index]][:-4])
		self.button_play.config(text="Fade out", command=self.stop_music)
		self.next_song()

	def stop_music(self):
		mixer.music.fadeout(1500)
		self.button_play.config(text="Play next", command=self.start_music)

	def next_song(self):
		self.history_index += 1
		while (len(self.history) <= self.history_index):
			if self.random_numbers == []:
				self.random_numbers = sample(range(self.ant), self.ant)
			self.random_number = self.random_numbers.pop()
			self.history.append (self.random_number)
		self.label_next_song.config(text=self.songs[self.history[self.history_index]][:-4])

	def previous_song(self):
		if self.history_index > 0:
			self.history_index -= 1
			self.label_next_song.config(text=self.songs[self.history[self.history_index]][:-4])

root = Tk()
window = Gui(root)
root.mainloop()