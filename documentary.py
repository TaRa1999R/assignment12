                              # CLASS DOCUMENTARY ( CHILD CLASS )

from media import Media

class Documentary ( Media ) :

    def __init__ ( self , type , name , director , imbd , url , duration , casts ) :
        super().__init__ ( type , name , director , imbd , url , duration , casts )