from gtts import gTTS
import kawaii_voice_gtts
from playsound import playsound

file_name = 'voice.mp3'
txt = 'お兄ちゃん、すごいね！'

gTTS(txt, lang='ja').save(file_name)
imouto = kawaii_voice_gtts.kawaii_voice(file_name)
# imouto = imouto.formant(1.1, 1.5)
# imouto = imouto.speed(2.0)
imouto = imouto.pitch(1.0)
imouto.audio.export('voice_.mp3', 'mp3')

playsound('voice_.mp3')
