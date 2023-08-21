                              # CLASS SERIES ( CHILD CLASS )

from media import Media

class Series ( Media ) :

    def __init__ ( self , type , name , director , imbd , url , duration , casts , episode , gener ) :
        super().__init__ ( type , name , director , imbd , url , duration , casts )
        self.episode = episode
        self.gener = gener