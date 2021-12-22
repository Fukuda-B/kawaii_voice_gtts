# https://github.com/Fukuda-B/kawaii_voice_gtts

import numpy as np
import pydub
from pydub import effects
from pydub.audio_segment import AudioSegment
import pyworld

class Error(Exception):
    pass

class FileTypeError(Error):
    def __init__(self, message):
        self.message = message

class kawaii_voice:

    def __init__(self, filen):
        # 最初に self.audio に AudioSegment型 としてデータを読み込んでおく
        self.filen = filen
        try:
            self.audio = pydub.AudioSegment.from_file(self.filen)
        except:
            print('Error: The file could not be loaded.')

    def formant(self, val, f0_v):
        '''
            Change formant.
            val : formant rate
            f0_v: f0 rate
        '''
        f_rate = self.audio.frame_rate
        np_arr = np.array(self.audio.get_array_of_samples(), dtype=np.float64) # pydub --> np.array(float64) 変換
        # print(np_arr, f_rate)
        _f0_val, _time = pyworld.dio(np_arr, f_rate) # 基本周波数
        spct = pyworld.cheaptrick(np_arr, _f0_val, _time, f_rate) # スペクトル包絡
        aper = pyworld.d4c(np_arr, _f0_val, _time, f_rate) # 非周期性指標
        spct_b = np.zeros_like(spct)
        for i in range(spct_b.shape[1]):
            spct_b[:, i] = spct[:, int(i/val)]
        ef_audio = pyworld.synthesize(_f0_val*f0_v, spct_b, aper, f_rate)
        ef_audio = ef_audio.astype(np.int16).tobytes()

        # print(ef_audio)
        # print(type(ef_audio))
        new_audio = AudioSegment(
            ef_audio,
            sample_width=self.audio.sample_width,
            frame_rate=f_rate,
            channels=self.audio.channels,
        )
        self.audio = new_audio
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
            opt = 0: 120Hz order=1 --> overlay 
            opt = 1: 120Hz order=1 --> over write
        '''
        bass = self.audio.low_pass_filter(120)
        if opt == 0: self.audio = self.audio.overlay(bass)
        elif opt == 1: self.audio = bass
        return self

    def high_boost(self, opt):
        '''
            opt = 0: 4000Hz order=1 --> overlay
            opt = 1: 4000Hz order=1 --> over write
        '''
        high = self.audio.high_pass_filter(4000)
        if opt == 0: self.audio = self.audio.overlay(high)
        elif opt == 1: self.audio = high
        return self

    def normalize(self):
        self.audio = effects.normalize(self.audio)
        return self

# -----
    def voice_pack1(self):
        ''' high pitch '''
        self = kawaii_voice.pitch(self, 0.4)
        return self

    def voice_pack2(self):
        ''' change formant '''
        self = kawaii_voice.formant(self, 1.2, 1.6)
        self = kawaii_voice.speed(self, 1.07)
        return self

    def music_pack1(self):
        ''' nightcore '''
        self = kawaii_voice.bass_boost(self, 0)
        # self = kawaii_voice.high_boost(self, 0)
        self = kawaii_voice.pitch(self, 0.1)
        # self = kawaii_voice.normalize(self)
        return self

if __name__ == '__main__': pass
