import webbrowser

class Movie() :
    """Movie class with attributes for Movie Name, Poster Image and Trailer Url"""
    def __init__(self,title,poster_image_url,trailer_youtube_url):
        self.title = title
        self.poster_image_url= poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    #def show_trailer (self) :
     #   webbrowser.open(self.trailer_youtube_url)    