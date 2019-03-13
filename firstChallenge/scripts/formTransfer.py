import cgi

form = cgi.FieldStorage()

fav_color = form.getvalue('color')

def checkColor(user_color):

    server_favorites= ["green", "yellow"]

    if user_color in server_favorites:
        print("""
        <html>
        <body>
        <p> Oh great, I like %s too.
        </p>
        </body>
        </html>
        """ %user_color)
    else:
        print("""
        <html>
        <body>
        <p> You have a bad taste.
        </p>
        </body>
        </html>
        """)
    
checkColor(fav_color)
