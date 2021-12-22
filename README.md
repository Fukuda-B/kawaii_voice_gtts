# kawaii_voice_gtts  
Audio Conversion Extension Module  
For the general public, please refer to [README_normal.md](./README_normal.md).  
  
![top_illust_11](./illust/top_illust_12.png)
---
## Usage  
Apply basic voice pack1.
```
imouto = kawaii_voice('voice.mp3')  
result = imouto.voice_pack2()
```
Apply pitch change.
```
imouto = kawaii_voice('voice.mp3')  
result = imouto.pitch(2.0)
```  
　  
Note: Audio data is passed as pydub.AudioSegment.  
AudioSegment. You can also convert it with numpy as follows  
```
np_array = numpy.array(imouto.audio.get_array_of_samples())
```


![sub_illust_3](./illust/sub_illust_3.png)
---
## Function
| function | outline |
--- | ---
| formant (value、f0_rate) | The higher the value, the closer it is to a woman's voice. |
| speed (value) | Change play speed. |
| pitch (value) | Change audio pitch. |
| volume (value) | Change audio volume. |
| bass_boost (option) | Bass boost using a low-pass filter. |
| normalize (option) | Normalize audio data. |
|||
| voice_pack1 () | Audio conversion (old ver.) |
| voice_pack2 () | Audio conversion tuned for gTTS(ja) |
| music_pack1 () | Nightcore conversion. |

## Sample  
| Voice source | option | source | result |
| ----- | ----- | ----- | ----- |
| gTTS | voice_pack2 | [voice_gtts.mp3](./sample/voice_gtts.mp3) | [voice_gtts_pack2.mp3](./sample/voice_gtts_pack2.mp3) |
| pyttsx3 | formant(1.2, 1.7) | [voice_pyttsx3.mp3](./sample/voice_pyttsx3.mp3) | [voice_pyttsx3_formant.mp3](./sample/voice_pyttsx3_formant.mp3) |
  
| Sample code | |
| ----- | ----- |
| [example_voice.py](./example_voice.py)| gTTS ver. |
| [example_voice2.py](./example_voice2.py) | pyttsx3 ver. | 
| [example_music.py](./example_music.py) | convert song to Nightcore. |

---
### Future  
It's still just a basic voice converter, but I'm hoping to add advanced voice quality conversion as well.  
　  
README紳士向け版を最後まで読んでくれるなんてやさしいね！  ありがとう お兄ちゃん！
