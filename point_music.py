from os import listdir			# package to get file names
from pygame import mixer		# package to play mp3 files
from random import sample		# package to randomize numbers
from tkinter import *			# package for GUI

class Gui(object):
	# attributes for functionality
	start = True
	history = []
	history_index = -1
	random_numbers = []
	songs = listdir("Music/")
	ant = len(songs)

	# attributes for GUI
	color = "SteelBlue4"
	font_1 = "Arial 11 bold"
	font_2 = "Arial 11"

	def __init__(self, master):
		# setting up master frame
		master.title("Point Music")
		master.resizable(width=FALSE, height=FALSE)
		master.bind("<space>", self.start_stop_music)
		master.bind("<Left>", self.previous_song)
		master.bind("<Right>", self.next_song)

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
		self.button_play = Button(self.frame_inner_left, text="Play next", command=lambda: self.start_stop_music(""))

		# layout for widgets in left frame
		self.label_static_1.grid(row= 0)
		self.label_playing_song.grid(row= 1)
		self.button_play.grid(row= 2)

		# creating widgets in right frame
		self.label_static_2 = Label(self.frame_inner_right, text="Playing next", bg=self.color, font=self.font_1)
		self.label_next_song = Label(self.frame_inner_right, text="", bg=self.color, font=self.font_2)
		self.button_next = Button(self.frame_inner_right_2, text="Next", command=lambda: self.next_song(""))
		self.button_previous = Button(self.frame_inner_right_2, text="Previous", command=lambda: self.previous_song(""))

		# layout for widgets in right frame
		self.label_static_2.grid(row=0)
		self.label_next_song.grid(row=1)
		self.frame_inner_right_2.grid(row=2)
		self.button_previous.pack(side=LEFT)
		self.button_next.pack(side=LEFT)

		# start up
		mixer.init()
		self.next_song("")

	# functions for keybind events and buttons
	def start_stop_music(self, event):
		if self.start:
			mixer.music.load("Music/"+self.songs[self.history[self.history_index]])
			mixer.music.play()
			self.label_playing_song.config(text=self.songs[self.history[self.history_index]][:-4])
			self.button_play.config(text="Fade out")
			self.next_song("")
			self.start = False
		else:
			mixer.music.fadeout(1500)
			self.button_play.config(text="Play next")
			self.start = True

	def next_song(self, event):
		self.history_index += 1
		while (len(self.history) <= self.history_index):
			if self.random_numbers == []:
				self.random_numbers = sample(range(self.ant), self.ant)
			self.random_number = self.random_numbers.pop()
			self.history.append (self.random_number)
		self.label_next_song.config(text=self.songs[self.history[self.history_index]][:-4])

	def previous_song(self, event):
		if self.history_index > 0:
			self.history_index -= 1
			self.label_next_song.config(text=self.songs[self.history[self.history_index]][:-4])

root = Tk()
window = Gui(root)
root.mainloop()