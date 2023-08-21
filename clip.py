                              # CLASS CLIP ( CHILD CLASS )

from media import Media

class Clip ( Media ) :

    def __init__ ( self , type , name , director , imbd , url , duration , casts , gener ) :
        super().__init__ ( type , name , director , imbd , url , duration , casts )
        self.gener = gener