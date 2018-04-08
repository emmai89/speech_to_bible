import re
def readBible(fileName):
    f = open(fileName)

    books = {}
    for line in f :
        if line[1] == 'b' :
            currBook = line.split("\"")[1]
            books.update({currBook:"book"})
            books[currBook] = {}
        elif line[1] == 'c' :
            currCp = line.split("\"")[1]
            books[currBook].update({currCp:"cp"})
            books[currBook][currCp] = {}
        elif line[1] == 'v' :
            currVs = line.split("\"")[1]
            verse = re.split('>|<', line)
            books[currBook][currCp].update({currVs:verse[2]})

    return books
