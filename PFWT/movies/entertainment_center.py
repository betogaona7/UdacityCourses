
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that come to life",
	"https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=cRdxXPV9GNQ")

my_name_is_khan = media.Movie("My name is Khan",
	"A man with special challenges",
	"https://en.wikipedia.org/wiki/File:My_Name_Is_Khan_film_poster.jpg",
	"https://www.youtube.com/watch?v=XAtPpjEZwC8")

school_of_rock = media.Movie("School of Rock",
	"Storyline",
	"https://en.wikipedia.org/wiki/File:School_of_Rock_Poster.jpg",
	"https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
	"Storyline",
	"https://en.wikipedia.org/wiki/File:RatatouillePoster.jpg",
	"https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in paris",
	"Storyline",
	"https://en.wikipedia.org/wiki/File:Midnight_in_Paris_Poster.jpg",
	"https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
	"Storyline",
	"https://en.wikipedia.org/wiki/File:HungerGamesPoster.jpg",
	"https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story,avatar,my_name_is_khan,school_of_rock,ratatouille,midnight_in_paris,hunger_games]

fresh_tomatoes.open_movies_page(movies)
