import webbrowser

class Movie():
    def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
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
