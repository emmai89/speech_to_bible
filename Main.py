from Voice import audioToText
from FileIO import readBible
from Passage import passageFinder
bible = readBible("ESV")

#passage = audioToText()
passage = "first John 1 verses 2 to 5"
print (passage)
print(passageFinder(bible, passage))
