from gtts import gTTS
import kawaii_voice_gtts
import pydub
from pydub.playback import play
from playsound import playsound

file_name = 'voice.mp3'
txt = 'お兄ちゃん、すごいね！'

gTTS(txt, lang='ja').save(file_name)
imouto = kawaii_voice_gtts.kawaii_voice(file_name)
result = imouto.pitch(0.45)
# result = imouto.speed(1.3)
result.audio.export('voice_.mp3', 'mp3')

playsound('voice_.mp3')
