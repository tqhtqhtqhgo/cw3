
## Import module for handling csv files.
import csv
## You are not allowed to import any other module into this file.

## display_playlist( filename )
## Replace the following dummy function with one that reads the playlist
## from the csv file corresponding to the filename argument and prints
## out the playlist in the format shown in the coursework specification
## document.
##
## Note: Check whether the filename argument ends in ".csv". If it doesn't
## then you should add ".csv" to get the actual name of the CSV file that
## will be opened.

def display_playlist( filename ):
    song_name=[]
    artists=[]
    album=[]
    time=[]
    max1 = 0
    max2 = 0
    max3 = 0
    try:
        data=get_datalist_from_csv(filename)
        for row in data:
            song_name.append(row[0])
            artists.append(row[1])
            album.append(row[2])
            time.append(row[3])
        len1=len(song_name)
        for i in song_name:
            if len(i)>max1:
                max1=len(i)
        for i in artists:
            if len(i)>max2:
                max2=len(i)
        for i in album:
            if len(i)>max3:
                max3=len(i)
        for i in range(len1):
            if (i==0):
                print(len(pad_to_length(song_name[i],max1))*'-'+len(pad_to_length(artists[i],max2))*'-'+len(pad_to_length(album[i],max3))*'-'+len(pad_to_length(time[i],6))*'-'+5*'-')
                print('\033[1;33;44m|'+pad_to_length(song_name[i],max1)+'|'+pad_to_length(artists[i],max2)+'|'+pad_to_length(album[i],max3)+'|'+pad_to_length(time[i],6)+'|\033[0m')
                print(len(pad_to_length(song_name[i],max1))*'-'+len(pad_to_length(artists[i],max2))*'-'+len(pad_to_length(album[i],max3))*'-'+len(pad_to_length(time[i],6))*'-'+5*'-')
            elif(i==len1-1):
                print('|' + pad_to_length(song_name[i], max1 ) + '|' + pad_to_length(artists[i],max2 ) + '|' + pad_to_length(album[i], max3 ) + '|' + pad_to_length(time[i], 6) + '|')
                print(len(pad_to_length(song_name[i], max1)) * '-' + len(
                    pad_to_length(artists[i], max2 )) * '-' + len(pad_to_length(album[i], max3 )) * '-' + len(
                    pad_to_length(time[i], 6)) * '-' + 5 * '-')

            else:
                print('|'+pad_to_length(song_name[i],max1)+'|'+pad_to_length(artists[i],max2)+'|'+pad_to_length(album[i],max3)+'|'+pad_to_length(time[i],6)+'|')

    except:
        filename=filename+'.csv'
        data = get_datalist_from_csv(filename)
        for row in data:
            song_name.append(row[0])
            artists.append(row[1])
            album.append(row[2])
            time.append(row[3])
        len1 = len(song_name)
        for i in song_name:
            if len(i) > max1:
                max1 = len(i)
        for i in artists:
            if len(i) > max2:
                max2 = len(i)
        for i in album:
            if len(i) > max3:
                max3 = len(i)
        for i in range(len1):
            if (i == 0):
                print(len(pad_to_length(song_name[i], max1)) * '-' + len(pad_to_length(artists[i], max2)) * '-' + len(
                    pad_to_length(album[i], max3)) * '-' + len(pad_to_length(time[i], 6)) * '-' + 5 * '-')
                print('\033[1;33;44m|' + pad_to_length(song_name[i], max1) + '|' + pad_to_length(artists[i],
                                                                                                 max2) + '|' + pad_to_length(
                    album[i], max3) + '|' + pad_to_length(time[i], 6) + '|\033[0m')
                print(len(pad_to_length(song_name[i], max1)) * '-' + len(pad_to_length(artists[i], max2)) * '-' + len(
                    pad_to_length(album[i], max3)) * '-' + len(pad_to_length(time[i], 6)) * '-' + 5 * '-')
            elif (i == len1 - 1):
                print('|' + pad_to_length(song_name[i], max1) + '|' + pad_to_length(artists[i],
                                                                                    max2) + '|' + pad_to_length(
                    album[i], max3) + '|' + pad_to_length(time[i], 6) + '|')
                print(len(pad_to_length(song_name[i], max1)) * '-' + len(
                    pad_to_length(artists[i], max2)) * '-' + len(pad_to_length(album[i], max3)) * '-' + len(
                    pad_to_length(time[i], 6)) * '-' + 5 * '-')

            else:
                print('|' + pad_to_length(song_name[i], max1) + '|' + pad_to_length(artists[i],
                                                                                    max2) + '|' + pad_to_length(
                    album[i], max3) + '|' + pad_to_length(time[i], 6) + '|')
    print( '\n Running  display_playlist( "{}" )'.format(filename) )



## You can use the following function to read data from a csv format file
def get_datalist_from_csv( filename ):
    ## Create a 'file object' f, for accessing the file: 
    with open( filename ) as f:
         reader = csv.reader(f)     # create a 'csv reader' from the file object
         datalist = list( reader )  # create a list from the reader 
    return datalist


## The following function may be useful for aligning your table columns
## It adds spaces to the end of a string to make it up to length n.
def pad_to_length( string, n):
    return string + " "* (n-len(string)) ## s*n gives empty string for n<1 

## Run the display_playlist function on the example files
## (The ".csv" should get added by display_playlist)
## display_playlist( "geek-music.csv" )
## display_playlist( "snake-music")

