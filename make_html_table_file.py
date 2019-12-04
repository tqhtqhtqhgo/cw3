## make_html_table_file.py

## make_html_table_file( heading, datalist, filename )

## This function makes an html file to display some data.
## Arguments are as follows:
## heading: a string used to make the title and heading of the html page. 
## datalist: a list of data records, with eachrecord being a list of data items.
## filename: a string giving the name of the html file

## Result: will create HTML file with name filename, and the givein title/heading.
## The file will also contain the data from datalist, formatted as a table.

def make_html_table_file( heading, datalist, filename ):
      print( "** Running make_html_table_file")
      print( "** Creating file:", filename) 
      with open(filename, 'w') as html_file:
          html_file.write('<html>\n')
          html_file.write('<title>' + heading + '</title>\n')
          html_file.write('<center>\n')
          html_file.write('<H1>' + heading + '</H1>\n')
          html_table = make_html_table_from_datalist( datalist )
          html_file.write( html_table )
          html_file.write('</center>\n')
          html_file.write('</html>\n')
      print("**", filename, "has been created :)" )
      print("** Try opening it in a web browser.\n" )


def make_html_table_from_datalist( datalist ):
    ## We just keep adding the html we want to the html_string variable
    html_string = "<table border=2 cellpadding=10>\n" 
    ## loop over all the records in the datalist
    for record in datalist:
        html_string += "<tr>\n" 
        for datum in record:
            ## put each piece of data into a html table data element
            html_string += "<td>" + str(datum) + "</td>\n"
        html_string += "<tr>\n\n"
        ## NOTE: to format each column differently you should remove the
        ## preceeding loop and individually add each item in the record
        ## creating a particular format for that type of data item.
    html_string += "</table>\n\n"
    return html_string

# Here I am creating some example data to fill a table.
# But you could extract this kind of data from a CSV, in the same
# way as you did in part A.

ODD_PEOPLE_DATA = [ 
        [ "TITLE",   "NAME",   "AGE",   "HAIR", "PERSONALITY"],
        [ "Lady",    "May",    69.69,   "grey",   "grim"],
        [ "Lord",    "Boris",  "9+97i", "wild",    "mad"],
        [ "Comrade", "Corbyn", 666,     "besson",  "odd"],
    ]

## Now we can use the example data to create an HTML file.
make_html_table_file( "Odd People", ODD_PEOPLE_DATA, "odd-people.html" )



