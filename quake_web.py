## quake_web.py   
## Template file provided by Brandon Bennett.

## You can run this file as it is and it will run some tests that
## will give you anidea of the functionality that you need to implement.
## Once you have coded the functions 'display_quake_record' and
## 'display_todays_largest_magnitude_quake you will get the full
## funcitonality.
## But note that you need to be connected to the internet for the
## function defined in Part 2 to work.

## Don't change or add to these module import commands.
## You do not need any other modules to do this coursework.
import urllib.request    # used to get data from the web
import os                # used for getting saved filenames
import csv               # used for reading a csv

## Part 1
def display_quake_record( quake_record ):
    ## Replace the following lines with code to print out the
    ## quake record nicely.
    print( "!! Sorry, the 'display_quake_record' function has not been" )
    print( "   coded yet :(" )
    print( "   Just printing the raw quake record instead:" )
    print( quake_record )

## Part 2  
def display_todays_largest_magnitude_quake():
    ## Replace the following lines with code to print out the
    ## display today's largest magnitude earthquake.
    print( "!! Sorry, the display_todays_largest_magnitude_quake function" )
    print( "   has not been coded yet :(" )
    print( "   You need to write code that will download the quake datalist,")
    print( "   find the record with the largest magnitude, and display it" )
    print( "   using the display_quake_record function you just defined." )


########################################################################
# Read the rest of this file carefully.
# But DO NOT CHANGE it.
# It proveds a useful function, some example data and some tests.

## You should definitely make use of this function!
## Give it the URL of a csv file that is available on the internet.
## It will return a datalist of the contents of that file.
def get_datalist_from_csv_url( url ):
    url_response = urllib.request.urlopen(url)
    url_data = url_response.readlines()
    url_data = [line.decode('utf-8') for line in url_data]
    reader = csv.reader(url_data)
    datalist = list(reader)
    return datalist

## Here is the URL of the earthquake data CSV file provided by USGS.
## The data is updated daily. 
USGS_QUAKE_DATA_URL = ( 'http://earthquake.usgs.gov/earthquakes/feed/' +
                        'v1.0/summary/all_day.csv' )

## So you can see some basic functionality, I am initialising this 
## "global variable" EXAMPLE_QUAKE_DATA to a list containing the first few
## rows taken from a CSV file I have previsously downloaded from USGS.
EXAMPLE_QUAKE_DATA = [
    ['time', 'latitude', 'longitude', 'depth', 'mag', 'magType',
   'nst', 'gap', 'dmin', 'rms', 'net', 'id','updated', 'place', 'type', 
   'horizontalError', 'depthError', 'magError', 'magNst', 'status',
    'locationSource', 'magSource'],
    ['2017-11-16T18:42:11.676Z', '61.7647', '-153.9615', '0.8', '2.1', 'ml', 
     '', '', '', '0.64', 'ak', 'ak17253456', 
     '2017-11-16T18:58:24.707Z', '156km NNW of Redoubt Volcano, Alaska', 'earthquake', 
     '', '0.2', '', '', 'automatic', 'ak', 'ak'],
    ['2017-11-16T18:35:00.940Z', '34.1638333', '-116.4253333', '10.17', '1.76', 'ml', 
     '58', '33', '0.03663', '0.17', 'ci', 'ci37812975', 
     '2017-11-16T19:14:13.440Z', '6km N of Yucca Valley, CA', 'earthquake', 
     '0.14', '0.32', '0.18', '50', 'reviewed', 'ci', 'ci']
         ]

## This function tests the three functions of the program (including the
## one I have provided to check it is working).
## I have used "try" and "except" to ensure that run_tests does not fail
## even if one of the tests gives an error.
def run_tests():
    print( "** TEST 1: Testing 'display_quake_record'" )
    print( "** Running 'display_quake_record' on an example quake record:" )
    try:
       display_quake_record( EXAMPLE_QUAKE_DATA[1] )
    except BaseException as e:
       print( "!! Something went wrong !!" )
       print( "   Exception generated was:\n    ", repr(e) )
       
    print( "\n** TEST 2: Testing quake data download (Provided by BB)")
    print( "** Running 'get_datalist_from_csv_url' on USGS_QUAKE_DATA_URL.")
    print( "** Getting latest quake data from USGS ..." )
    try:
       latest_quake_data = get_datalist_from_csv_url( USGS_QUAKE_DATA_URL )
       print( "** Quake data downloaded." )
       print( "** Running display_quake_record on first downloaded record:" )
       display_quake_record( latest_quake_data[1] )
    except BaseException as e:
       print( "!! Something went wrong !!" )
       print( "   Exception generated was:\n    ", repr(e) )
    #--------------------------------------------------------
    print( "\n** TEST 3: Testing 'display_todays_largest_magnitude_quake'" )
    print( "** Running 'display_todays_largest_magnitude_quake()' ..." )
    try:
       display_todays_largest_magnitude_quake()
    except BaseException as e:
       print( "!! Something went wrong !!" )
       print( "   Exception generated was:\n    ", repr(e) )
       
    print( "\n======= TESTING COMPLETED ========" )


run_tests()



