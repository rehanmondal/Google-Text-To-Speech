# This is a very simple text to speech program

from gtts import gTTS

class Sound:
    def sound(self,text,filename):
        my_audio = gTTS(text)
        my_audio.save(f"{filename}.mp3")

sd = Sound()

sd.sound("Insert You Card","insert")
sd.sound("Please Do Not Remove Your Card","waiting1")
sd.sound("Please wait while your transaction is being processed","waiting2")
sd.sound("Thank You For banking","thankyou")

# Sampling Rate also controlled to change playback speed