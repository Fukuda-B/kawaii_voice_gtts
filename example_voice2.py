# pyttsx3 Ver.

import os
import pyttsx3
import kawaii_voice_gtts
from playsound import playsound

file_name = os.path.join(os.getcwd(), "voice.mp3")
file_name_e = 'voice_.mp3'
file_format = 'mp3'
txt = 'こんにちは、BBBotのv_boice 日本語の声をkawaii_voice_gttsを通して出力しました。'
# txt = 'こんばんは。 今夜は月が綺麗だね。'

# ----- create a voice source
engine = pyttsx3.init()
engine.save_to_file(txt, file_name)
engine.runAndWait()

# ----- voice synthesis
imouto = kawaii_voice_gtts.kawaii_voice(file_name)
imouto = imouto.formant(1.2, 1.7)
# imouto = imouto.speed(1.05)
# imouto = imouto.pitch(0.4)
# imouto = imouto.voice_pack2()
imouto.audio.export(file_name_e, file_format)

# ----- playback
playsound(file_name_e)
