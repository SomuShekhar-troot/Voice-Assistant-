import speech_recognition as sr
import webbrowser
sr.Microphone(device_index=1) ##to get device microphone
voice=sr.Recognizer()  ## Recognizer function is used to recognise the words we speak
voice.energy_threshold=5000 ##it is to set the voice frequency to recognise the words we say
with sr.Microphone() as source: ##with is keyword used becozs when we want to use other sources we use with here we using microphone
    print("Say Something Buddy I'm Here For You")
    audio=voice.listen(source) ##here we are taking the source data from microphone to listen the voice and storing it in voice variable
    try:
        text=voice.recognize_google(audio) ##here we convert the audio into text that acn be recognised by the google
        print("you want : ()".format(text))
        url='https://www.google.com/search?q=' ##this basic common url to search
        search_url=url+text ##here we seaching the url in google with the thing we want to search for
        webbrowser.open(search_url) ## asking browser to open to search what is requested
    except:
            print(" Can't hear you buddy")
        
    
