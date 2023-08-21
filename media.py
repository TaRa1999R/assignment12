                              # MEDIA CLASS ( PARENT CLASS )
import pytube

class Media :

    def __init__ ( self , type , name , director , imbd , url , duration , casts ) :
        self.type = type
        self.name = name
        self.director = director
        self.IMBD_score = imbd
        self.url = url
        self.duration = duration 
        self.casts = casts

    def showInfo ( self ) :
        if self.type == "film" or self.type == "clip" :
            print ( self.type + " , " + self.name + " , " + self.director + " , " + self.IMBD_score + " , " + self.duration + " , " + self.casts + " , " + self.gener )

        elif self.type == "series" :
            print ( self.type + " , " + self.name + " , " + self.director + " , " + self.IMBD_score + " , " + self.duration + " , " + self.casts + " , " + self.episode + " , " + self.gener )

        elif self.type == "documentary" :
            print ( self.type + " , " + self.name + " , " + self.director + " , " + self.IMBD_score + " , " + self.duration + " , " + self.casts )

    def download ( self ) :
        link = self.url
        first_stream = pytube.YouTube( link ).streams.first()
        first_stream.download ( "F:/Python Projects/assignment12" , self.name )

