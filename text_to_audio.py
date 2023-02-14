
from gtts import gTTS # google text to speech convertor. 

import os # to access the folder need this package


mytext = 'Text to audio convertor' # user defined text which is converted into the audio

language = 'en' # in which language it is going to be converted. 


myobj = gTTS(text=mytext, lang=language, slow=False) # false is made in order to convert the audio to text at faster rate

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("audio.mp3")#save the audio file

# Playing the converted file
os.system("audio.mp3")#play the audio file
