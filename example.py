from gtts import gTTS
import kawaii_voice_gtts
from playsound import playsound

file_name = 'voice.mp3'
txt = 'お兄ちゃん、すごいね！'

gTTS(txt, lang='ja').save(file_name)
imouto = kawaii_voice_gtts.kawaii_voice(file_name)
imouto = imouto.speed(0.25)
imouto = imouto.pitch(2.7)
imouto.audio.export('voice_.mp3', 'mp3')

playsound('voice_.mp3')
