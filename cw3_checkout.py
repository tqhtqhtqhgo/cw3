
import os
import zipfile

print("** Running cw3_checkout.py **" )

def report_exception( command, e ):
       print( "!! Something went wrong !!" )
       print( "!! when running '{}'". format( command ) )
       print( "   Exception generated was:\n    ", repr(e) )

def make_cw3_zip():
          print( "* Making CW3 submission file cw3.zip ...\n")
          allfiles = os.listdir()
          remove = ["cw3.zip", "cw3_checkout.py", "__pycache__"]
          files  = [f for f in allfiles if not f in remove]
          #print( files )
          if not "display_playlist.py" in files:
              print( "!!! WARNING: display_playlist.py not found" )
          if not "make_html_playlist.py" in files:
              print( "!!! WARNING: make_html_playlist.py not found" )
          if not "make_html_playlist.py" in files:
              print( "!!! WARNING: quake_web.py not found" )
          with zipfile.ZipFile( 'cw3.zip', mode='w' ) as subzip:
               for f in files:
                   print( "   -- Adding file:", f )
                   subzip.write(f)
          print("\n* Created cw3.zip *")
          print( "* This is the file you should submit via Minerva")


test_music1 = """Track,Artist,Album,Time
Test Me!,Tina Tester,"Life's a Test",3:05
Test Match Special,The Tender Tinder Testers,Best of the Testers,5:32
The Final Test,Eurotest,Test Party 1983,2:50
Check Me Out,Chubby Checker,Check Mate,2:59
A Man Needs Testing,Testosterone,Contest,5:63
"Testing, Testing, Testing, Testing",Purple Milk Quality Assurance,The Long Test,59:59"""

test_music2 = """Track,Artist,Album,Time
Solid Potato Salad,The Ross Sisters,Youtube,3:50
White Rabbit,Jefferson Airplane,Surrealistic Pillow,2:31
Hallogallo,Neu!,Neu!,10:08
You Ain't Seen Nothing Yet,Bachman Turner Overdrive,Not Fragile,3:54
Make Me Smile,Steve Harley and Cockney Rebel,The Best Years of Out Lives,3:52
Fairies Wear Boots,Black Sabbath,Paranoid,6:18
Love Shack,B-52s,Cosmic Thing,5:21
Lost in Music,Sister Sledge,We are Family,4:52
The Stranglers,Hey! (Rise of the Robots),Black and White,2:28
Free Yourself,Chemical Brothers,No Geography,6:31
High-Reel - Ivy Leaf,Joshua Polack,GuitarsOfPikesvile.Com,2:01
Green Groves of Erin,Stuche51,YouTube,1:47
Tom Billy's Jig,De Danann,"Selected Jigs, Reels and Songs",1:28"""


with open("test-music1.csv", "w") as file:
    file.write(test_music1)

with open("test-music2.csv", "w") as file:
    file.write(test_music2)

print("\n=============================================")
print("                   PART A                    ")
print("---------------------------------------------")
    

imported_display_playlist = False
print( "Importing display_playlist ..." )
try:
  import display_playlist
  print("display_playlist imported")
  imported_display_playlist = True
except BaseException as e:
  report_exception("import display_playlist", e)

if imported_display_playlist:
   print( "** Testing display_playlist ..." )
   try:
     print("   Case where input has no extension ('test-music1')")
     display_playlist.display_playlist("test-music1")
   except BaseException as e:
     report_exception('display_playlist("test-music1")', e)
   try:
     print("   Case where input has .csv extension ('test-music2.csv')")
     display_playlist.display_playlist("test-music2.csv")
   except BaseException as e:
     report_exception('display_playlist("test-music2.csv")', e)

print("\n=============================================")
print("                   PART B                    ")
print("---------------------------------------------")
      
imported_make_html_playlist = False
print( "Importing make_html_playlist ..." )
try:
  import make_html_playlist
  print("make_html_playlist imported")
  imported_make_html_playlist = True
except BaseException as e:
  report_exception("import make_html_playlist", e)

if imported_make_html_playlist:
   print( "** Testing make_html_playlist ..." )
   print( "   Will try making playlist for test-music2, with and without .csv extension")
   print( "   Hopefully at least one of them will generate test-music2.html" )
   try:
     print("   Case where input has no extension ('test-music2')")
     make_html_playlist.make_html_playlist("test-music2")
   except BaseException as e:
     report_exception('make_html_playlist("test-music2")', e)
   try:
     print("   Case where input has .csv extension ('test-music2.csv')")
     make_html_playlist.make_html_playlist("test-music2.csv")
   except BaseException as e:
     report_exception('make_html_playlist("test-music2.csv")', e)

if "test-music2.html" in os.listdir():
    print( "\n** HTML file test-music2.html was created :)" )
    print( "** Open test-music2.html in a browser to see what it looks like **")
else:
    print( "!!! WARNING: HTML file test-music2.html was not created :(" )
    

print("\n=============================================")
print("                   PART C                    ")
print("---------------------------------------------")

print( "Importing quake_web ..." )
try:
  import quake_web
  print("* quake_web imported")
except BaseException as e:
  report_exception( "import quake_web", e )

print("\n=============================================\n")

make_cw3_zip()








