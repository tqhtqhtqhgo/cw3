import csv
## Do not import any other modules.
## The csv module is all you need.


def make_html_playlist( playlist ):

    playl=playlist.split('.')[0]
    print("** Running make_html_table_file")
    print("** Creating file:", playlist)
    data=get_datalist_from_csv(playlist)
    track=[]
    artist=[]
    album=[]
    time=[]
    for i in data:
        track.append(i[0])
        artist.append(i[1])
        album.append(i[2])
        time.append(i[3])
    heading=playl
    with open(playl+'.html','w') as html_file:
        html_file.write('<html>\n')
        html_file.write('<style>table, th{border: 2px solid black;background-color: #CCCCFF;border-color:  #8888FF;font-family:calibri;}</style>')
        html_file.write('<title>' + heading.upper() + '</title>\n')
        html_file.write('<body bgcolor=#DDFFF8 background="1.jpg">\n')
        html_file.write('<center>\n')
        html_file.write('<H1>' +"Web play"+ '</H1>\n')
        html_file.write("<table border=2 cellpadding=10>\n")
        html_file.write("<tr><td colspan=\"4\" align=\"center\"><b>"+"Play list: "+playl.upper()+"</b></td><tr>\n\n")
        html_table = make_html_table_from_datalist(data)
        html_file.write(html_table)
        html_file.write('</center>\n')
        html_file.write('</body>\n')
        html_file.write('</html>\n')

    # Here you should write your actual code that creates
    # an HTML file to display the playlist details stored
    # in the CSV file referred to by the playlist argument.
    

def get_datalist_from_csv( filename ):
    ## Create a 'file object' f, for accessing the file:
    try:
        with open( filename ) as f:
             reader = csv.reader(f)     # create a 'csv reader' from the file object
             datalist = list( reader )  # create a list from the reader
    except:
        filename+=".csv"
        with open( filename ) as f:
             reader = csv.reader(f)
             datalist = list( reader )
    return datalist

def make_html_table_from_datalist( datalist ):
    ## We just keep adding the html we want to the html_string variable
    html_string = ""
    ## loop over all the records in the datalist
    len1=len(datalist)
    sec=0

    for i in range(len1):
        record=datalist[i]
        if i==0:
            html_string += "<tr>\n"
            for datum in record:
                ## put each piece of data into a html table data element
                html_string += "<td ><b>" + str(datum) + "</b></td>\n"
            html_string += "<tr>\n\n"
        else:
            len2=len(record)
            html_string += "<tr>\n"

            for i in range(len2):
                datum=record[i]
                if i==0:
                ## put each piece of data into a html table data element
                    html_string += "<td style=\"background-color: #ffff;\"><b>" + youtube_query_link(str(datum), str(datum)) + "</b></td>\n"
                elif i==1:
                    html_string += "<td style=\"background-color: #fffa;\"><b>"+wiki(str(datum),str(datum))+"</b></td>\n"

                elif i==2:
                    html_string += "<td style=\"background-color: #fff8;\">" + str(datum) + "</td>\n"
                elif i==3:
                    a=str(datum).split(':')
                    sec+=int(a[0])*60+int(a[1])
                    html_string += "<td>" + str(datum) + "</td>\n"
            html_string += "<tr>\n\n"
    sec1 = sec%60
    hour = sec//3600
    min = (sec-3600*hour)//60
    html_string += "<tr><td colspan=\"4\" align=\"center\"><b>" + "Total playing time: " + str(hour) + ":" + str(
        min) + ":" + str(sec1) + "</b></td><tr>\n\n"
    ## NOTE: to format each column differently you should remove the
        ## preceeding loop and individually add each item in the record
        ## creating a particular format for that type of data item.
    html_string += "</table>\n\n"
    return html_string

# You can add other functions that can be used by your code
# in make_html_playlist
# For example, you may use the get_datalist_from_csv function
# that was provided for display_playlist
# You may also take and adapt code from the example file
# make_html_table_file.py

## Some tests you should try.
#make_html_playlist( "geek-music.csv" )
#make_html_playlist( "snake-music" )

## Note that the ".csv" extension is optional, make_html_playlist
## should work the same, whether or not it is present.

## Before submitting please delete of comment out any code
## that is outside definined functions (apart from 'import csv').

def youtube_query_link(query_string, text_string):
    wordlist = query_string.split()
    URL = ("https://www.youtube.com/results?search_query=" +
           "+".join(wordlist))  # Add query terms separated by '+'
    # Make string containing the HTML link element
    return ('<a href="' + URL + '">' + text_string + '</a>')

def wiki(query_string, text_string):
    wordlist = query_string.split()
    URL = ("https://en.wikipedia.org/?search=" +
           "_".join(wordlist))  # Add query terms separated by '+'
    # Make string containing the HTML link element
    return ('<a href="' + URL + '">' + text_string + '</a>')

if __name__ == '__main__':
    make_html_playlist('geek-music.csv')