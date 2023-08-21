                              # MEDIA MANAGMENT APPLICATION

#---------------------------------------------------------------- import classes
from media import Media
from series import Series
from film import Film
from documentary import Documentary
from clip import Clip
from actors import Actor

#---------------------------------------------------------------- Database class
OBJECTS = []
ACTORS = []

class Database :

    def read ( self ) :
        f = open ( "database.txt" , "r" )
        for line in f :
            text = line.split("\n")
            obj = text[0]
            result = obj.split (",")
            if result[0] == "film" :
                my_object = Film ( result[0] , result[1] , result[2] , result[3] , result[4] , result[5] , result[6] , result[7] )
            
            elif result[0] == "series" :
                my_object = Series ( result[0] , result[1] , result[2] , result[3] , result[4] , result[5] , result[6] , result[7] , result[8] )

            elif result[0] == "documentary" :
                my_object = Documentary ( result[0] , result[1] , result[2] , result[3] , result[4] , result[5] , result[6] )

            elif result[0] == "clip" :
                my_object = Clip ( result[0] , result[1] , result[2] , result[3] , result[4] , result[5] , result[6] , result[7] )

            OBJECTS.append ( my_object )
        f.close ()

    def write ( self ) :
        f = open ( "database.txt" , "w" )
        for obj in OBJECTS :
            if obj.type == "series" :
                text = obj.type + "," + obj.name + "," + obj.director + "," + obj.IMBD_score + "," + obj.url + "," + obj.duration + "," + obj.casts + "," + obj.episode + "," + obj.gener + "\n"           
                print ("done series")
                f.write ( text )

            elif obj.type == "documentary" :
                text = obj.type + "," + obj.name + "," + obj.director + "," + obj.IMBD_score + "," + obj.url + "," + obj.duration + "," + obj.casts + "\n"
                print ("done documentary")
                f.write ( text )

            else :
                text = obj.type + "," + obj.name + "," + obj.director + "," + obj.IMBD_score + "," + obj.url + "," + obj.duration + "," + obj.casts + "," + obj.gener + "\n"
                print ("done film-clip")
                f.write ( text )

        f.close ()

