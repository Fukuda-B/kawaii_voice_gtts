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

    def formant(self, val, f0_v):
        '''
            Change formant.
            val : formant rate
            f0_v: f0 rate
        '''
        f_rate = self.audio.frame_rate
        np_arr = numpy.array(self.audio.get_array_of_samples()) # pydub -> numpy.array 変換
        print(np_arr)
        _f0_val, _time = pyworld.dio(np_arr, f_rate) # 基本周波数
        spct = pyworld.cheaptrick(np_arr, _f0_val, _time, f_rate) # スペクトル包絡
        aper = pyworld.d4c(np_arr, _f0_val, _time, f_rate) # 非周期性指標
        spct_b = numpy.zeros_like(spct)
        for i in range(spct_b.shape[1]):
            spct_b[:, i] = spct[:, int(i/val)]
        self.audio = pyworld.synthesize(_f0_val*f0_v, spct_b, aper, f_rate)
        return self

    def speed(self, val):
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

    def bass_boost(self, opt):
        '''
            opt 0: 120Hz order=1 -> overlay 
            opt 1: 120Hz order=1 -> over write
        '''
        bass = self.audio.low_pass_filter(120)
        if opt == 0: self.audio = self.audio.overlay(bass)
        elif opt == 1: self.audio = bass
        return self

    def high_boost(self, opt):
        '''
            opt 0: 3000Hz order=1 -> overlay
            opt 1: 3000Hz order=1 -> over write
        '''
        high = self.audio.high_pass_filter(3000)
        if opt == 0: self.audio = self.audio.overlay(high)
        elif opt == 1: self.audio = high
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
        self = kawaii_voice.pitch(self, 0.10)
        self = kawaii_voice.bass_boost(self, 0)
        self = kawaii_voice.normalize(self)
        return self

if __name__ == '__main__': pass
