#!/Python37-32

import cgi
import sys
import csv

form = cgi.FieldStorage()

user_color = form.getvalue('usercolor')


with open('colors.csv') as csv_file:
    hex_found = False
    color_found = False
    csv_file_reader = csv.reader(csv_file)
    for row in csv_file_reader:
        if user_color[0] == '#':
            if user_color == row[2]:
                hex_found = True
                break
        else:
            if user_color.upper() == row[1].upper():
                color_found = True
                break

    if color_found:
        print("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Document</title>
            </head>
            <body>
            <p> Color Match Found </p>
            </body>
            </html>""") 
    elif hex_found:
        print("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Document</title>
            </head>
            <body>
            <p> Hex Match Found </p>
            </body>
            </html>""") 
    else:
        print("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Document</title>
            </head>
            <body>
            <p> No Match Found </p>
            </body>
            </html>""")         

    
        