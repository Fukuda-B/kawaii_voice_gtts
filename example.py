from gtts import gTTS
import kawaii_voice_gtts
import pydub
from pydub.playback import play

file_name = 'voice.mp3'
gTTS('お兄ちゃん、すごいね！', lang='ja').save(file_name)
imouto = kawaii_voice_gtts.kawaii_voice(file_name)
result = imouto.pitch(1.2)
play(result.audio)
