# gTTS Ver.

from gtts import gTTS
import kawaii_voice_gtts
from playsound import playsound

file_name = 'voice.mp3'
file_name_e = 'voice_.mp3'
file_format = 'mp3'
# txt = 'お兄ちゃん、すごいね！'
# txt = 'こんにちは、BBBotのv_boice 日本語の声をkawaii_voice_gttsを通して出力しました。'
txt = 'こんにちは！ 今日もいい天気だね。'

# ----- create a voice source
gTTS(txt, lang='ja').save(file_name)

# ----- voice synthesis
imouto = kawaii_voice_gtts.kawaii_voice(file_name)
# imouto = imouto.formant(1.2, 1.6)
# imouto = imouto.speed(1.1)
# imouto = imouto.pitch(0.4)
imouto = imouto.voice_pack2()
imouto.audio.export(file_name_e, file_format)

# ----- playback
playsound(file_name_e)
