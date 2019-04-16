import webbrowser
class Movie():
    def __init__(self, movie_title, movie_image, movie_trailer, movie_rating, movie_storyline):
        self.title = movie_title
        self.poster_image = movie_image
        self.youtube_trailer_url = movie_trailer
        self.imdb_rating_url = movie_rating
        self.storyline = movie_storyline

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)
