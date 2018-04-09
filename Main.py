from Voice import audioToText
from FileIO import readBible
from Passage import passageFinder
bible = readBible("ESV")

passage = audioToText()
print (passage)
print(passageFinder(bible, passage))
