import os
import numpy
import pydub
from pydub import effects
from pydub.playback import play
import pyworld

class Error(Exception):
    pass

class FileTypeError(Error):
    def __init__(self, message):
        self.message = message

class kawaii_voice:

    def __init__(self, filen):
        self.filen = filen
        if self.filen.endswith('.mp3'):
            self.codec = 'mp3'
            self.audio = pydub.AudioSegment.from_mp3(self.filen)
        elif self.filen.endswith('.wav'):
            self.codec = 'wav'
            self.audio = pydub.AudioSegment.from_wav(self.filen)
        elif self.filen.endswith('.ogg'):
            self.codec = 'ogg'
            self.audio = pydub.AudioSegment.from_ogg(self.filen)
        else:
            raise FileTypeError('Not support any format other than wav/mp3/ogg.')

    def formant(self, val):
        '''
        Change formant.
        '''
        np_arr = numpy.array(self.audio.get_array_of_samples()) # pydub -> numpy.array 変換
        _f0_val, _time = pyworld.dio(np_arr, self.audio.frame_rate) # 基本周波数
        spct = pyworld.cheaptrick(np_arr, _f0_val, _time, self.audio.frame_rate) # スペクトル包絡
        aper = pyworld.d4c(np_arr, _f0_val, _time, self.audio.frame_rate) # 非周期性指標

        return self

    def speed(self, val):
        # self.audio = self.audio.speedup(val, 150, 25)
        self.audio = self.audio._spawn(self.audio.raw_data, overrides={"frame_rate": int(self.audio.frame_rate*val)})
        self.audio = self.audio.set_frame_rate(self.audio.frame_rate)
        return self

    def pitch(self, val):
        '''
        Change pitch.
        The criterion is 0.0
        Increasing val by +12 raises it by one octave.
        '''
        nsample_rate = int(self.audio.frame_rate*(2.0**val))
        self.audio = self.audio._spawn(self.audio.raw_data, overrides={"frame_rate": nsample_rate})
        self.audio = self.audio.set_frame_rate(self.audio.frame_rate)        
        return self

    def volume(self, val):
        self.audio += val
        return self

    def bass_boost(self):
        ''' 120Hz order=1 -> overlay '''
        bass = self.audio.low_pass_filter(120)
        self.audio = self.audio.overlay(bass)
        return self

    def high_boost(self):
        ''' 3000Hz order=1 -> overlay '''
        high = self.audio.high_pass_filter(3000)
        self.audio = self.audio.overlay(high)
        return self

    def normalize(self):
        self.audio = effects.normalize(self.audio)
        return self

# -----
    def voice_pack1(self):
        ''' high pitch '''
        return

    def music_pack1(self):
        ''' nightcore '''
        self = kawaii_voice.pitch(self, 0.2)
        self = kawaii_voice.bass_boost(self)
        self = kawaii_voice.normalize(self)
        return self

if __name__ == '__main__': pass
