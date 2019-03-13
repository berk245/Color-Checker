import csv

user_color = '18th Century Green'
splitted_color = user_color.split()
match_found = False

with open("./scripts/colornames.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    for row in csv_reader:
        if splitted_color[0] == "#":
            if user_color == row[1]:
                try:
                    print("""<html>
                    <body>
                    <p> Yes,that code is a color and it's name is %s
                    </p>
                    </body>
                    </html>
                    """%row[0])
                    match_found = True
                except:
                    pass            
        else:
            try:
                if user_color.lower() == row[0].lower():
                    print("""<html>
                    <body>
                    <p> Yes, that's a color and it's hex code is %s
                    </p>
                    </body>
                    </html>
                    """ %row[1])
                    match_found = True
            except:
                pass        
    if not match_found:    
        print("""<html>
                <body>
                <p> This is not a valid color name or a code
                </p>
                </body>
                </html>
                """)            