import os
import numpy
import pydub
import pyworld

class Error(Exception):
    pass

class FileTypeError(Error):
    def __init__(self, message):
        self.message = message

class kawaii_voice:

    def __init__(self, filen):
        self.filen = filen
        if self.filen.endwith('.mp3'):
            self.codec = 'mp3'
            self.audio = pydub.AudioSegment.from_mp3(self.filen)
        elif self.filen.endwith('.wav'):
            self.codec = 'wav'
            self.audio = pydub.AudioSegment.from_wav(self.filen)
        elif self.filen.endwith('.ogg'):
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

    def bass_boost(self, val):
        return self

    def normalize(self, val):
        self.audio = self.audio.effects.normalize(self.audio)
        return self

# -----
    def voice_pack1(self):
        ''' high pitch '''
        return

    def music_pack1(self):
        ''' nightcore '''
        return
