import webbrowser

class Movie():
<<<<<<< HEAD
    def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
||||||| merged common ancestors
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
=======
    VALID_RATINGS = ("G", "PG", "PG-13", "R')
                     
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
>>>>>>> fdbd46d5598f43418c715240db968001ee8c2a40
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
        
class TV():
    def __init__ (self, tv_title, tv_synopsis, box_art, tv_clip):
        self.title = tv_title
        self.storyline = tv_synopsis
        self.poster_image_url = poster_image
        self.trailer_youtube_url = tv_clip
    
    def show_trailer(self):
        webbrowser.open(self.tv_clip)
