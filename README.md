# kawaii_voice_gtts  
Audio Conversion Extension Module  
For the general public, please refer to [README_normal.md](./README_normal.md).  
  
![top_illust_11](https://user-images.githubusercontent.com/60131202/118388452-884f9f80-b65f-11eb-90b4-4fea4db32db3.png)
---
## Usage  
Apply basic voice pack1.
```
imouto = Kawaii_voice('voice.mp3')  
result = imouto.voice_pack1()
```
Apply pitch change.
```
imouto = Kawaii_voice('voice.mp3')  
result = imouto.pitch(2.0)
```  
　  
Note: Audio data is passed as pydub.AudioSegment.  
AudioSegment. You can also convert it with numpy as follows  
```
np_array = numpy.array(imouto.audio.get_array_of_samples())
```


![sub_illust_3](https://user-images.githubusercontent.com/60131202/118389684-eb443500-b665-11eb-8907-7b9e3cf60e14.png)
---
## Function
| function | outline |
--- | ---
| formant (value) \[unimplemented\] | The higher the value, the closer it is to a woman's voice. |
| speed (value) | Change play speed. |
| pitch (value) | Change audio pitch. |
| valume (value) | Change audio volume. |
| bass_boost () \[unimplemented\] | Bass boost using a low-pass filter. |
| normalize () | Normalize audio data. |
|||
| voice_pack1 () \[unimplemented\] | Audio conversion tuned for gTTS(ja) |
| music_pack1 () \[unimplemented\] | Nightcore conversion. |

---
### Future  
It's still just a basic voice converter, but I'm hoping to add advanced voice quality conversion as well.  
　  
最後まで読んでくれてありがとう お兄ちゃん！
