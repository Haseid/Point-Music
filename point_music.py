from tkinter import *
from os import listdir		#get file names
from pygame import mixer	#package to play mp3 files
from random import sample

class Gui(object):
	songs = listdir("Music/")	#fetching song-file names
	ant = len(songs)			#amount of songs
	random_numbers = []			#array with random numbers
	history = []				#array to keep track of the songs in the random order
	history_index = -1			#index to keep track of history

	def __init__(self, master):
		# setting up master frame
		master.title("Point Music")
		master.resizable(width=FALSE, height=FALSE)

		# creating frames
		self.left_frame = Frame(master, bg="black", width=400, height=300)
		self.right_frame = Frame(master, bg="green", width=400, height=300)
		self.inner_left_frame = Frame(self.left_frame, bg="red")
		self.inner_right_frame = Frame(self.right_frame, bg="red")

		# layout for frames
		self.left_frame.grid(row=0, column=0)
		self.right_frame.grid(row=0, column=1)
		self.inner_left_frame.place(in_=self.left_frame, anchor="c", relx=.5, rely=.5)
		self.inner_right_frame.place(in_=self.right_frame, anchor="c", relx=.5, rely=.5)

		# creating widgets in left frame
		self.label_static_1 = Label(self.inner_left_frame, text="Playing now:")
		self.label_playing_song = Label(self.inner_left_frame, text="Nothing")
		self.button_play = Button(self.inner_left_frame, text="Play next", command=self.start_music)

		# layout for widgets in left frame
		self.label_static_1.grid(row= 0)
		self.label_playing_song.grid(row= 1)
		self.button_play.grid(row= 2)

		# creating widgets in right frame
		self.label_static_2 = Label(self.inner_right_frame, text="Playing now:")
		self.label_next_song = Label(self.inner_right_frame, text="")
		self.button_previous = Button(self.inner_right_frame, text="Previous", command=self.previous_song)
		self.button_next = Button(self.inner_right_frame, text="Next", command=self.next_song)

		# layout for widgets in right frame
		self.label_static_2.grid(row=0, columnspan=2)
		self.label_next_song.grid(row=1, columnspan=2)
		self.button_previous.grid(row=2, column=0)
		self.button_next.grid(row=2, column=1)

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