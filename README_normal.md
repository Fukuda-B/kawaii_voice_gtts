# kawaii_voice_gtts  
Audio Conversion Extension Module  

## Usage  
Apply basic voice pack1.
```
v_data = Kawaii_voice('voice.mp3')  
result = v_data.voice_pack1()
```
Apply pitch change.
```
v_data = Kawaii_voice('voice.mp3')  
result = v_data.pitch(2.0)
```  
　  
Note: Audio data is passed as pydub.AudioSegment.  
AudioSegment. You can also convert it with numpy as follows  
```
np_array = numpy.array(v_data.audio.get_array_of_samples())
```

## Function
| function | outline |
--- | ---
| formant (val) \[unimplemented\] | The higher the value, the closer it is to a woman's voice. |
| speed (val) | Change play speed. |
| pitch (val) | Change audio pitch. |
| valume (val) | Change audio volume. |
| bass_boost () \[unimplemented\] | Bass boost using a low-pass filter. |
| normalize () | Normalize audio data. |
|||
| voice_pack1 () \[unimplemented\] | Audio conversion tuned for gTTS(ja) |
| music_pack1 () \[unimplemented\] | Nightcore conversion. |

---
### Future  
It's still just a basic voice converter, but I'm hoping to add advanced voice quality conversion as well.
