def passageFinder(bible, passage):
    text = passage.split(" ")
    output = ""

    if text[0] == "first" :
        try:
            if text[5]  == "to" :
                output = verseToVerse(bible, "1 "+text[1], text[2], text[4], text[6])
        except IndexError as e:
                output = verseToVerse(bible, "1 "+text[1], text[2], text[4], text[4])

    elif text[0] == "secound" :
        try:
            if text[5]  == "to" :
                output = verseToVerse(bible, "2 "+text[1], text[2], text[4], text[6])
        except IndexError as e:
                output = verseToVerse(bible, "2 "+text[1], text[2], text[4], text[4])

    elif text[0] == "third" :
        try:
            if text[5]  == "to" :
                output = verseToVerse(bible, "3 "+text[1], text[2], text[4], text[6])
        except IndexError as e:
                output = verseToVerse(bible, "3 "+text[1], text[2], text[4], text[4])

    elif text[0] == "fourth" :
        try:
            if text[5]  == "to" :
                output = verseToVerse(bible, "4 "+text[1], text[2], text[4], text[6])
        except IndexError as e:
                output = verseToVerse(bible, "4 "+text[1], text[2], text[4], text[4])
    else :
        try:
            if text[4]  == "to" :
                output = verseToVerse(bible, text[0], text[1], text[3], text[5])
        except IndexError as e:
                output = verseToVerse(bible, text[0], text[1], text[3], text[3])
    return output

def verseToVerse(bible, book, chapter, verse1, verse2):
    output = ""
    for verse in range((int)(verse1), (int)(verse2)+1) :
        output += str(verse) +". "
        output += bible[book][chapter][str(verse)] +"\n"

    return output