#---------------------------------------------------------------- class stor
class Stor :
    @staticmethod
    def show_menue () :
        print ()
        print (" Enter 1 to Add new media ")
        print (" Enter 2 to Edit a media ")
        print (" Enter 3 to Remove a media ")
        print (" Enter 4 to Search for a media ")
        print (" Enter 5 to Find a media with specific length ")
        print (" Enter 6 to Show the list of media ")
        print (" Enter 7 to Show the information of a media ")
        print (" Enter 8 to download a media ")
        print (" Enter 9 to see the list of actors ")
        print (" Enter 10 to Exit the application ")
        print ()

    @staticmethod
    def add () :
        type = input (" Please enter type of media you want to add ( choose between series , film , documentary , clip) : ")
        if type == "series" or type == "film" or type == "clip" or type == "documentary" :
            name = input (" Please enter the name : ")
            director = input (" Please enter the director : ")
            imbd = input (" Please enter IMBD score : ")
            url = input (" Please enter the URL : ")
            duration = input (" Pleae enter the duration : ")
            casts = input (" Please enter the actors ( split them with '-') : ")
            if type == "series" :
                episod = input (" Please enter the number of episods : ")
                gener = input (" Please enter the gener : ")
                obj = Series ( type , name , director , imbd , url , duration , casts , episod , gener )
                OBJECTS.append ( obj )
            
            elif type == "documentary" :
                obj = Documentary ( type , name , director , imbd , url , duration , casts )
                OBJECTS.append ( obj )
            
            elif type == "film" or type == "clip" :
                gener = input (" Please enter the gener : ")
                obj = Film ( type , name , director , imbd , url , duration , casts , gener )
                OBJECTS.append ( obj )
            
            print (" done ")

        else :
            print (" ❌❌ Wrong type of input ❌❌ ")
        

    @staticmethod
    def edit () :
        obj = Stor.search ()
        if obj != " No " :
            print (" Rember that documentary doesn't have episode and gener , also film and clip don't have gener 😊")
            user_chang = input (" Which part of this media you want to change ? ( name , director , IMBD_score , url , duration , casts , gener , episode ) : ")
            if user_chang == "name" :
                obj.name = input (" Please enter new information : ")
                print (" done ")

            elif user_chang == "director" :
                obj.director = input (" Please enter new information : ")
                print (" done ")

            elif user_chang == "IMBD_score" :
                obj.IMBD_score = input (" Please enter new information : ")
                print (" done ")

            elif user_chang == "url" :
                obj.url = input (" Please enter new information : ")
                print (" done ")

            elif user_chang == "duration" :
                obj.duration = input (" Please enter new information : ")
                print (" done ")

            elif user_chang == "casts" :
                obj.casts = input (" Please enter new information : ")
                print (" done ")

            elif user_chang == "gener" :
                if obj.type == "documentary" :
                    print (" ❌❌ Wrong input ❌❌ ")
                    print (" Documentaries don't have gener")
                else :
                    obj.gener = input (" Please enter new information : ")
                    print (" done ")

            elif user_chang == "episode" :
                if obj.type == "series" :
                    obj.episode = input (" Please enter new information : ")
                    print (" done ")
                
                else :
                    print (" ❌❌ Wrong input ❌❌ ")
                    print (" only series have episode ")

            else :
                print (" ❌❌ Wrong input ❌❌ ")


    @staticmethod
    def remove () :
        obj = Stor.search ()
        if obj != " No " :
            OBJECTS.remove ( obj )
            print (" done ")
        

    @staticmethod
    def search () :
        user_input = input (" Please enter the name of media you are looking for : ")
        for obj in OBJECTS :
            if obj.name == user_input :
                print (" The media found ✅✅ ")
                return obj
        
        else :
            print (" Sorry😞 This media doesn't exist in this app ")
            return (" No ")
        

    @staticmethod
    def advanced_search () :
        low = int ( input (" Please enter the lower range of duration : "))
        high = int ( input (" Please enter the higher range of duration : "))
        for obj in OBJECTS :
            lengh = int ( obj.duration )
            if low <= lengh <= high :
                print ( obj.name + " , " + obj.duration + " min" )

    
    @staticmethod
    def media_list () :
        for obj in OBJECTS :
            print ( obj.type + " , " + obj.name + " , " + obj.casts )


    @staticmethod
    def show_information () :
        obj = Stor.search ()
        if obj != " No " :
            obj.showInfo ()


    @staticmethod
    def download () :
        obj = Stor.search ()
        if obj != " No " :
            obj.download ()
    
    
    @staticmethod
    def actors () :
        obj = Stor.search ()
        if obj != " No " :
            result = obj.casts.split ( "-" )
            
        for x in result :
            person = Actor ( x )
            ACTORS.append ( person )
        
        for x in ACTORS :
            print ( x.name )
            

# #---------------------------------------------------------------- main part
print (" Hello😊! Welcom to my Application.")
print (" Please waite✋! Loading... ")
data = Database ()
data.read ()
print (" Data loaded👍 Thaks for your patient ")


while True :
    Stor.show_menue ()
    user_choice = input (" Please enter your choice : ")
    if user_choice == "1" :
        Stor.add ()
    
    elif user_choice == "2" :
        Stor.edit ()
    
    elif user_choice == "3" :
        Stor.remove ()

    elif user_choice == "4" :
        Stor.search ()

    elif user_choice == "5" :
        Stor.advanced_search ()

    elif user_choice == "6" :
        Stor.media_list ()

    elif user_choice == "7" :
        Stor.show_information ()
    
    elif user_choice == "8" :
        Stor.download ()

    elif user_choice == "9" :
        Stor.actors ()
    
    elif user_choice == "10" :
        data.write ()
        exit (0)
    
    else :
        print (" ❌❌ Your entered input is wrong ... ❌❌ ")
        print (" Please enter right inputs ... 🧐 ")