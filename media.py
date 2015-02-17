#! /usr/bin/env python

import webbrowser

# Class that can be used as a template to create instances for different movies
class Movie():
	"""This class allows you to store Movie related information"""
	def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer, movie_actors, movie_releasedate):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster
		self.trailer_youtube_url = movie_trailer
		self.actors = movie_actors
		self.release_date = movie_releasedate

#Function to open a webbrowser to play movie trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)