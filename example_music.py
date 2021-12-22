# Sample of converting music to nightcore

import kawaii_voice_gtts
from playsound import playsound

file_name = 'music.mp3'

# ----- music synthesis
imouto = kawaii_voice_gtts.kawaii_voice(file_name)
imouto = imouto.music_pack1()
imouto.audio.export('music_.mp3', 'mp3')

# playsound('music_.mp3')
