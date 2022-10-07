from gtts import gTTS
from playsound import playsound
audio = 'try.mp3'
language = 'en'
text = gTTS(text = "Hello", lang = language, slow= False)
text.save(audio)
playsound(audio)