from gtts import gTTS
import kawaii_voice_gtts
import pydub
from pydub.playback import play
from playsound import playsound

file_name = 'music.mp3'

imouto = kawaii_voice_gtts.kawaii_voice(file_name)
imouto = imouto.music_pack1()
imouto.audio.export('music_.mp3', 'mp3')

playsound('music_.mp3')
