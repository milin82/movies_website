#! /usr/bin/env python

import media
import fresh_tomatoes

#Creation of objects for each movie using the Class Movie in the media.py file 
the_imitation_game = media.Movie("The Imitation Game", 
	"Story about Alan Turing",
	"http://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg", 
	"https://www.youtube.com/watch?v=S5CjKEFb-sM",
	"Benedict Cumberbatch, Keira Knightley",
	"25th December 2014")

guardians_of_the_galaxy = media.Movie("Guardians of The Galaxy", 
	"A Marvel movie involving space adventures",
	"http://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg", 
	"www.youtube.com/watch?v=B16Bo47KS2g",
	"Chris Pratt, Zoe Saldana",
	"1st August 2014")

transformers = media.Movie("Transformers: Age of Extinction", 
	"A war of good versus evil",
	"http://ia.media-imdb.com/images/M/MV5BMjEwNTg1MTA5Nl5BMl5BanBnXkFtZTgwOTg2OTM4MTE@._V1_SX640_SY720_.jpg", 
	"www.youtube.com/watch?v=S30VkLn5a2o",
	"Mark Wahlberg, Stanley Tucci",
	"27 June 2014")

ironman = media.Movie("Ironman", 
	"A Marvel Superhero film",
	"http://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG", 
	"www.youtube.com/watch?v=8hYlB38asDY",
	"Robert Downey Jr., Terrence Howard",
	"2 May 2008")

#Array of all movies
movies = [the_imitation_game, guardians_of_the_galaxy, transformers, ironman]

#Function call to Open the Movies page using the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)