def passageFinder(bible, passage):
    text = passage.split(" ")
    output = "dosen't exist"

    if text[0] == "first" :
        output = bible["1 "+text[1]][text[2]][text[4]]
    elif text[0] == "secound" :
        output = bible["2 "+text[1]][text[2]][text[4]]
    elif text[0] == "third" :
        output = bible["3 "+text[1]][text[2]][text[4]]
    elif text[0] == "fourth" :
        output = bible["4 "+text[1]][text[2]][text[4]]
    else :
        output = bible[text[0]][text[1]][text[3]]

    return output
