import speech_recognition as sr

def audioToText():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    print("checking.....")

        # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language='en-AUS')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return text
